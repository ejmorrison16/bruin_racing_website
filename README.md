# Set up theme and build static files

Install node.js

    brew install node

Or use ASDF, using the version in `.tool-versions`

    asdf install

    # export PATH=$PATH:$HOME/.asdf/installs/nodejs/8.11.3/bin
    export PATH=$PATH:$HOME/.asdf/installs/nodejs/8.11.3/.npm/bin

Install gulp command

    npm install -g gulp

Install theme dependencies.
From the `themes/spacial` directory, run:

    npm install

Build the theme output files to the `static` directory.
From the `themes/spacial` directory, run:

    gulp

If you make changes to the scss files, run gulp to regenerate the minified css and js files.
You can run this command in the `themes/spacial` directory, and gulp will automatically regenerate
the files when you make changes.

    gulp watch

# Set up pelican

Create a virtualenv for the Python deps and install into it.

For Python 2.x

    virtualenv ~/.virtualenvs/bruinracing
    source ~/.virtualenvs/bruinracing/bin/activate
    pip install -r requirements.txt

or for Python 3.x

    python3 -m venv ~/.virtualenvs/blog
    pip3 install -r requirements.txt

# Generate content

Use the virtualenv

    source ~/.virtualenvs/blog/bin/activate

Generate html to run locally

    make html

Run a local web server to preview the site. This will automatically
compile the files when they change.

    make devserver
    open http://localhost:8000/
    make stopserver

Live reload http://tech.agilitynerd.com/livereload-with-pelican.html
https://merlijn.vandeen.nl/2015/pelican-livereload.html

    pip install livereload

    scripts/pelican-livereload.py

# Deploy

## Set up AWS

Create a file `~/.aws/credentials` with your AWS access key:

    [bruinracing]
    aws_access_key_id = XXX
    aws_secret_access_key = YYY

Update the `AWS_PROFILE` and `S3_BUCKET` settings in `Makefile` if necessary

    make publish
    make s3_upload

# Authoring

Syntax highlighing http://pygments.org/docs/lexers/

    :::identifier
    your code goes here

Open links in a separate window

    [link](url){:target="_blank"}

If you change the URL, you can make an alias from the old URL to to the new one using the
https://github.com/Nitron/pelican-alias plugin:

    Alias: /blog/old/

# Docs

Home page: https://blog.getpelican.com/
Docs: http://docs.getpelican.com/en/stable/settings.html
Tutorials: https://github.com/getpelican/pelican/wiki/Tutorials
Themes: http://docs.getpelican.com/en/3.7.1/themes.html

Useful vars: https://stackoverflow.com/questions/40923844/variable-for-url-of-current-page-in-pelican-templates

# Plugins

    git clone --recursive https://github.com/getpelican/pelican-plugins

copy to plugins dir

http://hyperpolyglot.org/lightweight-markup
https://dev.twitter.com/cards/types/summary


# Syntax highlighting

http://docs.getpelican.com/en/3.6.3/faq.html#i-m-creating-my-own-theme-how-do-i-use-pygments-for-syntax-highlighting

https://github.com/honza/vim2pygments

/Users/jake/.asdf/installs/nodejs/8.2.1/.npm/bin/gulp


# Designers

Follow the instructions in the "Set up theme and build static files" and "Set
up pelican" sections.  The instructions in "Generate content" are probably
correct, but I am not sure about the live-reload stuff, it might just be notes.

If things are working, then this should work:

    make devserver
    open http://localhost:8000/

Then you should be able to edit the style in `themes/spacial/scss/cogini.scss`. 
If "gulp watch" is working, it will generate the css files, and if the
devserver is working, it will recompile the output files and you can reload
port 8000 and see them.
