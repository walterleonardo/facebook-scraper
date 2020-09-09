from facebook_scraper import get_posts

for post in get_posts("nintendo", pages=1, comments = True):
    print(post)