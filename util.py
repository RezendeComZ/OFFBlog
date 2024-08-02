import os

def custom_tag(tag_name, attribute, content):
  return "<" + tag_name + " " + (attribute or "") +">" + content + "</" + tag_name + ">"

def post_location(location, name):
  return os.path.join(location, name + ".html")

def is_offpost_file(file_name):
  return file_name.split(".")[-1] == "offpost"