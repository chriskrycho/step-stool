__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'

from collections import namedtuple
from logging import error
from os import path, walk
from sys import exit

try:
    from markdown import Markdown
    from mixins import DictAsMember

except ImportError as import_error:
    error(import_error)
    exit()


Content_Pair = namedtuple('Content_Pair', ['html', 'meta'])


def convert_source(config):
    '''
    Convert all Markdown pages to HTML and metadata pairs. Pairs are keyed to
    file names slugs (without the original file extension).
    '''

    md = Markdown(extensions=config.markdown_extensions, output_format='html5')
    converted_content = {}
    for root, dirs, file_names in walk(config.site.content.source):
        for file_name in file_names:
            file_path = path.join(root, file_name)
            plain_slug, extension = path.splitext(file_name)

            with open(file_path, 'r') as file:
                md_text = file.read()
                html = md.convert(md_text)
                converted_content[plain_slug] = Content_Pair(html, md.Meta)
                md.reset()

    return converted_content


def generate_site(config, content):
    pages = generate_pages(config, content)
    archive = generate_archive(config, content)
    categories = generate_categories(config, content) if config.site.render_options.categories.use else None
    tags = generate_tags(config, content) if config.site.render_options.tags.use else None

    home = generate_home(config, content) if config.site.render_options.home.use else archive


def generate_archive(config, content):
    for page in content:
        pass
    return content


def generate_categories(config, content):
    return content


def generate_home(config, content):
    '''
    Generate the index page based on the settings in config. If the site is set
    to use a home page and supplied a home page slug, it will attempt to use a
    file with that slug. If the site is set to use a home page and no home slug
    exists, an error is printed. If the site is not set to use a home page, the
    function returns immediately.
    '''
    if not config.site.render_options.home.use:
        return None


def generate_pages(config, content):
    '''
    Generate each of the standalone pages. Pages are rendered using a template
    specified in the file's meta, if (1) a template is specified there and (2)
    a template with that name is available. If no template file with that name
    exists, or if none is specified in the meta, the default is used.
    '''
    pages = {}
    for page in content:
        pass
    return pages


def generate_tags(config, content):
    return content


def paginate(posts_per_page, content):
    return content


class Page():
    def __init__(self):
        pass
