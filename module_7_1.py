from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        name = 'products.txt'
        file = open(name, 'a')
        file.write(f'\n{self.name}, {self.weight}, {self.category}')
        file.close()

    def __str__(self):
       return f'{self.name}, {self.weight}, {self.category}'



class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return self.__file_name


    def add(self, *products):
        name = 'products.txt'
        file = open(name, 'a')
        for product in products:
            if isinstance(product, Product):
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(product.name)
        file.close()


  
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())