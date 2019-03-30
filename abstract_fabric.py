# Interface for products
class ProductA:
    def do_stuff(self):
        pass


class ProductB:
    def do_stuff(self):
        pass


# Concrete products
class ConcreteProductA1(ProductA):
    def do_stuff(self):
        print(self, 'do stuff')


class ConcreteProductA2(ProductA):
    def do_stuff(self):
        print(self, 'do stuff')


class ConcreteProductB1(ProductB):
    def do_stuff(self):
        print(self, 'do stuff')


class ConcreteProductB2(ProductB):
    def do_stuff(self):
        print(self, 'do stuff')


# Interface factories
class Factory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


# Concrete factories
class ConcreteFactory1(Factory):
    def create_product_a(self):
        print(self, 'create product a')
        return ConcreteProductA1()

    def create_product_b(self):
        print(self, 'create product b')
        return ConcreteProductB1()


class ConcreteFactory2(Factory):
    def create_product_a(self):
        print(self, 'create product a')
        return ConcreteProductA2()

    def create_product_b(self):
        print(self, 'create product b')
        return ConcreteProductB2()


# Application
class Application:
    factory_by_type = {
        '1': ConcreteFactory1,
        '2': ConcreteFactory2,
        'default': ConcreteFactory1,
    }

    def __init__(self, factory_type='default'):
        Factory = self.factory_by_type.get(factory_type, 'default')
        self.factory = Factory()

    def do_stuff(self):
        product_a = self.factory.create_product_a()
        product_a.do_stuff()
        product_b = self.factory.create_product_b()
        product_b.do_stuff()

if __name__ == "__main__":
    app = Application(factory_type='2')
    app.do_stuff()
