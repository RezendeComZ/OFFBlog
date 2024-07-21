import os

CSS_TAG = "<link rel=\"stylesheet\" href=\"/styles.css\">"
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'public')
BLOG_POSTS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'blog-posts')