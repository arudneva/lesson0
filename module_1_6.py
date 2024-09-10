my_dict = {'Anna':1990,'Ilia':2009,'Kirill':1990}
print(my_dict)
print(my_dict ['Anna'])
my_dict ['Ivan'] = 1995
print(my_dict)
my_dict.update({'Lena':1980,
                'Masha':1985})
a = my_dict.pop('Ivan')
print(a)
print(my_dict)

my_set = {1,2,3,1,2,3,1,2,3,1.25,1.5,1.25,True,'Hi'}
print(my_set)
print(my_set.add(9))
print(my_set.add('Hello'))
print(my_set)
print(my_set.remove(1.25))
print(my_set)
