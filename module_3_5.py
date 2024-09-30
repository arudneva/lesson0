def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str(number)) > 1 and str_number[1:] != '0':
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(402030)
print(result)

