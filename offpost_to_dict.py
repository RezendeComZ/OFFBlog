def title(file):
  # Get the first line of the file and remove the number sign (#).
  return file.split("\n")[0][2:]

def file_name(title):
    return title.translate(str.maketrans(" ,.!_", "-----", ".,!"))

def body(file, date):
  lines = file.split('\n')
  return "<p class=date>" + date + "</p>" + '\n'.join(lines[1:])

def html_structure(file, title, date):
  return {"title": title,
          "file_name": file_name(title),
          "body": body(file, date)}