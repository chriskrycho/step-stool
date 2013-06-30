__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from os import getcwd, walk
import argparse

# Step Stool modules
import content
from config import Configurator, validate
from render import render_template
from mixins import DictAsMember


def main():
    ''' Either configure the project initially or (re)generate the site. '''
    args = process_args()
    configurator = Configurator(args.directory)
    if not configurator.configured() or args.setup:
        configurator.setup(args.manual_config)
    else:
        config = DictAsMember(configurator.get_config())
        validate(config)
        content.generate_site(config)


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
