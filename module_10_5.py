from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Линейный вызов
# start_time = time.time()
# for filename in filenames:
#     read_info(filename)
# finish_time = time.time()
# summa_time = finish_time - start_time
# print(f"{summa_time} (линейный)")

# Многопроцессный
if __name__ == '__main__':
    start_time = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    finish_time = time.time()
    summa_time = finish_time - start_time
    print(f"{summa_time} (многопроцессный)")