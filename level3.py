"""Page hint to solve the riddle: uards on each of its sides."
...which download html page and regex the hell out of it. String pattern to look after is XXXxXXX and collect the small
ones."""

from level0 import url_edit
from level2 import get_html_page_source
import re


URL_LEVEL3 = 'http://www.pythonchallenge.com/pc/def/equality.html'


def parse_html(html_raw):
    """Parse html string for comment lines where the riddle is hide."""
    return re.findall(r'<!--(.*?)-->', str(html_raw))[0]  # return string not list


def solve_level3(riddle_str):
    """Parse string for pattern XXXxXXX and take the x.

    :REGEX:

        * [a-z]: 1 lower case letter
        * [A-Z]: 1 upper case letter
        * [A-Z]{3}: 3 consecutive upper case letters
        * [A-Z]{3}[a-z][A-Z]{3}: 3 upper case letters + 1 lower case letter + 3 upper case letters
        * [^A-Z]: any character BUT an upper case letter
        * [^A-Z]+: at least one such character
        * [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+: something else before and after our patter(AAAbCCC) so there's no more
                                               than 3 consecutive upper case letters on each side
        * [^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+: ...and we only care about the lower case
    """
    return ''.join(re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', riddle_str))


if __name__ == '__main__':
    html = get_html_page_source(URL_LEVEL3)
    riddle = parse_html(html)
    edit = solve_level3(riddle)
    url_level4 = url_edit(URL_LEVEL3, edit.lower())
    print(url_level4)
