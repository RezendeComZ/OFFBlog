import os, shutil, html_generator, offpost_to_dict, css_style, const, time

def post_location(location, name):
  return os.path.join(location, name + ".html")

def write_html_file(location, html_content):
  file = open(post_location(location, html_content["file_name"]), "w")
  file.write(html_generator.generate_html(html_content["title"], html_content["body"]))
  file.close()

def create_PUBLIC_DIRECTORY():
  if os.path.exists(const.PUBLIC_DIRECTORY):
    print("The 'public' directory already exists.")
    return True
  else:
    try:
      os.makedirs(const.PUBLIC_DIRECTORY)
      return True
    except Exception as e:
      print(f"Something went wrong while creating the 'public' directory {e}")

def erase_PUBLIC_DIRECTORY():
  if os.path.exists(const.PUBLIC_DIRECTORY):
    try:
      shutil.rmtree(const.PUBLIC_DIRECTORY)
      return True
    except Exception as e:
      print(f"Something went wrong while deleting the 'public' directory: {e}")
  else: 
    # The 'public' directory does not exist and cannot be deleted.
    return True

def initial_public_directory_setup():
  return erase_PUBLIC_DIRECTORY() and create_PUBLIC_DIRECTORY()

def make_html(location, destination, file_name):
  date_numbers = destination.split("/")[-3:][::-1]
  date = "/".join(date_numbers)
  file = open(location + "/" + file_name, "r").read()
  html_content = offpost_to_dict.html_structure(file, offpost_to_dict.title(file), date)
  write_html_file(destination, html_content)

def replicate_directory_structure(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        # Relative path from the source directory.
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)
        os.makedirs(target_path, exist_ok=True) # Create the directory in the target directory.

        for file_name in files:
          make_html(root, target_path, file_name)

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
  post_line_text = html_generator.paragraph_tag("<span class=date>" + date + "</span> - " + title)
  post_line_url = "<a href=\"" + post_url + "\">" + post_line_text + "</a>"

  return post_line_url

def generate_index_content(source_dir):
  files_list = []
  for root, dirs, files in os.walk(source_dir):
      for file in files:
          files_list.append(os.path.join(root, file))
  posts_tags = map(generate_post_index_tag, files_list)

  return reversed(list(posts_tags))

def create_index(source_dir):
    index_content = "".join(generate_index_content(source_dir))
    file = open(post_location(const.PUBLIC_DIRECTORY, "index"), "w")
    file.write(html_generator.generate_html("Latest posts", index_content))
    file.close()  

def run():
  if initial_public_directory_setup():
    ts_start = time.time()
    replicate_directory_structure(const.BLOG_POSTS_DIRECTORY, const.PUBLIC_DIRECTORY)
    css_style.css_content()
    create_index(const.BLOG_POSTS_DIRECTORY)
    ts_end = time.time()
    print("Finished successfully in " + str('%.4f'%(ts_end - ts_start)) + "s.")
  else:
    print("Error while generating the initial setup for the 'public' directory.")

run()