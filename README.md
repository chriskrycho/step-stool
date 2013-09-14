Step Stool
==========

A static website generator (in Python).

Current Version: 0.0.1

Introduction
------------

Step Stool is a simple static site generator. You write your content in
[Markdown][md], run a quick command line script, and it gets published to the
web. No content management system, no database, just simple HTML files.

Step Stool supports custom templates (via [Jinja2][jinja]), so you can make
your site look pretty much however you want. You can apply different templates
to different sections of your site, using a single line in a configuration file.

Step Stool also allows you to structure your site pretty much however you
choose. If you want to have nested categories, go for it. If you want an
entirely flat structure with an ever-growing list of tags, you can do that, too.

Setup
-----

### Installation

Note: I hope in later versions to create a bundled app-style version of the
software that can be used by non-technical folks. For the 1.0 series, however,
my goal is simply to get this up and going at a level where *I* can use it.

#### Dependencies

To install Step Stool, you'll need at least [Python 3.0][python]. If you
don't have it, you'll need to get it:

  - [Download it][python] and install it manually.
  - Use a package manager to install it (e.g. `brew install python`, `aptitude
    install python`, etc.).

That's it. (All the Python package dependencies will take care of themselves
when you install the package.)

#### Walkthrough

The easiest way to install Step Stool is using `pip`, which also installs
all dependencies for using Step Stool:

    :::sh
    $ pip install step-stool

I recommend using a virtual environment for this install, to keep it separate
from your other (system or project) Python setups. If you have
[virtualenvwrapper][vw] installed:

    :::sh
    $ mkvirtualenv step-stool
    $ setvirtualenvproject /path/where/you/want/to/build/your/site
    $ pip install step-stool

Otherwise, since we're running Python 3, you can just do (preferably in a
virtual environments directory somewhere in your home folder or some such):

    :::sh
    $ pyvenv step-stool
    $ pip install step-stool

Alternatively, you can download the package manually from the [downloads
page][download] and run:

    :::sh
    $ python setup.py

### Configuration

Once Step Stool has been installed, you can simply run it from the command line:

    $ step-stool

By default, Step Stool will set up a project in the directory where you run it,
but you can run it anywhere and tell it the directory in which to run (see
options below).

#### Configuration Tool Options

The following options can be passed to the configuration tool:

  - `-d`, `--working-dir`: Set the installation directory
  - `-m`, `--config-manually`: Configure the project manually (see below for
    detailed information on the configuration file). With this option set, Step
    Stool will generate a default (unconfigured) configure file in the root for
    the project and then exit.
  - `setup`: Re-run the initial setup sequence. (Ignored if )

#### The configuration file

All the settings are stored in a [YAML][yaml] file in the directory where you
initialized the project (either by running Step Stool in that directory or by
passing it as an argument with the `-d` flag).

##### Site

Site configuration is straightforward: simply supply the relevant values in each
of the required fields, and any additional fields you desire. The default
configuration has pretty sane options for most options that *have* defaults, and
great big warning flag comments for the required options. If you don't put in
the required fields, Step Stool will stop and yell at you (or at least print
error messages telling you that you need those fields filled in) when you try to
run it.

The required options are:

  - `name`: the name of the web site
  - `root`: the web address of the site you are generating. For example, in the
    Step Stool website configuration, this is `http://step-stool.io/`
  - `content`: (not required, and in fact ignored... but its *children* are
    required)
      * `source`: the absolute address of the place you want to put the Markdown
        files you write on your spiffy new site. When I say absolute address, I
        mean something like `/Users/chris/Documents/writing/my-site` (on a Mac
        or Linux system) or `C:\Users\chris\Documents\writing\my-site` (on
        Windows).
      * `destination`: the absolute address of the palce you want the generated
        content to go when Step Stool finishes with it.

###### Options

