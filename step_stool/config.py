__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
import os.path as path

# Dependency modules
from yaml import load


class Configurator():
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
            return load(self.file_name)
        except FileNotFoundError:
            pass

    def setup(self, manual_config):
        '''
        Set up an instance of Step Stool

        - Generate a configuration file
        - Populate the configuration file:
            * with defaults, if manual configuration specified
            * with user inputs, otherwise
        '''

        config = load(self.default_config)
        if not manual_config:
            pass

    default_config = '''\
# Basic site configuration
site_name: Step Stool Demo
root: http://step-stool.io/demo
content_source: /Users/chris/development/personal_projects/step-stool/sample/source
content_output: /Users/chris/development/personal_projects/step-stool/sample/generated-site
default_template: clean

# Publication configuration
remote:
  - push: true
  - push_method: # must be one of ssh, sftp, or ftp-ssl

git:
  - push: false
  - repository:
  - push_method: # must be one of local, ssh, or https
  - https_username: # only required if pushing via https - NOT RECOMMENDED
  - https_password: # only required if pushing via https - NOT RECOMMENDED

hg:
  - push: false
  - repository:
  - push_method: # must be either local, ssh, or https
  - https_username: # only required if pushing via https - NOT RECOMMENDED
  - https_password: # only required if pushing via https - NOT RECOMMENDED

# Detailed configuration
archives:
  - generate: true
  - categories: true
  - tags: true
  - author: false
'''
