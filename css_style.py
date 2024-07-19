import os, util, configs

body = "body {background-color: " + configs.BACKGROUND_COLOR + "; margin-right: 150px; margin-left: 150px}"
blog_title = "#blog_title {color: " + configs.TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
navigation_bar = "#navigation_bar {display: flex; align-items: center}"
nav = "nav {color:" + configs.NAV_COLOR + "; font-family: monospace; margin-left: 20px; font-size: 125%}"
article_title = "#article_title {color: " + configs.ARTICLE_TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
p = "p {color: " + configs.TEXT_COLOR + "; font-family: monospace; font-size: 150%}"
code_block = ".code_block {font-family: monospace; background: #343942; border-radius: 25px; padding: 5px 15px 5px;}"

css_tags = body + blog_title + navigation_bar + nav + article_title + p + code_block

def css_content():
  css_file = open(os.path.join(util.PUBLIC_DIRECTORY, "../styles.css"), "w")
  css_file.write(css_tags)