Most of the options are fairly self-explanatory, but here are a few notes on
each nonetheless.

  - `posts_per_page`:

  - `blog`: allows the user to set whether to create a specific page on which to
    display the blog archives. If you're using Step Stool to manage a site for
    which the blog is just one piece, for example, you'd set the `use` value to
    `true` and supply whatever slug you like for `slug`. If you do not want a
    blog at all, you can simply set `use` to `false`.

  - `categories`: allows the user to set whether or not category pages are
    generated. If the user sets `use` to `false`, any category metadata in the
    Markdown documents will simply be ignored. If the user sets `use` to `true`,
    archive pages for each distinct category will be generated and can be linked
    from the template at the user's convenience.

    If the user provides a value for `slug`, that will be used as the root for
    the category archive pages; otherwise the category archive pages will be
    located at `<site>/categories/<category-name>`. For example, on the Step
    Stool site, the history category is at
    <http://step-stool.io/categories/history/>.[^1]

    If you include any values under the `restrict` option, Step Stool will
    print an error message for any file that does not match one of the options
    listed. The file will still be generated, but its category metadata will be
    stripped.

  - `tags`: exactly like `categories`, except that at present, there is no
    support for restricting the list of tags -- that rather defeats the purpose
    of most tagging systems.

  - `home`: allows the user to specify a page to display at the index of the
    site distinct from the standard blog archive page. Step Stool will look for
    a file with the slug specified in the `source` directory specified under the
    site configuration. If it finds the slug, it will convert the contents of
    that page using either the default template name supplied in the site
    configuration or the template specified in the file metadata. The file
    generated will be saved as `index.html`. (Otherwise, `index.html` has the
    contents of the blog archive.)

    If you want a custom-build landing page, you can simply supply a Markdown
    file with no content other than metadata specifying the template, and fill
    out the template file with standard HTML. (Note that the same trick will
    work for ordinary standalone pages, as well.)

*Note:* If you do *not* choose to use the `home` page and you *do* choose to use
the `blog` setting, Step Stool will generate a page at the slug specified
(`blog` if you do not specify one yourself) that will be identical to the index
page, listing all the blog archives.

##### Publication

##### Markdown Extensions

For a full list of Markdown extensions you can enable, see [here][md-ext].

#### Templating

All article information is supplied to the template in the `article` object.
Each `article` includes the following properties:

  - `content`: the HTML body of the article, based on the Markdown document
  - `meta`:

You can then use the `article` objects

#### Pages and Posts

Writing and Publishing
----------------------

### Blogging

Step Stool works quite well for blogging (that is, in fact, what inspired me to
write it: I wanted my own blogging platform, over which I had complete control.)
To write blog posts, just include a piece of date metadata at the top of your
Markdown file, like this:

    Date: 2013-09-07

    Here is my super great blog post---don't you love it?

You can read more about metadata
[here](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-
Guide). Note that the first piece of metadata *has* to be on the first line of
the file; otherwise the Markdown processor assumes it is regular content. As
soon as you include a completely blank line, the Markdown processor assumes you
are done with metadata and goes back to processing everything else normally---so
the formatting on this first section matters quite a bit.

The default Step Stool theme makes use of the following pieces of
metadata, if you supply them. Note that neither the titles nor the option
values of the fields are case-sensitive.

  - Author(s): Fairly self-explanatory: the author (or authors) of the post in
    question. You can supply `Author` or `Authors`; Step Stool will understand
    either one and yield the same result.

  - Category: Specify one or more categories in which to publish the post.
    Ignored if categories or the blog functionality are not enabled.

  - Date: Specify the date the post is to be published. Ignored if the `Type`
    field is included and set to anything other than `post`. At present, this
    must be of the form `YYYY-MM-DD HH:MM`, though I will increase the date
    field's flexibility in the future.

  - Published: Keep the page from being published. If the user supplies `no` or
    `false` (case insensitive), the page/post will not be published. Any other
    value is simply ignored.

  - Slug: Specify a slug different from the file name with which the file is
    saved to use as the link to the page. By default, Step Stool just assumes
    the slug for your Markdown file should be the slug for the HTML file it
    generates; this lets you change that. Thus, you could have a file named
    `2013-09-08.md` but supply `my-first-post` as the value here and the
    resulting HTML file would be named `my-first-post.html` instead of
    `2013-09-08.html`.

  - Tags: Specify one or more tags in which to publish the post. Ignored if tags
    or the blog functionality are not enabled.

  - Template: Specify a template other than the default with which to render the
    page.

  - Title: Just what it says---title for the post or page.[^blogging-title-note]

  - Type: Specify that the element is one of `page` or `post` (case
    insensitive)---the default is `post` if no value is supplied.

