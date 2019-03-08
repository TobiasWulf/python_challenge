"""Page hint to solve the riddle: There was no one. It seems like it has to be a creepy url get and replace game."""

import urllib.request
import urllib.parse
import re


URL_LEVEL4 = 'http://www.pythonchallenge.com/pc/def/linkedlist.html'


def get_html_page_source(url):
    """Get html source from url and return it as string.
    :param url: Valid URL to web page.
    :type url: str.
    :return: HTML source from requested URL.
    :rtype: str.
    :raises: None.
    """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as respond:
        return str(respond.read())


if __name__ == '__main__':  # Needs function to pull get requests until server broke or post!
    url_1 = URL_LEVEL4

    url_base_1 = url_1.split('/')[:-1]

    html_ext_1 = url_1.split('/')[-1]
    html_source_1 = get_html_page_source(url_1)

    html_ext_2 = re.findall(r'(\w+\.\w+)', html_source_1)
    url_2 = '/'.join(url_base_1 + html_ext_2)
    html_source_2 = get_html_page_source(url_2)

    html_ext_3 = re.findall(r'<a href\=\"([\w+].*?)\">', html_source_2)
    url_3 = '/'.join(url_base_1 + html_ext_3)
    html_source_3 = get_html_page_source(url_3)

    url_base_2 = url_3.split('=')[:-1]

    html_ext_4 = [re.search(r'\w+(\d+)', html_source_3).group()]
    url_4 = '='.join(url_base_2 + html_ext_4)
    html_source_4 = get_html_page_source(url_4)

    html_ext_5 = [re.search(r'\w+(\d+)', html_source_4).group()]
    url_5 = '='.join(url_base_2 + html_ext_5)
    html_source_5 = get_html_page_source(url_5)

    html_ext_6 = [re.search(r'\w+(\d+)', html_source_5).group()]
    url_6 = '='.join(url_base_2 + html_ext_6)
    html_source_6 = get_html_page_source(url_6)

    html_ext_7 = [re.search(r'\w+(\d+)', html_source_6).group()]
    url_7 = '='.join(url_base_2 + html_ext_7)
    html_source_7 = get_html_page_source(url_7)
