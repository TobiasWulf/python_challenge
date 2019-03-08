"""Page hint to solve the riddle: "recognize the characters. maybe they are in the book, but MAYBE they are in the page
source." ...download page source and look for hints. The hints should be hidden a comment"""

from level0 import url_edit
import urllib.request
import urllib.parse
import re


URL_LEVEL2 = 'http://www.pythonchallenge.com/pc/def/ocr.html'


def get_html_page_source(url):
    """Get the html source from website as raw binary html."""
    # make some values to handle a POST request from url when pulled
    values = {'s': 'basics',
              'submit': 'search'
              }
    # encode
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    # pull request and wait for response
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        return response.read()


# noinspection PyShadowingNames,PyShadowingNames
def parse_html(html):
    """Parse html string for comment lines where the hints and riddles are hide."""
    # noinspection PyShadowingNames
    hint, riddle = re.findall(r'<!--\\n(.*?)\\n-->', str(html))
    return hint, riddle


def solve_level2(hint_msg, riddle_str):
    """Solve level 2 by counting the chars in the riddles string. Chars with min appearance build the url edit."""
    print(hint_msg)

    # if a new char appears append
    # else count on position
    chars = []
    counts = []

    for c in riddle_str:
        if c not in chars:
            chars.append(c)
            counts.append(0)
        else:
            ind = chars.index(c)
            counts[ind] += 1

    # show results
    print("\t* Char appearances:")
    for i, c in enumerate(chars):
        print("\t\t* {}: {:>5}".format(c, str(counts[i])))

    # filter url editable from results
    # min searches for first min in al list
    ind = counts.index(min(counts))
    return ''.join(chars[ind:])


if __name__ == '__main__':
    html = get_html_page_source(URL_LEVEL2)
    hint, riddle = parse_html(html)
    edit = solve_level2(hint, riddle)
    url_level3 = url_edit(URL_LEVEL2, edit)
    print(url_level3)
