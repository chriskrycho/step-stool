__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from os import getcwd
import argparse

# Step Stool modules
import content
from config import Configurator
import render


def main():
    '''
    Either configure the project initially or (re)generate the site.
    '''
    args = process_args()
    config = Configurator(args.directory)
    if not config.configured() or args.setup:
        config.setup(args.manual_config)
    else:
        generate_site(config.get_config())


def generate_site(config):
    '''
    Generate the site:

    - Get the site configuration
    - Get all the content from the content directory
    - Render the content
    '''
    pass


def process_args():
    program_desc = 'Configure a new Step Stool site or (re)build an existing site.'
    program_name = 'Step Stool'
    parser = argparse.ArgumentParser(prog=program_name, description=program_desc)

    parser.add_argument('-d', '--working-dir', help='Set the working directory for Step Stool',
                        metavar='<working directory>', dest='directory', default=getcwd())
    parser.add_argument('-m', '--manual-config', help='Configure the site manually',
                        action='store_true', dest='manual_config')
    parser.add_argument('--setup', help='Re-run the setup command (ignored if first run in directory)',
                        action='store_true')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
