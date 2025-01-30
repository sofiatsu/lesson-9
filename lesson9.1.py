from collections import OrderedDict

def popular_words (text, words):
    text_lst = text.lower().split()
    ordered_dict = OrderedDict()
    s = 0
    for w in words:
        ordered_dict[words[s]] = text_lst.count(words[s])
        s += 1
    return ordered_dict


assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
        == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }), 'Test1'
print('OK')
