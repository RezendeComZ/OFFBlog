import os, util

code_block = ".code_block {font-family: monospace; background: grey}"

def css_content():
  css_file = open(os.path.join(util.PUBLIC_DIRECTORY, "../styles.css"), "w")
  css_file.write(code_block)
