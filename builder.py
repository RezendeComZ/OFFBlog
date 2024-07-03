import os, shutil, html_generator, offpost_to_dict

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'public')
BLOG_POSTS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'blog-posts')

def post_location(location, name):
  return os.path.join(location, name + ".html")

def write_html_file(location, html_content):
  file = open(post_location(location, html_content["file_name"]), "w")
  file.write(html_generator.generate_html(html_content["title"], html_content["body"]))
  file.close()

def create_PUBLIC_DIRECTORY():
  if os.path.exists(PUBLIC_DIRECTORY):
    print("The 'public' directory already exists.")
    return True
  else:
    try:
      os.makedirs(PUBLIC_DIRECTORY)
      return True
    except Exception as e:
      print(f"Something went wrong while creating the 'public' directory {e}")

def erase_PUBLIC_DIRECTORY():
  if os.path.exists(PUBLIC_DIRECTORY):
    try:
      shutil.rmtree(PUBLIC_DIRECTORY)
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

        # Calculate the relative path from the source directory.
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)


        os.makedirs(target_path, exist_ok=True) # Create the directory in the target directory.

        file_number = 1
        for file_name in files:
          make_html(root, target_path, file_name, file_number)
          file_number += 1

def run():
  if initial_public_directory_setup():
    replicate_directory_structure(BLOG_POSTS_DIRECTORY, PUBLIC_DIRECTORY)
    print("Finished successfully.")
  else:
    print("Error while generating the initial setup for the 'public' directory.")

run()