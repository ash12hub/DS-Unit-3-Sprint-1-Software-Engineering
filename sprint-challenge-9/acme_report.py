from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
list_end = 4


def generate_products(num_products=30):
    """Generate some Acme products."""
    products = []
    for _ in range(num_products):
        adjective = ADJECTIVES[randint(0, 4)]
        noun = NOUNS[randint(0, 4)]
        name = f'{adjective} {noun}'
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)

        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    """A report of a number of Acme products."""
    size = len(products)
    names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for product in products:
        if product.name not in names:
            names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT\n' +
          f'Unique product names: {len(names)}\n' +
          f'Average price: {total_price / size}\n' +
          f'Average weight: {total_weight / size}\n' +
          f'Average flammability: {total_flammability / size}')
    return

if __name__ == '__main__':
    inventory_report(generate_products())
