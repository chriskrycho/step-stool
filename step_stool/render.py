__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


from logging import error, warning
from sys import exit

try:
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound
except ImportError as import_error:
    error(import_error)
    exit()


class Renderer():
    def __init__(self, config):
        self.template_path = config.site.template.directory
        self.environment = Environment(loader=FileSystemLoader(searchpath=self.template_path))
        self.default_template = self.environment.get_template(config.site.template.default)

    def render_page(self, page):
        if 'template' in page.meta:
            template = self.__get_template(page.meta['template'])
        else:
            template = self.__get_template()

        pass

    def __get_template(self, template_name=None):
        if template_name:
            try:
                template = self.environment.get_template(template_name)
            except TemplateNotFound:
                template = self.default_template
                warning_msg = "Specified template {} not found.'".format(template_name)
                warning(warning_msg)
        else:
            template = self.default_template

        return template
