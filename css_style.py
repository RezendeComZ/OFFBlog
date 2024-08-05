import os, const, configs

body = "body {background-color: " + configs.BACKGROUND_COLOR + "; margin-right: 25%; margin-left: 25%}"
blog_title = "#blog_title {background-color: none; color: " + configs.TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
navigation_bar = "#navigation_bar {display: flex; align-items: center}"
article_title = "#article_title {color: " + configs.ARTICLE_TITLE_COLOR + "; font-family: monospace; font-size: 220%}"
tag = ".tag {color: black; background-color: rgb(255,255,0, 0.5);border-radius: 25px; padding: 5px}"
p = "p {color: " + configs.TEXT_COLOR + "; font-family: monospace; font-size: 150%}"
code_block = ".code_block {font-family: monospace; background: #343942; border-radius: 25px; padding: 5px 15px 5px;}"
date = ".date {color: " + configs.DATE_COLOR + "}"
postline = ".postline {display: flex; align-items: center; margin-top: 15px; column-gap: 15px}"
image = ".image {color: " + configs.TEXT_COLOR + "; font-size: 130%; width: 55%; display: flex; flex-direction: column; justify-content: center;font-family: monospace; background: #343942; border-radius: 25px; padding: 15px 15px 5px; text-align: center;}"

css_tags = body + blog_title + navigation_bar + article_title + p + date + code_block + tag + postline + image

def css_content():
  css_file = open(os.path.join(const.PUBLIC_DIRECTORY, "../public/styles.css"), "w")
  css_file.write(css_tags)
