"""Page hint to solve the riddle: "Try to change the URL address." ...with 2**38, displayed on the website."""

URL_LEVEL0 = 'http://www.pythonchallenge.com/pc/def/0.html'
HINT_LEVEL0 = 2 ** 38


def url_edit(url, edit):
    """Edit the end of the URL http://www.pythonchallenge.com/pc/def/<end>.html"""
    url = url.split('/')
    url[-1] = '{}.html'.format(str(edit))
    return '/'.join(url)


if __name__ == '__main__':
    url_level1 = url_edit(URL_LEVEL0, HINT_LEVEL0)
    print(url_level1)
