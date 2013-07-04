__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from logging import error
from os import getcwd, path, walk
from sys import exit
import argparse

# Step Stool modules
try:
    import content
    import config
    import render
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
    args = parse_args()
    process_args(args)
    configurator = config.Configurator(directory=args.directory, run_setup=args.setup)
    converted_documents = content.convert_source(configurator.configuration)
    site = content.build_site(configurator.configuration.site, converted_documents)
    content.write_site(configurator.configuration.site, site)


def parse_args():
    program_desc = 'Configure a new Step Stool site or (re)build an existing site.'
    program_name = 'Step Stool'
    parser = argparse.ArgumentParser(prog=program_name, description=program_desc)

    parser.add_argument('-d', '--working-dir', help='Set the working directory for Step Stool',
                        metavar='<working directory>', dest='directory', default=getcwd())
    parser.add_argument('-m', '--manual-config', help='Configure the site manually',
                        action='store_true', dest='manual_config')
    parser.add_argument('--setup', help='Re-run the setup command (same as first run in directory)',
                        action='store_true', default=False)
    parser.add_argument('--copy_defaults', action='store', metavar='<filename>',
                        help='Generate a copy of the default configuration file for reference, then exit.')

    args = parser.parse_args()
    return args


def process_args(args):
    if args.copy_defaults:
        file_name = args.copy_defaults
        file_path = path.join(getcwd(), file_name) if path.isabs(file_name) else file_name
        config.print_default_config(file_path)


if __name__ == '__main__':
    main()
