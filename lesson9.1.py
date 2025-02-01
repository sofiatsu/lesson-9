def popular_words (text, words):
    text_lst = text.lower().split()
    new_dict = {}
    for w in words:
        new_dict[w] = text_lst.count(w)
    return new_dict


assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
        == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }), 'Test1'
print('OK')
