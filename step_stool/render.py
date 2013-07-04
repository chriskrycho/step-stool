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
    def __init__(self, site_info):
        self.site_info = site_info
        self.template_path = self.site_info.template.directory
        self.environment = Environment(loader=FileSystemLoader(searchpath=self.template_path))
        self.templates = {'default': self.environment.get_template(self.site_info.template.default)}

    def render_page(self, page):
        if 'template' in page.meta:
            template = self.__get_template(page.meta['template'])
        else:
            template = self.__get_template()

        return template.render(site=self.site_info, page=page)

    def __get_template(self, template_name='default'):
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
