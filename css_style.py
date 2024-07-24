import os, const, configs

body = "body {background-color: " + configs.BACKGROUND_COLOR + "; margin-right: 150px; margin-left: 150px}"
blog_title = "#blog_title {background-color: none; color: " + configs.TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
navigation_bar = "#navigation_bar {display: flex; align-items: center}"
article_title = "#article_title {color: " + configs.ARTICLE_TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
tag = ".tag {color: black; background-color: rgb(255,255,0, 0.5);border-radius: 25px; padding: 5px}"
p = "p {color: " + configs.TEXT_COLOR + "; font-family: monospace; font-size: 150%}"
code_block = ".code_block {font-family: monospace; background: #343942; border-radius: 25px; padding: 5px 15px 5px;}"
date = ".date {color: " + configs.DATE_COLOR + "}"
postline = ".postline {display: flex; align-items: center; column-gap: 20px;}"

css_tags = body + blog_title + navigation_bar + article_title + p + date + code_block + tag + postline

def css_content():
  css_file = open(os.path.join(const.PUBLIC_DIRECTORY, "../public/styles.css"), "w")
  css_file.write(css_tags)
