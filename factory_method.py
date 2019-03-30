class Product:
    # определяем общий интерфейс
    def do_stuff(self):
        pass


class ConcreteProductA(Product):
    def do_stuff(self):
        print('{} do stuff'.format(self))


class ConcreteProductB(Product):
    def do_stuff(self):
        print('{} do stuff'.format(self))


def create_product_a():
    return ConcreteProductA()


def create_product_b():
    return ConcreteProductB()


# client
class Application:
    creator_product_by_type = {
        'A': create_product_a,
        'B': create_product_b,
        'default': create_product_a,
    }

    def __init__(self, type_product='default'):
        create_product = self.creator_product_by_type.get(
            type_product, 'default')
        self.product = create_product()

    def do_stuff(self):
        print('{} do stuff'.format(self))
        return self.product.do_stuff()


if __name__ == "__main__":
    app = Application()
    app.do_stuff()
