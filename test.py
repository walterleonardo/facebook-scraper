from facebook_scraper import get_posts
import json
import credentials

for post in get_posts("nintendo", pages=1, comments = True, credentials={credentials.username, credentials.password}):
    print((post))