[^blogging-title-note]: Note on themes: If you leave this off, the default theme
will still render everything just fine, but if a theme depends on it and the
post doesn't supply it, the renderer will fail (but it will tell you so).

If you do not supply a date at all *and* you do not set the `Type` option to
`page`, the post simply won't be published (even if you include `Published:
True`). If you supply a date with no time, Step Stool will supply midnight in
the time zone your computer uses as the full time for the post. This is
important because Step Stool uses the date and time to sort posts for
publication, as well any places it may be included in a theme, of course.

#### Sample

For a full-length sample of a blog post, see the source for the website. As a
brief example, consider the following (assume it is saved as `2013-09-08.md`):

    Title: My first blog post using Step Stool!
    Date: September 8, 2013
    Author: Chris Krycho
    Category: Information/Demo
    Tags: writeup, sample, infodump
    Slug: my-first-post

    Here, I might have the basic content of my first, extra-fun post using my
    new blogging software. I would go on, and on, and on about how amazing it is
    to be using software I wrote myself, and very soon I would bore you all to
    tears.

    Instead, I will just call it good and end this sample right here.

The result would be something like this (greatly simplified, of course, and note
the slug for the "permalink" to the article in the header link):

    <html>
    <head>
        <title>My first blog post using Step Stool!</title>
    </head>
    <body>
        <article>
            <a href="my-first-post.html">
                <h1>My first blog post using Step Stool!</h1>
            </a>
            <div class="meta">
                <span class="author">by Chris Krycho</span>
                <span class="date">September 8, 2013</span>
                <span class="category">Information > Demo</span>
                <span class="tags">writeup, sample, infodump</span>
            </div>

            <p>Here, I might have the basic content of my first, extra-fun post
            using my new blogging software. I would go on, and on, and on about
            how amazing it is to be using software I wrote myself, and very soon
            I would bore you all to tears.</p>

            <p>Instead, I will just call it good and end this sample right
            here.</p>

        </article>
    </body>
    </html>

Different themes will do different things with those elements, but this gives a
very basic idea of how the content might come out as you supply those different
pieces of metadata.

Theming
-------

You can write your own themes for Step Stool fairly easily. The default template
distributed with Step Stool shows a simple but thorough use of the facilities
provided by the software, including how to use metadata, and how to create
different templates for different kinds of pages. You can also look at the
template for the Step Stool site to see a fairly different approach.[^theming]

[^theming]: Well, you *will* be able to, anyway... once I get this sufficiently
far along that I can generate Step Stool with it.

For ordinary pages or posts, the renderer starts with any template specified in
the file metadata, then falls back to the base template specified in the
configuration file. For categories and tags pages, if you supply a template in
the configuration, the renderer will look for that template; if it doesn't find
it, it will fall back to the base template as well.

Miscellanies
------------

### Why "Step Stool"?

A step stool helps you get just a little higher. It's not a ladder, and it's
definitely not a powered lift to do work on street lamps. It just makes a
process a wee little bit easier. That's what Step Stool does: it automates
generation of HTML from templates. It doesn't tell you what the templates should
look like, and it doesn't interact with a database, or generate pages
dynamically, or do much of anything other than turn Markdown into HTML. It's a
step stool.



[download]: /

[jinja]: http://jinja.pocoo.org/ "Jinja 2 Python Templating Language"

[md]: http://daringfireball.net/projects/markdown/

[md-ext]: http://pythonhosted.org/Markdown/extensions/

[python]: http://www.python.org/download/ "Download Python 3 for your platform"

[vw]: https://bitbucket.org/dhellmann/virtualenvwrapper "Extensions to Ian Bickings virtualenv tool"

[yaml]: http://www.yaml.org/



[^1]: Well, it will be, anyway -- once I get to the point where I can generate
Step Stool itself with Step Stool.
