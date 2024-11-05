def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    counter = 0
    for string in strings:
        counter += 1
        strings_positions[(counter, file.tell())] = string
        file.write(string + '\n')

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)