
def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        if (root_word.upper().count(words.upper()) > 0
            or words.upper().count(root_word.upper()) > 0
        ):
            same_words.append(words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)