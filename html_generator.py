import configs, const, util

tag_start_state = True

def div_start(html_class):
  return "<div class=" + html_class + ">"

div_end = "</div>"

def title(article_title):
  return "<title>" + article_title + " - " + configs.TITLE + "</title>"

def tag_marker(tag_start):
  global tag_start_state
  if tag_start_state:
    tag_start_state = False
    return tag_start
  else:
    tag_start_state = True
    return div_end

def tag_formater(paragraphs_html, div_start, marker):
  global tag_start
  tag_start = True
  code_blocks = paragraphs_html.split(marker)
  code_block_tags = "".join(map(lambda p: p + tag_marker(div_start), code_blocks))
  return code_block_tags[slice(-len(div_start))] # Remove extra code_block div, not my best code

def text_formatter(paragraphs_html):
  code_block = tag_formater(paragraphs_html, div_start("code_block"), "<p>```</p>")
  return code_block

def html_tag(content):
  return "<!doctype html><html lang=\"en-US\">" + content + "</html>"

def paragraph_tag(text):
  return "<p>" + text + "</p>\n"

def article_tag(content, title):
  paragraphs = content.split("\n")
  paragraphs_tags = map(paragraph_tag, paragraphs)
  paragraphs_html = "".join(paragraphs_tags)
  formatted_text = text_formatter(paragraphs_html)
  return "<article><h1 id=article_title>" + title + "</h1>" + formatted_text + "</article>"

def navigation_bar():
  header = util.custom_tag("header", None, "<a href=" + configs.BLOG_URL + "><h1 id=blog_title>" + configs.TITLE + "</h1></a>")
  return util.custom_tag("div", "id=navigation_bar", header)

def body_tag(content, title):
  article = article_tag(content, title)
  body_content = navigation_bar() + article
  return util.custom_tag("body", None, body_content)

def head(article_title):
  head_content = title(article_title) + const.CSS_TAG
  return util.custom_tag("head", None, head_content)

def generate_html(article_title, body_content):
  body = body_tag(body_content, article_title)
  body_content = head(article_title) + body
  return html_tag(body_content)