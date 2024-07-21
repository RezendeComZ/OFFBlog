import os, configs

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CSS_TAG = "<link rel=\"stylesheet\" href=\"" + configs.BLOG_URL + "/styles.css\">"
PUBLIC_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'public')
BLOG_POSTS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, 'blog-posts')