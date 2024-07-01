def html_tag(content):
  return "<!doctype html><html lang=\"en-US\">" + content + "</html>"

def custom_tag(tag_name, content):
  return "<" + tag_name + ">" + content + "</" + tag_name + ">"

def nav_tag():
  return custom_tag("nav", "Home | By subject | By Date")

def article_tag(content):
  return "<h1>Blablabla</h2><p>blebleble</p>" + "<p>" + content + "</p>"

def body_tag(content):
  header = custom_tag("header", "alou")
  nav = nav_tag()
  article = article_tag(content)
  body_content = header + nav + article
  return custom_tag("body", body_content)

def generate_html(title, body_content):
  head_content = "<title>" + title + "</title>"
  head = custom_tag("head", head_content)
  body = body_tag(body_content)
  body_content = head + body
  return html_tag(body_content)