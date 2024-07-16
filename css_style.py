import os, util, configs

body = "body {background-color: " + configs.BACKGROUND_COLOR + "}"
blog_title = "#blog_title {color: " + configs.TITLE_COLOR + "; font-family: monospace}"
nav = "nav {color:" + configs.NAV_COLOR + "; font-family: monospace; margin-left: 20px}"
article_title = "#article_title {color: " + configs.ARTICLE_TITLE_COLOR + "; font-family: monospace}"
p = "p {color: " + configs.TEXT_COLOR + "; font-family: monospace}"
code_block = ".code_block {font-family: monospace; background: #343942}"
navigation_bar = "#navigation_bar {display: flex; align-items: center}"



css_tags = body + blog_title + navigation_bar + nav + article_title + p + code_block

def css_content():
  css_file = open(os.path.join(util.PUBLIC_DIRECTORY, "../styles.css"), "w")
  css_file.write(css_tags)
