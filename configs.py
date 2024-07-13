import os
from dotenv import load_dotenv 
load_dotenv() 
 
BLOG_TITLE = os.getenv("BLOG_TITLE")
HTML_BLOG_TITLE = os.getenv("HTML_BLOG_TITLE")

configs = {"blog_title": BLOG_TITLE,
           "html_blog_title": HTML_BLOG_TITLE}