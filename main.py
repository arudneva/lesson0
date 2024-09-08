print("1st program")
print(9**0.5*5)
print("2nd program")
print(9.99>9.98 and 1000!=1000.1)
print("3rd program")
print((2*2+2)==(2*(2+2)))
print("4th program")
a=str(int(float('123.456')*10))
print(str(int(float('123.456')*10))[3])

a = 'Топинамбур'
print(a[0])
print(a[-1])
print(a[len(a)//2:])
print(a[::-1])
print(a[1::2])

Completed_homework = 12
Number_of_hours = 1.5
Course_name = 'Python'
Time_for_one_task = Number_of_hours/Completed_homework
print('Курс: ',Course_name,'всего задач: ',Completed_homework,'затрачено часов: ',Number_of_hours,'среднее время выполнения ',Time_for_one_task)