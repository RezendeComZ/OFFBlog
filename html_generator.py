from configs import configs

code_block_start = True

code_block_div_start = "<div class=code_block>"

div_end = "</div>"

CSS_TAG = "<link rel=\"stylesheet\" href=\"/styles.css\">"

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

def custom_tag(tag_name, content):
  return "<" + tag_name + ">" + content + "</" + tag_name + ">"

def nav_tag():
  return custom_tag("nav", "Home | By subject | By Date")

def article_tag(content, title):
  paragraphs = content.split("\n")

  paragraphs_tags = map(lambda paragraph: "<p>" + paragraph + "</p>", paragraphs)
  paragraphs_html = "".join(paragraphs_tags)
  formatted_text = text_formatter(paragraphs_html)
  return "<article><h1>" + title + "</h1>" + formatted_text + "</article>"

def body_tag(content, title):
  header = custom_tag("header", configs["blog_title"])
  nav = nav_tag()
  article = article_tag(content, title)
  body_content = header + nav + article
  return custom_tag("body", body_content)

def head(article_title):
  title = "<title>" + configs["html_blog_title"] + " - " + article_title + "</title>"
  head_content = title + CSS_TAG
  return custom_tag("head", head_content)

def generate_html(article_title, body_content):
  body = body_tag(body_content, article_title)
  body_content = head(article_title) + body
  return html_tag(body_content)