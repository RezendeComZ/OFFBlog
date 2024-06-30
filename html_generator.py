def html_tag(content):
  return "<!doctype html>\n<html lang=\"en-US\">\n" + content + "\n</html>"

def custom_tag(tag_name, content):
  return "<" + tag_name + ">\n" + content + "\n</" + tag_name + ">"

def nav_tag():
  return custom_tag("nav", "Home | By subject | By Date")

def article_tag(content):
  return "<h1>Blablabla</h2>\n<p>blebleble</p>\n" + "<p>" + content + "</p>"

def body_tag(content):
  header = custom_tag("header", "alou")
  nav = nav_tag()
  article = article_tag(content)
  body_content = header + "\n" + nav + "\n" + article
  return custom_tag("body", body_content)

def md_to_html(content):
  head_content = "<title>" + "some title" + "</title>"
  head = custom_tag("head", head_content)
  body = body_tag(content)
  body_content = head + body
  return html_tag(body_content)

# print(md_to_html("Conteúdo do artigo aqui"))