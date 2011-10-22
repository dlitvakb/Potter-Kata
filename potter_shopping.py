class PotterShoppingCart(object):
    def __init__(self, books):
        self.books = books
        self.discounts = {-1: 0, 0: 0, 1: 0.05, 2:0.1, 3:0.2, 4:0.25, 5:0.25, 6:0.25}

    def total_price(self):
        return float("%.2f" % round((len(self.books) * 8) * (1 - self.discounts.get(len([x for x in set(self.books)]) - 1)), 2))
