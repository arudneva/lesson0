import pandas as pd

# Слияние и объединение данных
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})
merged = pd.merge(df1, df2, on='key', how='outer')
print(merged)

import matplotlib.pyplot as plt
# Построить график
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Линейный график")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
# Построить столбчатую диаграмму
categories = ['A', 'B', 'C']
values = [4, 7, 5]
plt.bar(categories, values)
plt.title("Столбчатая диаграмма")
plt.show()

import numpy as np

# Создание одномерного массива
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)
# Создание двумерного массива (матрицы)
array_2d = np.array([[1, 2], [3, 4], [5, 6]])
print(array_2d)
# Массив 3x4, заполненный нулями
zeros_array = np.zeros((3, 4))
print(zeros_array)
# Основные арифметические операции
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
sum_array = array_a + array_b
print(sum_array)