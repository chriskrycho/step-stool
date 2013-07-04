__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'

from collections import namedtuple
from logging import error
from os import path, walk
from sys import exit

try:
    from markdown import Markdown
    from mixins import DictAsMember
    import render

except ImportError as import_error:
    error(import_error)
    exit()


Content_Pair = namedtuple('Content_Pair', ['content', 'meta'])
OUTPUT_EXTENSION = '.html'


def convert_source(config):
    '''
    Convert all Markdown pages to HTML and metadata pairs. Pairs are keyed to
    file names slugs (without the original file extension).
    '''
    md = Markdown(extensions=config.markdown_extensions, output_format='html5')
    converted_documents = {}
    for root, dirs, file_names in walk(config.site.content.source):
        for file_name in file_names:
            file_path = path.join(root, file_name)
            plain_slug, extension = path.splitext(file_name)

            with open(file_path, 'r') as file:
                md_document = file.read()
                html_document = md.convert(md_document)
                converted_documents[plain_slug] = Content_Pair(html_document, md.Meta)
                md.reset()

    return converted_documents


def generate_site(config, documents):
    pages = generate_pages(config, documents)
    blog = generate_blog(config, documents) if config.site.options.blog.use else None
    categories = generate_categories(config, documents) if config.site.options.categories.use else None
    tags = generate_tags(config, documents) if config.site.options.tags.use else None

    home = generate_home(config, documents) if config.site.options.home.use else blog

    for slug in pages:
        output_path = path.join(config.site.content.destination, slug + OUTPUT_EXTENSION)
        with open(output_path, 'w') as file:
            file.write(pages[slug])


def generate_blog(config, documents):
    for page in documents:
        pass
    return documents


def generate_categories(config, documents):
    return documents


def generate_home(config, documents):
    '''
    Generate the index page based on the settings in config. If the site is set
    to use a home page and supplied a home page slug, it will attempt to use a
    file with that slug. If the site is set to use a home page and no home slug
    exists, an error is printed. If the site is not set to use a home page, the
    function returns immediately.
    '''
    if not config.site.options.home.use:
        return None


def generate_pages(config, documents):
    '''
    Generate each of the standalone pages. Pages are rendered using a template
    specified in the file's meta, if (1) a template is specified there and (2)
    a template with that name is available. If no template file with that name
    exists, or if none is specified in the meta, the default is used. Note that
    a 'page' is *any* page on the site, not just standalone, non-blog pages.
    '''
    pages = {}
    renderer = render.Renderer(config.site)
    for slug in documents:
        pages[slug] = renderer.render_page(documents[slug])

    return pages


def generate_tags(config, documents):
    return documents


def paginate(posts_per_page, documents):
    return documents


class Page():
    def __init__(self):
        pass
