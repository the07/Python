class Flower:
    """A class that generalises flowers.

    name    name of the flower
    number  number of petals
    price   price of the flowers
    """

    def __init__(self, name, number, price):

        self._name = name
        self._number = number
        self._price = price

    def print_flower(self):

        return [self._name, self._number, self._price]

if __name__ == '__main__':

    Rose = Flower('Rose')
    print (Rose.print_flower())
