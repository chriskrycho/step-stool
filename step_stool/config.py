__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from os import path
from sys import exit

# Dependency modules
from yaml import load


class Configurator():
    ''' Configure the site. '''

    DEFAULT_CONFIG = '''\
# Basic site configuration
site:
  site_name: Step Stool Demo
  root: http://step-stool.io/demo
  content_source: /Users/chris/development/personal_projects/step_stool/sample/source
  content_output: /Users/chris/development/personal_projects/step_stool/sample/generated-site
  template_directory: /Users/chris/development/personal_projects/step_stool/sample/templates
  default_template: clean

# Publication configuration
publication:
  remote:
    push: true
    push_method: # must be one of ssh, sftp, or ftp-ssl

  git:
    push: false
    repository: # ignored if push = false
    push_method: # must be one of local, ssh, or https
    https_username: # only required if pushing via https - NOT RECOMMENDED
    https_password: # only required if pushing via https - NOT RECOMMENDED

  hg:
    push: false
    repository: # ignored if push = false
    push_method: # must be either local, ssh, or https
    https_username: # only required if pushing via https - NOT RECOMMENDED
    https_password: # only required if pushing via https - NOT RECOMMENDED

# Detailed configuration
archives:
  generate: true
  categories: true
  tags: true
  author: false

markdown_extensions: # See http://pythonhosted.org/Markdown/extensions/index.html for a list of extensions
  codehilite: # depends on Pygments (installed by default with
  extra: # includes a number of modules corresponding to the PHP Extra Markdown syntax
  headerid: # adds an ID attribute to header elements in HTML
  meta: # returns metadata from the top of Markdown files (like in MultiMarkdown)
  smartypants: # Smartypants typography
'''

    def __init__(self, directory):
        self.directory = directory
        self.file_name = ''

    def configured(self):
        '''
        Check whether the directory has a configuration file already. If the file
        exists, assume it has been configured.
        '''
        full_path = path.join(self.directory, 'config.yaml')
        if path.exists(full_path):
            self.file_name = full_path
            return True
        else:
            return False

    def get_config(self):
        try:
            stream = open(self.file_name, 'r')
            return load(stream)
        except FileNotFoundError as file_not_found:
            exit('Could not find your configuration file. Is it missing?')

    def setup(self, manual_config):
        '''
        Set up an instance of Step Stool

        - Generate a configuration file
        - Populate the configuration file:
            * with defaults, if manual configuration specified
            * with user inputs, otherwise
        '''

        config = load(self.DEFAULT_CONFIG)
        if not manual_config:
            # TODO: Input `m` at any time to finish configuration manually
            # TODO: Site name
            # TODO: Website URL
            # TODO: Content source
            # TODO: Where to store generated content
            # TODO: Friendly message!
            # TODO: Remote publishing: y/n
            pass

    def validate(self, config):
        pass

