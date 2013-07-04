Title:      Progress Update #1: Configuration and Generating Content
Author:     Chris Krycho
Published:  true
Type:       post
Date:       2013-06-30 21:00 EST
Category:   History

Courtesy of some extra free time I've had near the end of the month, I've been
able to make substantially more progress on Step Stool. Tonight, I'm hoping to
generate the first piece(s) of content using a Jinja2 template and this and the
[previous](/first-steps/) post.

You can see the (stuttering) progress I've made in the interval by taking a
look at the [revision history][history] up through today. I've been primarily
focusing on getting the configuration pieces in place and getting the
conversion working properly. With both of those in place and much of the
initialization and argument-handling done, the next step is to start actually
generating content and building out the default template (as well as,
eventually, a template for the Step Stool [site](http://step-stool.io/) so that
it can be built using Step Stool).

Some of the biggest pieces I still need to set up in terms of configuration are
menus (which I simply need to decide how to handle!) and RSS feed settings. The
latter are particularly low in the priority list, however, as the PyRSS2Gen
module should cover most of my needs quite thoroughly. The focus, for the
moment, is just getting a handle on templating and inheritance. After that I'll
start dealing with pagination; once I have a single pagination function written
I'll integrate it into the archives, tags, and categories elements. *Then* I
can start dealing with menu items,[^1] and after that will come things like the
RSS feed.

There are two *major* features that I want to implement once I finish the first
pass on the generator (I guess for the 1.1 "release," since the first release
will be 1.0 -- we're currently on 1.0a. At best). The two killer features that
I simply haven't seen implemented in a way that I like in another generator:

- image uploads
- caching

I'd like the tool to be able to handle image uploads easily. This is non-
trivial, which is why I don't think any of the other site generators do it.
(I don't know of any that do, certainly! If you know of one, please tell me.)
My first pass will almost certainly rely on version-control systems, as it's
straightforward, if not trivial, to manage images with those: if they're not
in the repository, add them to the repository. If they're in the repository,
move on with life. The tricky things are automating image removal and dealing
with images that are *not* in version controlled sites (or which are, but when
users would like to upload them somewhere else).

Caching would be helpful because it would allow me to minimize the amount of
site regeneration to be done each time. This, too, is a non-trivial project. It
would be really helpful in at least two ways, though. First, it would minimize
the time running Step Stool takes the majority of the time: if the content
hasn't changed, don't regenerate it. (The trick there is doing it in such a way
that it doesn't come out as a wash with just regenerating the content.) I
should probably also be able to work in automatic deletion of items this way,
though that will also require a few more configuration settings (like a flag to
let the user choose to *always* delete pages from the site for which the source
Markdown file has been deleted, or to always ask, etc.)

One final icing-on-the-cake feature I'd like to implement when all is said and
done is some basic search engine optimization: allow users to specify Facebook
Open Graph information, Twitter card information, and Google+ authorship data
from the configuration file. (They could of course add this into templates
manually, but that's a pain.) I'll probably figure out a way to make than an
extension that users can leave disabled entirely, but can turn on if they wish.

All of these pieces are still far out on the horizon, though; I largely put
them here (a) to help me think through them and (b) to give myself a target at
which to aim. That is simply how I roll.

[history]: https://bitbucket.org/chriskrycho/step-stool/commits/all?search=date('%3C2013-06-30')

[^1]: I actually only realized I needed those tonight... and, with my brain
chugging along happily in the background while I was writing this up, I've
already devised what I hope will be a fairly decent solution for it.
