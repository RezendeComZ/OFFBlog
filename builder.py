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

def make_html(location, destination, file_name, file_number):
  date_numbers = destination.split("/")[-3:][::-1]
  date = "/".join(date_numbers)
  file = open(location + "/" + file_name, "r")
  html_content = offpost_to_dict.html_structure(file.read(), file_number, date)
  write_html_file(destination, html_content)

def replicate_directory_structure(source_dir, target_dir):
    # Walk through the source directory.
    for root, dirs, files in os.walk(source_dir):
        # TODO, Generate a index file for the year/month.

        # Relative path from the source directory.
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)

        os.makedirs(target_path, exist_ok=True) # Create the directory in the target directory.

        file_number = 1
        for file_name in files:
          make_html(root, target_path, file_name, file_number)
          file_number += 1

def run():
  if initial_public_directory_setup():
    ts_start = time.time()
    replicate_directory_structure(const.BLOG_POSTS_DIRECTORY, const.PUBLIC_DIRECTORY)
    css_style.css_content()
    # create_index(const.BLOG_POSTS_DIRECTORY, const.PUBLIC_DIRECTORY)
    ts_end = time.time()
    print("Finished successfully in " + str('%.4f'%(ts_end - ts_start)) + "s.")
  else:
    print("Error while generating the initial setup for the 'public' directory.")

run()