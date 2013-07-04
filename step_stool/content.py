__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'

from collections import namedtuple
from logging import error
from os import path, walk, remove
from shutil import copytree, copy, rmtree
import errno
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


def build_site(site_config, documents):
    renderer = render.Renderer(site_config)
    options = site_config.options

    output = {
        'pages': __build_pages(documents, renderer),
        'blog': __build_blog(documents, renderer) if options.blog.use else None,
        'categories': __build_categories(documents, renderer) if options.categories.use else None,
        'tags': __build_tags(documents, renderer) if options.tags.use else None}

    output['home'] = __build_home(options.home, documents, renderer) if options.home.use else output['blog']

    return output


def write_site(site_config, output):
    '''
    Write all the content in output to files by slug with extension `.html`,
    then copy any necessary files from the template directory (e.g. Javascript
    or CSS) to the output directory.
    '''
    for element in output:
        if output[element]:
            for slug in output[element]:
                output_path = path.join(site_config.content.destination, slug + OUTPUT_EXTENSION)
                with open(output_path, 'w') as file:
                    file.write(output['pages'][slug])

    __copy_required_template_elements(site_config)


def __build_blog(documents, renderer):
    pages = {}
    for page in documents:
        pass
    return pages


def __build_categories(documents, renderer):
    pages = {}
    return pages


def __build_home(home_options, documents, renderer):
    '''
    Generate the index page based on the settings in config. If the site is set
    to use a home page and supplied a home page slug, it will attempt to use a
    file with that slug. If the site is set to use a home page and no home slug
    exists, an error is printed. If the site is not set to use a home page, the
    function returns immediately.
    '''
    pages = {}
    if home_options.use and home_options.slug not in documents:
            error('Specified slug {} not in list of documents supplied. Could not build home page.'.format(
                home_options.slug))
    else:
        slug = home_options.slug



def __build_pages(documents, renderer):
    '''
    Generate each of the standalone pages. Pages are rendered using a template
    specified in the file's meta, if (1) a template is specified there and (2)
    a template with that name is available. If no template file with that name
    exists, or if none is specified in the meta, the default is used. Note that
    a 'page' is *any* page on the site, not just standalone, non-blog pages.
    '''
    pages = {}

    for slug in documents:
        pages[slug] = renderer.render_page(documents[slug])

    return pages


def __build_tags(documents, renderer):
    return None


def __copy_required_template_elements(site_config):
    copy_names = site_config.template.copy_elements
    copy_sources = [path.join(site_config.template.directory, copy_name) for copy_name in copy_names]
    copy_destinations = [path.join(site_config.content.destination, copy_name) for copy_name in copy_names]
    copy_pairs = zip(copy_sources, copy_destinations)
    for source, destination in copy_pairs:
        if path.exists(destination):
            rmtree(destination)

        try:
            copytree(source, destination)
        except OSError as exc:
            if exc.errno == errno.ENOTDIR:
                copy(source, destination)
            else:
                raise


def __paginate(posts_per_page, documents):
    return documents
