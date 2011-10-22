import unittest
from potter_shopping import PotterShoppingCart

class PotterTest(unittest.TestCase):

    def test_if_i_buy_no_books_the_total_price_is_zero(self):
        books = []
        self.assertEquals(0, PotterShoppingCart(books).total_price())

    def test_if_i_buy_1_books_the_total_price_is_8(self):
        books = ["Sorcerer-s Stone"]
        self.assertEquals(8, PotterShoppingCart(books).total_price())

    def test_if_i_buy_2_equal_books_the_total_price_is_16(self):
        books = ["Sorcerer-s Stone","Sorcerer-s Stone"]
        self.assertEquals(16, PotterShoppingCart(books).total_price())

    def test_if_i_buy_2_different_books_the_total_price_is_15_2(self):
        books = ["Sorcerer-s Stone","Deathly Hallows"]
        self.assertEquals(15.20, PotterShoppingCart(books).total_price())

    def test_if_i_buy_3_different_books_the_total_price_is_21_6(self):
        books = ["Sorcerer-s Stone","Deathly Hallows", "Goblet of Fire"]
        self.assertEquals(21.60, PotterShoppingCart(books).total_price())

    def test_if_i_buy_4_different_books_the_total_price_is_25_6(self):
        books = ["Sorcerer-s Stone","Deathly Hallows", "Goblet of Fire", "Phoenix Order"]
        self.assertEquals(25.60, PotterShoppingCart(books).total_price())


if __name__ == "__main__":

    unittest.main()
