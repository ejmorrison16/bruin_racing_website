# Bruin Racing website

This site uses a static site generator, [Pelican](http://docs.getpelican.com/).
Pelican builds static HTML pages using templates, so it's like HTML but we don't
have to repeat things like CSS includes, menus and footer in every file.

The templates are in `theme/templates`, and the content is in `content/pages`.
Pelican allows pages to be created in Markdown (like this file) or HTML.
Markdown is nice for things like blog pages, but most of the pages on this
site are heavily designed, so we use HTML.

To create a new page, put an HTML file in `content/pages` like this:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Bruin Racing — Baja</title>
    <meta name="slug" content="baja" />
    <meta name="template" content="page-baja" />
  </head>
  <body>
  <p>Your content here</p>
  </body>
</html>
```

Run `make html` and Pelican will generate the output file in
`output/baja/index.html`. The template adds in the CSS and JS references
for styling and dynamic functionality. If a page needs to have
special CSS or JS, make a new template which extends the base template,
same as the Baja page does, e.g. `theme/templates/page-baja.html`.
Add CSS to the `extra_css` section, JavaScript libraries to the
`extra_vendor_js` section, or JavaScript initialization/configuration code to
the `js_plugins_init` section.  Then reference your template in the HTML:

```html
<meta name="template" content="page-foo" />
```

You can then link to your new page:

```html
<a href="/foo/">Foo</a>
```

# Installation

Before running commands, you need to install the Pelican libraries and set up
your environment.

# Set up pelican

Create a Python virtualenv and install the dependencies into it.

For Python 2.x:

```shell
virtualenv ~/.virtualenvs/bruinracing
source ~/.virtualenvs/bruinracing/bin/activate
pip install -r requirements.txt
```

or for Python 3.x:

```shell
python3 -m venv ~/.virtualenvs/bruinracing
source ~/.virtualenvs/bruinracing/bin/activate
pip3 install -r requirements.txt
```

# Generate content

Every time you run Pelican commands, you have to "activate" the virtualenv:

```shell
source ~/.virtualenvs/bruinracing/bin/activate
```

Generate html to run locally:

    make html

Run a local web server to preview the site. This will automatically
compile the files when they change.

    make devserver
    open http://localhost:8000/
    make stopserver

# Deploy

We deploy the site to an Amazon S3 bucket, so you need to have
an AWS account with permissions to write content there.

## Set up AWS

Create a file `~/.aws/credentials` with your AWS access key:

    [bruinracing]
    aws_access_key_id = XXX
    aws_secret_access_key = YYY

Update the `AWS_PROFILE` and `S3_BUCKET` settings in `Makefile` if necessary

Generate the final HTML and sync the data with the S3 bucket:

```shell
make s3_upload
```

# Authoring

If you change the URL, you can make an alias from the old URL to to the new one using the
https://github.com/Nitron/pelican-alias plugin:

```html
<meta name="alias" content="/site/index/" />
```
or, for markdown:

    Alias: /blog/old/

# Docs

* Home page: https://blog.getpelican.com/
* Docs: http://docs.getpelican.com/en/stable/settings.html
* Tutorials: https://github.com/getpelican/pelican/wiki/Tutorials
* Themes: http://docs.getpelican.com/en/stable/themes.html
* Useful vars: https://stackoverflow.com/questions/40923844/variable-for-url-of-current-page-in-pelican-templates

## Plugins

```shell
git clone --recursive https://github.com/getpelican/pelican-plugins
```

Copy them to the plugins dir.
