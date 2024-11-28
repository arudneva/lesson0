import threading
import time

enemies = 100

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemies = enemies
        self.counter = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.counter += 1
            time.sleep(1)
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name} сражается {self.counter} осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.counter} дней(дня)!")
        

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")