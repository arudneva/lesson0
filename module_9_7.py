def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0 or result % 3 == 0:
            print("Составное")
            return result
        else:
            print("Простое")
            return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)