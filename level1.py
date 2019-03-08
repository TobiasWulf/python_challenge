"""Page hint to solve the riddle: "Everybody thinks twice before solving this." ...K-->M O-->Q E-->G"""

URL_LEVEL1 = 'http://www.pythonchallenge.com/pc/def/map.html'
# noinspection SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection,SpellCheckingInspection
RIDDLE_LEVEL1 = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddga" +
                 "gclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc" +
                 " spj.")


def shift_list(l, n, right=True):
    """Shift list elements of list lby n times. Default is right shift, right=True False otherwise."""
    if right:
        return l[n:] + l[:n]
    else:
        return l[-n:] + l[:-n]


def solve_level1(riddle):
    """Solve level 1: the riddle is done with an rightshift by 2 in the hint string a-->c."""
    riddle = list(riddle)
    # noinspection SpellCheckingInspection
    abc = list('abcdefghijklmnopqrstuvwxyz')
    shifted_abc = shift_list(abc, 2)
    return ''.join([shifted_abc[abc.index(x)] if x in abc else x for x in riddle])


def url_edit(url):
    """Edit the end of the URL http://www.pythonchallenge.com/pc/def/<end>.html"""
    url = url.split('/')
    edit, ext = url[-1].split('.')
    edit = solve_level1(edit)
    url[-1] = '.'.join([edit, ext])
    return '/'.join(url)


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    unriddled = solve_level1(RIDDLE_LEVEL1)
    print(unriddled)

    url_level2 = url_edit(URL_LEVEL1)
    print(url_level2)
