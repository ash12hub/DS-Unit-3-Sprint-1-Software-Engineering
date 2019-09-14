import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_price(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_price(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_custom_product(self):
        """Create a custom product to test."""
        prod = Product('Test Product', 25, 50, 0.7)

        # Stealability is 0.5
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

        # Explode is 35
        self.assertEqual(prod.explode(), '...boom!')


class AcmeREportTests(unittest.TestCase):
    """Making sure Acme reports are accurate."""
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test if all the names of the products are allowed."""
        products = generate_products()
        for product in products:
            name_split = product.name.split(' ')
            adjective = name_split[0]
            noun = name_split[1]
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
