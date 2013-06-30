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
# Site configuration. Note that indentation matters to YAML - don't change the
# indentation of existing values! If you extend the file, you can of course
# supply whatever data you like. Note that PyYAML currently only supports the
# YAML 1.1 standard, not YAML 1.2.

site:
  name: Step Stool Demo
  root: http://step-stool.io/demo
  content:
    source: /Users/chris/development/personal_projects/step_stool/sample/source
    destination: /Users/chris/development/personal_projects/step_stool/sample/generated-site
  template:
    directory: /Users/chris/development/personal_projects/step_stool/sample/templates
    default: clean

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
        except FileNotFoundError:
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
        if not config.site.name:
            self.missing_value('site name')
        if not config.site.root:
            self.missing_value('site root')
        if not config.site.content.source:
            self.missing_value('site content source')
        if not config.site.content.destination:
            self.missing_value('site content destination')
        if not config.site.template.directory:
            self.missing_value('site template directory')
        if not config.stie.template.default:
            self.missing_value('site template default')

    def missing_value(self, message):
        base = 'You must supply a value for'
        print(base, message + '.')
        exit()
