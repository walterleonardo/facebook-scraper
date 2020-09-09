import codecs
import re
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlparse, urlunparse

from html2text import html2text as _html2text
from requests_html import DEFAULT_URL, Element, PyQuery


def find_and_search(node, selector, pattern, cast=str):
    container = node.find(selector, first=True)
    match = container and pattern.search(container.html)
    return match and cast(match.groups()[0])


def parse_int(value: str) -> int:
    return int(''.join(filter(lambda c: c.isdigit(), value)))


def decode_css_url(url: str) -> str:
    url = re.sub(r'\\(..) ', r'\\x\g<1>', url)
    url, _ = codecs.unicode_escape_decode(url)
    return url


def filter_query_params(url, whitelist=None, blacklist=None) -> str:
    def is_valid_param(param):
        if whitelist is not None:
            return param in whitelist
        if blacklist is not None:
            return param not in blacklist
        return True  # Do nothing

    parsed_url = urlparse(url)
    query_params = parse_qsl(parsed_url.query)
    query_string = urlencode([(k, v) for k, v in query_params if is_valid_param(k)])
    return urlunparse(parsed_url._replace(query=query_string))


def make_html_element(html: str, url=DEFAULT_URL) -> Element:
    pq_element = PyQuery(html)[0]  # PyQuery is a list, so we take the first element
    return Element(element=pq_element, url=url)


def html2text(html: str) -> str:
    return _html2text(html)



def request_comments(post_url: str, post_id: str) -> list:
    if post_url is None:
        print("Dont Has URL")
    else:
        print(post_id)
        print(post_url)
    #https://m.facebook.com/story.php?story_fbid=3406271012790661&id=119240841493711
    comment_list = list()
    comment_list.append("Comment 1")
    comment_list.append("Comment 2")
    
    return comment_list