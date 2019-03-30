# Concrete products
class ProductA:
    def __init__(self, *args, **kwargs):
        self.future_a = False
        self.future_b = False

    def set_future_a(self):
        print(self, 'set future a')
        self.future_a = True

    def set_future_b(self):
        print(self, 'set future b')
        self.future_b = True


class ProductB:
    def __init__(self, *args, **kwargs):
        self.future_a = False
        self.future_b = False

    def set_future_a(self):
        print(self, 'set future a')
        self.future_a = True

    def set_future_b(self):
        print(self, 'set future b')
        self.future_b = True


# Interface Builder
class Builder:
    def reset(self):
        raise NotImplementedError

    def build_step_a(self):
        raise NotImplementedError

    def build_step_b(self):
        raise NotImplementedError

    def get_result(self):
        raise NotImplementedError


# Concrete builders
class ConcreteBuilderA(Builder):
    def __init__(self, *args, **kwargs):
        self.product = ProductA()

    def reset(self):
        self.product = ProductA()

    def build_step_a(self):
        self.product.set_future_a()
        print(self, 'build step a')

    def build_step_b(self):
        self.product.set_future_b()
        print(self, 'build step b')

    def get_result(self):
        return self.product


class ConcreteBuilderB(Builder):
    def __init__(self, *args, **kwargs):
        self.product = ProductB()

    def reset(self):
        self.product = ProductB()

    def build_step_a(self):
        self.product.set_future_a()
        print(self, 'build step a')

    def build_step_b(self):
        self.product.set_future_b()
        print(self, 'build step b')

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def make(self, type='default'):
        self.builder.reset()
        if type == 'simple':
            self.builder.build_step_a()
        else:
            self.builder.build_step_a()
            self.builder.build_step_b()

    def change_builder(self, builder):
        self.builder = builder


if __name__ == "__main__":
    builder = ConcreteBuilderA()
    director = Director(builder)
    director.make()
    product = builder.get_result()
    print(product)
