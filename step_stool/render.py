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
    DEFAULT_NAME = 'default'

    def __init__(self, site_info):
        self.site_info = site_info
        self.template_path = self.site_info.template.directory
        self.environment = Environment(loader=FileSystemLoader(searchpath=self.template_path))
        self.templates = {'default': self.environment.get_template(self.site_info.template.default)}

    def render_page(self, page):
        template_name = page.meta['template'] if 'template' in page.meta else self.DEFAULT_NAME
        template = self.__get_template(template_name)
        return template.render(site=self.site_info, pages=[page])

    def render_page_set(self, pages, template_name=DEFAULT_NAME):
        template = self.__get_template(template_name)
        return template.render(site=self.site_info, pages=pages)

    def __get_template(self, template_name):
        '''
        Retrieve the template for rendering using Environment::get_template.
        Start by checking templates already stored by previous calls to this
        method (minimizing calls to the file system).
        '''
        if template_name in self.templates:
            template = self.templates[template_name]
        else:
            try:
                template = self.environment.get_template(template_name)
                self.templates[template_name] = template
            except TemplateNotFound:
                template = self.templates['default']
                warning_msg = "Specified template {} not found.'".format(template_name)
                warning(warning_msg)

        return template
