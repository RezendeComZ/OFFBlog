# OFFBlog
An out of fashion blog.

This is a simple static blog with simple principles: Write, build, commit, push.

[Click here to acess the publish pages](https://rezendecomz.github.io/OFFBlog/)

## How to make a post?

Use the following directory struture after the *blog-posts*'s directory:

```
year/month/day/file.offpost
```
e.g:
```
2024/07/21/finally_a_decent_readme_file.offpost
```
The *.offpost* files have very basic Markdown support, currently limited to line breaks and code blocks, but supports HTML tags.
The structure should be as follows:

```
# Title

Content
```

## How to generate the HTML files

Simply run builder.py.

## Environment Variables

The .env file allows you to edit some basic CSS and HTML properties.

## TODOs

- A way to execute *builder.py*, commit and push.
- Tags filter directly in JavaScript
- Better Markdown support.
- A better README.md file 👀