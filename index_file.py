import os, offpost_to_dict, html_generator, const, util
from functools import partial

def post_tags(source_file):
   source_file_split = source_file.split("|")[1:]
   if source_file_split:
    source_file_split[-1] = source_file_split[-1].replace(".offpost", "")
    return source_file_split
   else:
    return []

def post_tags_html(source_file):
   tags = post_tags(source_file)
   tags_html = map(partial(util.custom_tag ,"span", "class=tag"), tags)
   return "".join(tags_html)

def generate_post_index_tag(source_file):
  file = open(source_file, "r")
  file_content = file.read()
  file.close()
  
  title = offpost_to_dict.title(file_content)
  file_name = offpost_to_dict.file_name(title)
  source_file_split = source_file.split("/")
  post_url_split = source_file_split[-4:-1]
  post_url = "/".join(post_url_split) + "/" + file_name + ".html"
  date_array = post_url_split
  date = "-".join(date_array)
  post_line_text = title
  link = "<a href=" + post_url + ">" + post_line_text + "</a>"
  date_span = util.custom_tag("span", "class=date", date)
  post_line_url = util.custom_tag("span", "class=postline", date_span + link + post_tags_html(source_file))

  return post_line_url 

def generate_index_content(source_dir):
  files_list = []
  for root, dirs, files in os.walk(source_dir):
      for file in files:
          files_list.append(os.path.join(root, file))
  posts_tags = map(generate_post_index_tag, files_list)

  return reversed(list(posts_tags))

def create_index(source_dir):
    index_content = "\n" + "".join(generate_index_content(source_dir))
    file = open(util.post_location(const.PUBLIC_DIRECTORY, "index"), "w")
    file.write(html_generator.generate_html("Latest posts", index_content))
    file.close()  