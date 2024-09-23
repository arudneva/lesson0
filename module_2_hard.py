import random
n = random.randint(3,20)
print("Число в первом поле: ", n)


def generate_password(n):
    password = ''
    for i in range(1, n // 2 + 1):
        for j in range(1, n):
            pair_sum = i + j
            if n % pair_sum == 0 and j>i:
                password += str(i) + str(j)
    return password

print('Пароль:', generate_password(n))


