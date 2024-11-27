import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()

print(f"Работа функций {end_time - start_time}")

def new_thread(word_count, file_name):
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    thread.start()
    return thread

start_time_threads = time.time()

threads = [
    new_thread(10, 'example5.txt'),
    new_thread(30, 'example6.txt'),
    new_thread(200, 'example7.txt'),
    new_thread(100, 'example8.txt')
]

for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Работа потоков {end_time_threads - start_time_threads}")