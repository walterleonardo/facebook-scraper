from facebook_scraper import get_posts

for post in get_posts("nintendo", pages=2, comments = True, credentials=['walii@walii.es','jodete2k']):
    print(post)