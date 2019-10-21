# Bruin Racing website

This site uses a static site generator, [Pelican](http://docs.getpelican.com/).
Pelican builds static HTML pages using templates, so it's like HTML but we don't
have to repeat things like CSS includes, menus and footer in every file.

# Installation

Before running commands, you need to install the Pelican libraries and set up
your environment.

You can do this by running:

    make install

That does the following:

# Set up pelican

Create a Python virtualenv and install the dependencies into it.

For Python 3.x:

```shell
python3 -m venv ~/.virtualenvs/bruinracing
source ~/.virtualenvs/bruinracing/bin/activate
pip install -r requirements.txt
```

Or for Python 2.x:

```shell
virtualenv ~/.virtualenvs/bruinracing
source ~/.virtualenvs/bruinracing/bin/activate
pip install -r requirements.txt
```

This project includes a `.tool-versions` file which
manages the python version via [ASDF](https://asdf-vm.com/).
After installing, you may need to run:

```shell
asdf reshim python
```

to make the `pelican` command available.

# Authoring

Content is in `content/pages` or `content/blog` and templates are in
`theme/templates`.

Blog “articles” are chronological content, associated with a date.
Pages are used for content that does not change very often (e.g., “About Us” or
“Contact” pages).

Pelican allows content to be created in Markdown (like this file) or HTML.
Markdown is nice for things like blog pages, but most of the pages on this
site are heavily designed, so we use HTML.

To create a new blog page, add `topic.md` to it to `content/blog`.

To create a new page, put a `baja.html` HTML file in `content/pages` like this:

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

Run `make html` and Pelican will generate the output file in `output/baja/index.html`.
The template adds in the CSS and JS references for styling and dynamic functionality.

You can customize the output name used in the URL by setting the slug in the `head`:

```html
<meta name="slug" content="foobar" />
```

You can customize the page template the same way:

```html
<meta name="template" content="page-foo" />
```

If a page needs to have special CSS or JS, make a new template which extends
the base template, same as the Baja page does, e.g. `theme/templates/page-baja.html`.

Add CSS to the `extra_css` section, JavaScript libraries to the
`extra_vendor_js` section, or JavaScript initialization/configuration code to
the `js_plugins_init` section.

Then reference your template in the HTML:

```html
<meta name="template" content="page-foo" />
```

You can then link to your new page:

```html
<a href="/foo/">Foo</a>
```

Special Markdown tags:

`Status: draft` keeps a post private during development.

`Summary:` Lets you specify the summary when the first lines of your post are not appropriate.

`Slug:` my-special-slug

Make links to local content like this:

    [The title]({filename}/files/foo.pdf)

# Generate content

Before you run Pelican commands, you have to "activate" the virtualenv to make
the libraries available to Python:

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

Live reload http://tech.agilitynerd.com/livereload-with-pelican.html
https://merlijn.vandeen.nl/2015/pelican-livereload.html

```shell
pip install livereload

scripts/pelican-livereload.py
```

# Deploy

We deploy the site to an Amazon S3 bucket, so you need to have an AWS account
with permissions to write content there.

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

Serve files from CloudFront Content Deliver Network (CDN):

    make cloudfront_upload

## Setting up AWS

See general instructions in `terraform/README.md`.

    cd `terraform/website`

    export ENV=prod
    source set_env.sh

    terragrunt plan --terragrunt-working-dir "$ENV/cloudfront-public-web"
    terragrunt apply --terragrunt-working-dir "$ENV/cloudfront-public-web"

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

## Aliases

If you change the URL, you can make an alias from the old URL to to the new one
using the https://github.com/Nitron/pelican-alias plugin:

```html
<meta name="alias" content="/site/index/" />
```
or, for markdown:

    Alias: /blog/old/

## HELP!

If this is all a huge mystery to you, contact Jake Morrison,
email jake@cogini.com, jake_morrison on Skype

## TL;DR

    make install
    source ~/.virtualenvs/bruinracing/bin/activate
    make cloudfront_upload
