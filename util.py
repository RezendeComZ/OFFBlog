import os

def custom_tag(tag_name, attribute, content):
  return "<" + tag_name + " " + (attribute or "") +">" + content + "</" + tag_name + ">"

def post_location(location, name):
  return os.path.join(location, name + ".html")