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

    :::bash
    $ pip install step-stool

I recommend using a virtual environment for this install, to keep it separate
from your other (system or project) Python setups. If you have
[virtualenvwrapper][vw] installed:

    :::bash
    $ mkvirtualenv step-stool
    $ setvirtualenvproject /path/where/you/want/to/build/your/site
    $ pip install step-stool

Otherwise, since we're running Python 3, you can just do (preferably in a
virtual environments directory somewhere in your home folder or some such):

    :::bash
    $ pyvenv step-stool
    $ pip install step-stool

Alternatively, you can download the package manually from the [downloads
page][download] and run:

    :::bash
    $ python setup.py

### Configuration

#### The configuration file

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