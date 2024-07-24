import os
from dotenv import load_dotenv 
load_dotenv() 

ARTICLE_TITLE_COLOR = os.getenv("ARTICLE_TITLE_COLOR")
TITLE = os.getenv("TITLE")
TITLE_COLOR = os.getenv("TITLE_COLOR")
TAG_COLOR = os.getenv("TAG_COLOR")
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")
TEXT_COLOR = os.getenv("TEXT_COLOR")
DATE_COLOR = os.getenv("DATE_COLOR")
BLOG_URL = os.getenv("BLOG_URL")
