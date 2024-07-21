import configs, const

code_block_start = True

code_block_div_start = "<div class=code_block>"

div_end = "</div>"

def title(article_title):
  return "<title>" + article_title + " - " + configs.TITLE + "</title>"

def code_block_tag():
  global code_block_start
  if code_block_start:
    code_block_start = False
    return code_block_div_start
  else:
    code_block_start = True
    return div_end

def code_block_formater(paragraphs_html):
  global code_block_start
  code_block_start = True
  code_blocks = paragraphs_html.split("<p>```</p>")
  code_block_tags = "".join(map(lambda p: p + code_block_tag(), code_blocks))
  return code_block_tags[slice(-len(code_block_div_start))] # Remove extra code_block div, not my best code

def text_formatter(paragraphs_html):
  return code_block_formater(paragraphs_html)

def html_tag(content):
  return "<!doctype html><html lang=\"en-US\">" + content + "</html>"

def custom_tag(tag_name, attribute, content):
  return "<" + tag_name + " " + (attribute or "") +">" + content + "</" + tag_name + ">"

def paragraph_tag(text):
  return "<p>" + text + "</p>"

def article_tag(content, title):
  paragraphs = content.split("\n")
  paragraphs_tags = map(paragraph_tag, paragraphs)
  paragraphs_html = "".join(paragraphs_tags)
  formatted_text = text_formatter(paragraphs_html)
  return "<article><h1 id=article_title>" + title + "</h1>" + formatted_text + "</article>"

def navigation_bar():
  header = custom_tag("header", None, "<h1 id=blog_title>"+ configs.TITLE + "</h1>")
  return custom_tag("div", "id=navigation_bar", header)

def body_tag(content, title):
  article = article_tag(content, title)
  body_content = navigation_bar() + article
  return custom_tag("body", None, body_content)

def head(article_title):
  head_content = title(article_title) + const.CSS_TAG
  return custom_tag("head", None, head_content)

def generate_html(article_title, body_content):
  body = body_tag(body_content, article_title)
  body_content = head(article_title) + body
  return html_tag(body_content)