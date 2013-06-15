__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
import argparse

# Step Stool modules
import content
import config
import render


def main():
    '''
    Either configure the project initially or (re)generate the site.
    '''
    args = process_args()
    #if not config.configured(args['working-dir']) or args['setup']:
     #   config.setup()


def process_args():
    program_desc = 'Configure a new Step Stool site or (re)build an existing site.'
    program_name = 'Step Stool'
    parser = argparse.ArgumentParser(prog=program_name, description=program_desc)

    parser.add_argument('-d', '--working-dir', help='Set the working directory for Step Stool',
                        metavar='<working directory>')
    parser.add_argument('-m', '--config-manually', help='Configure the site manually', action='store_true')
    parser.add_argument('--setup', help='Re-run the setup command (ignored if first run in directory)',
                        action='store_true')

    args = parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    main()
