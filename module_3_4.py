def single_root_words(root_word,*other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for i in range(len(other_words)):
        a = other_words[i]
        if root_word_lower in a.lower() or a.lower() in root_word_lower:
            same_words.append(a)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)