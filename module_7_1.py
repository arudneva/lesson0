from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
       return f'{self.name}, {self.weight}, {self.category}'



class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.products = []

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        existing_products = file.read()
        file.close()
        return existing_products


    def add(self, *products):
        existing_products = set()
        name = 'products.txt'
        file = open(name, 'a')
        existing_products = self.get_products()
        for product in products:
            if str(product) in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product)+'\n')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())