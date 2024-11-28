import random
import threading
import time

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            add_balance = random.randint(50,500)
            self.balance += add_balance
            print(f"Пополнение: {add_balance}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            minus_balance = random.randint(50,500)
            print(f"Запрос на {minus_balance}")
            if minus_balance <= self.balance:
                with self.lock:
                    self.balance -= minus_balance
                    print(f"Снятие: {minus_balance}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')