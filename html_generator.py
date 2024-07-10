code_block_start = True

def code_block_tag():
  global code_block_start
  if code_block_start:
    code_block_start = False
    return "<span class=code_block style=\"color:red; font-family: monospace;\">"
  else:
    code_block_start = True
    return "</span>" 

def code_block_formater(paragraphs_html):
  code_blocks = paragraphs_html.split("<p>```</p>")
  return "".join(map(lambda p: p + code_block_tag(), code_blocks))

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
  header = custom_tag("header", "alou")
  nav = nav_tag()
  article = article_tag(content, title)
  body_content = header + nav + article
  return custom_tag("body", body_content)

def generate_html(title, body_content):
  head_content = "<title>" + title + "</title>"
  head = custom_tag("head", head_content)
  body = body_tag(body_content, title)
  body_content = head + body
  return html_tag(body_content)