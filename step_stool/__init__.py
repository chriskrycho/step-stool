__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from logging import error
from os import getcwd, walk
from sys import exit
import argparse

# Step Stool modules
try:
    import content
    from config import Configurator
    from render import render_template
    from mixins import DictAsMember

except ImportError as import_error:
    error(import_error)
    exit()


def main():
    '''
    Generate the site:

    - Get the site configuration
        + Configure the project initially, or
        + Pull in the existing site configuration
    - Get and convert any/all content in the content directory
    - Render the content
    '''
    args = process_args()
    configurator = Configurator(directory=args.directory, run_setup=args.setup)
    converted_content = content.convert_source(configurator.config)
    content.generate_site(configurator.config, converted_content)


def process_args():
    program_desc = 'Configure a new Step Stool site or (re)build an existing site.'
    program_name = 'Step Stool'
    parser = argparse.ArgumentParser(prog=program_name, description=program_desc)

    parser.add_argument('-d', '--working-dir', help='Set the working directory for Step Stool',
                        metavar='<working directory>', dest='directory', default=getcwd())
    parser.add_argument('-m', '--manual-config', help='Configure the site manually',
                        action='store_true', dest='manual_config')
    parser.add_argument('--setup', help='Re-run the setup command (same as first run in directory)',
                        action='store_true', default=False)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
