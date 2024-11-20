def all_variants(text):
    len_text = len(text)
    for i in range(len_text):
        for j in range(i + 1, len_text + 1):
            yield text[i:j]

a = all_variants("abc")
for i in a:
    print(i)