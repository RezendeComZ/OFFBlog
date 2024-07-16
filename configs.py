import os
from dotenv import load_dotenv 
load_dotenv() 

ARTICLE_TITLE_COLOR = os.getenv("ARTICLE_TITLE_COLOR")
TITLE = os.getenv("TITLE")
TITLE_COLOR = os.getenv("TITLE_COLOR")
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")
NAV_COLOR = os.getenv("NAV_COLOR")
TEXT_COLOR = os.getenv("TEXT_COLOR")
