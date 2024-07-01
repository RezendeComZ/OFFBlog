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
    print("'Public' directory already exists.")
  else:
    try:
      os.makedirs(PUBLIC_DIRECTORY)
    except Exception as e:
      print(f"Something went wrong while creating 'Public' directory {e}")

def erase_PUBLIC_DIRECTORY():
  if os.path.exists(PUBLIC_DIRECTORY):
    try:
      shutil.rmtree(PUBLIC_DIRECTORY)
    except Exception as e:
      print(f"Something went wrong while deleting 'Public' directory: {e}")
  else: 
    print("'Public' directory does not exist to be deleted.")

def initial_public_directory_setup():
  # TODO, Return an error if necessary
  erase_PUBLIC_DIRECTORY()
  create_PUBLIC_DIRECTORY()

def make_html(location, destination, file_name, file_number):
  file = open(location + "/" + file_name, "r")
  html_content = offpost_to_dict.html_structure(file.read(), file_number)
  write_html_file(destination, html_content)

def replicate_directory_structure(source_dir, target_dir):
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # TODO, Generate a index file for the year/month

        # Calculate the relative path from the source directory
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)

        os.makedirs(target_path, exist_ok=True) # Create the directory in the target directory

        file_number = 1
        for nome_arquivo in files:
          make_html(root, target_path, nome_arquivo, file_number)
          file_number += 1

def run():
  initial_public_directory_setup()
  replicate_directory_structure(BLOG_POSTS_DIRECTORY, PUBLIC_DIRECTORY)

run()