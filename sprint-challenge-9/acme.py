from random import randint


class Product:
    """A product of Acme."""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """How likely is it for the item to be stolen."""
        ratio = self.price / self.weight

        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """What king of explosion can it make when heated."""
        product = self.flammability * self.weight

        if product < 10:
            return '...fizzle.'
        elif product < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """A boxing glove type of product."""
    def __init__(self, name, price=10, weight=10,
                 flammability=0.5):
        super.__init__(name=name, price=price, weight=weight,
                       flammability=flammability)

    def explode(self):
        """What king of explosion can it make when heated."""
        return '...it\'s a glove.'

    def punch(self):
        """The punching strength of the glove."""
        weight = self.weight
        if weight < 5:
            return 'That tickles.'
        elif weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
