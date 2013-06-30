__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from logging import error
from os import path
from sys import exit

try:
    from yaml import load
    from mixins import DictAsMember

except ImportError as import_error:
    error(import_error)
    exit()


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
  posts_per_page: 5 # used on archive, categories, and tags pages

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

    def __init__(self, directory, run_setup=False, manual_config=False):
        if run_setup or not self.configured(directory):
            self.config = self.__config_setup(manual_config)
        else:
            self.config = self.get_config()

        self.__validate()

    def configured(self, directory):
        '''
        Check whether the directory has a configuration file already. If the file
        exists, assume it has been configured.
        '''
        full_path = path.join(directory, 'config.yaml')
        if path.exists(full_path):
            self.file_name = full_path
            return True
        else:
            return False

    def get_config(self):
        try:
            stream = open(self.file_name, 'r')
            yaml = load(stream)
            return DictAsMember(yaml)

        except FileNotFoundError:
            exit('Could not find your configuration file (config.yaml). Is it missing?')

    def __config_setup(self, manual_config):
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

        return config

    def __validate(self):
        ''' Check whether the required site configuration elements are set. '''
        if not self.config.site.name:
            self.__missing_value('site name')
        if not self.config.site.root:
            self.__missing_value('site root')
        if not self.config.site.content.source:
            self.__missing_value('site content source')
        if not self.config.site.content.destination:
            self.__missing_value('site content destination')
        if not self.config.site.template.directory:
            self.__missing_value('site template directory')
        if not self.config.site.template.default:
            self.__missing_value('site template default')

    def __missing_value(self, value):
        ''' Handle missing values required for site configuration.  '''
        base = 'You must supply a value for'
        print(base, value + '.')
        exit()
