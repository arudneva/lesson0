first = int(input('Ввелите число 1: '))
second = int(input('Ввелите число 2: '))
third = int(input('Ввелите число 3: '))

if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')