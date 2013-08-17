__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
from logging import error, warning
from os import path
from sys import exit

try:
    from yaml import load
    from mixins import DictAsMember
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound

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
  name: # required! cannot be blank
  root: # required! cannot be blank
  content: # leave blank; any value will be ignored
    source: # required! cannot be blank
    destination: # required! cannot be blank
  template:
    directory: # required! should be the path to the template directory
    default: # required! should be the name of the default template *file*
    copy_elements:
      - css
  options:
    posts_per_page: 5 # used on archive, categories, and tags pages
    blog:
      use: true
      slug: # defaults to 'blog'
    categories:
      use: true
      slug: # defaults to 'categories'
      restrict: # if left blank and with no children, categories can be named arbitrarily
    tags:
      use: true
      slug: # defaults to 'tags'
    home:
      use: # use a standalone home page, rather than a list of the latest blog posts(s)
      slug: # the slug (with no extension) from which to generate the index page. See documentation!

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

markdown_extensions: # See http://pythonhosted.org/Markdown/extensions/index.html for a list of extensions
  codehilite: # depends on Pygments (installed by default with
  extra: # includes a number of modules corresponding to the PHP Extra Markdown syntax
  headerid: # adds an ID attribute to header elements in HTML
  meta: # returns metadata from the top of Markdown files (like in MultiMarkdown)
  smartypants: # Smartypants typography
'''

    def __init__(self, directory, run_setup=False, manual_config=False):
        if run_setup or not self.configured(directory):
            self.configuration = self.__config_setup(manual_config)
        else:
            self.configuration = self.get_config()

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
        site = self.configuration.site
        if not site.name:
            self.__missing_value('site name')

        if not site.root:
            self.__missing_value('site root')

        if not site.content.source:
            self.__missing_value('site content source')

        if not site.content.destination:
            self.__missing_value('site content destination')

        if not site.template.directory:
            self.__missing_value('site template directory')

        if not site.template.default:
            self.__missing_value('site template default')

        if site.options.home.use and not site.options.home.slug:
            error('Configuration specified using a home page but no slug provided.')
            exit()

        if not path.exists(site.template.directory):
            self.__bad_path(site.template.directory)

        # TODO: Add handling for missing directories required in template copy

        try:
            directory = site.template.directory
            environment = Environment(loader=FileSystemLoader(directory))
            environment.get_template(site.template.default)

        except TemplateNotFound:
            warning('Default template not found.')
            print('Template name supplied:', site.template.default)
            print('Template directory supplied:', site.template.directory)
            exit()

    def __missing_value(self, value):
        ''' Handle missing values required for site configuration.  '''
        print('You must supply a value for', value + '.')
        exit()

    def __bad_path(self, path):
        print('Sorry, the path', path, 'does not appear to be valid!')
        exit()


def print_default_config(file_path):
    ''' Print a copy of the default configuration and then exit. '''
    with open(file_path, 'w') as file:
        file.write(Configurator.DEFAULT_CONFIG)
        exit()
