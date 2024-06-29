import os, shutil

current_directory = os.path.dirname(os.path.abspath(__file__))
public_diretory = os.path.join(current_directory, 'public')

def post_location(name):
  return os.path.join(public_diretory, name + ".html")

def write_html_file(content):
  file = open(post_location(content), "w")
  file.write("<h1>Something</h1>")
  file.close()

def create_public_diretory():
  if os.path.exists(public_diretory):
    print("'Public' directory already exists.")
  else:
    try:
      os.makedirs(public_diretory)
    except Exception as e:
      print(f"Something went wrong while creating 'Public' directory" {e})

def erase_public_diretory():
  if os.path.exists(public_diretory):
    try:
      shutil.rmtree(public_diretory)
    except Exception as e:
      print(f"Something went wrong while deleting 'Public' directory: {e}")
  else: 
    print("'Public' directory does not exist to be deleted.")

def initial_public_directory_setup():

def main():
  erase_public_diretory()
  create_public_diretory()


main()