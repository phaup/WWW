class Product:
    products = []

    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
    
    @classmethod
    def find_by_id(cls, id):
        return next(filter(lambda x: x.id == id, cls.products), None)

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)

    @classmethod
    def remove_product(cls, product):
        cls.products.remove(product)
