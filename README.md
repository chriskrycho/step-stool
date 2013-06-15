Step Stool
==========

A static website generator (in Python).

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

[python]: http://www.python.org/download/ "Download Python 3 for your platform"

[vw]: https://bitbucket.org/dhellmann/virtualenvwrapper "Extensions to Ian Bickings virtualenv tool"

[yaml]: http://www.yaml.org/