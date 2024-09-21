import random
n = random.randint(3,20)
print("Число в первом поле: ", n)


def generate_password(n):
    password = ''
    for i in range(1, n // 2 + 1):
        j = n - i
        pair_sum = i + j
        if n % pair_sum == 0:
            password += str(i) + str(j)
    return password

print('Пароль:', generate_password(n))


