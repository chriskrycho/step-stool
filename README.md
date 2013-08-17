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

### Setup

### Installation

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
the required fields, Step Stool will stop and yell at you when you try to run
it. Or at least print error messages telling you that you need those fields
filled in. The required options are:

- `name`: the name of the web site
- `root`: the web address of the site you are generating. For example, in the
  Step Stool website configuration, this is `http://step-stool.io/`
- `content`: (not required, and in fact ignored... but its *children* are
  required)
    * `source`: the absolute address of the place you want to put the Markdown
      files you write on your spiffy new site. When I say absolute address, I
      mean something like `/Users/chris/Documents/writing/my-site` (on a Mac or
      Linux system) or `C:\Users\chris\Documents\writing\my-site` (on Windows).
    * `destination`: the absolute address of the palce you want the generated
      content to go when Step Stool finishes with it.

###### Options

Most of the options are fairly self-explanatory, but here are a few notes on
each nonetheless.

- `posts_per_page`:
- `blog`: allows the user to set whether to create a specific page on which to
  display the blog archives. If you're using Step Stool to manage a site for
  which the blog is just one piece, for example, you'd set the `use` value to
  `true` and supply whatever slug you like for `slug`. If you do not want a blog
  at all, you can simply set `use` to `false`.

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

- `tags`: exactly like `categories`, except that at present, there is no support
  for restricting the list of tags -- that rather defeats the purpose of most
  tagging systems.

- `home`: allows the user to specify a page to display at the index of the site
  distinct from the standard blog archive page. Step Stool will look for a file
  with the slug specified in the `source` directory specified under the site
  configuration. If it finds the slug, it will convert the contents of that
  page using either the default template name supplied in the site
  configuration or the template specified in the file metadata. The file
  generated will be saved as `index.html`. (Otherwise, `index.html` has the
  contents of the blog archive.)

  If you want a custom-build landing page, you can simply supply a Markdown file
  with no content other than metadata specifying the template, and fill out the
  template file with standard HTML. (Note that the same trick will work for
  ordinary standalone pages, as well.)

*Note:* If you do *not* choose to use the `home` page and you *do* choose to use
the `blog` setting, Step Stool will generate a page at the slug specified
(`blog` if you do not specify one yourself) that will be identical to the index
page, listing all the blog archives.

##### Publication

##### Markdown Extensions

For a full list of Markdown extensions you can enable, see [here][md-ext]

#### Templating

All article information is supplied to the template in the `article` object.
Each `article` includes the following properties:

- `content`: the HTML body of the article, based on the Markdown document
- `meta`:

You can then use the `article` objects

#### Pages and Posts

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
