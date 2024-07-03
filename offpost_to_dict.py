def title(file):
  # Get the first line of the file and remove the number sign (#).
  return file.split("\n")[0][2:]

def file_name(title, index):
  # TODO, use the index number ONLY to order posts on other pages while keeping the file name clean without including the number
  return str(index) + "-" + title.replace(" ", "-").replace(",", "").replace(".", "").lower()

def body(file, date):
  lines = file.split('\n')
  return "<p>" + date + "</p>" + '\n'.join(lines[1:])

def html_structure(file, file_number, date):
  title_name = title(file)
  return {"title": title_name,
          "file_name": file_name(title_name, file_number),
          "body": body(file, date)}