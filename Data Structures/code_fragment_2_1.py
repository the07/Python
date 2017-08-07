class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """ Create a new credit card instance

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the account identfier
        limit       credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the name of the bank"""
        return self._bank

    def get_account(self):
        """Return the account identifying number, stored as string"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return true if charge was processed, false if denied.
        """

        if price + self._balance > self._limit: # if charge would exceed limit,
            return False                        # cannot accept charge.
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance """

        if not isinstance(amount, int):
            raise TypeError('amount must be numeric')
        elif amount < 0:
            raise ValueError('amount must be positive')
        elif amount > self._balance:
            change = amount - self._balance
            print ('You were charged {0}, change: {1}'.format(self._balance, change))
            self._balance = 0
        else:
            self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """An extension to the credit card that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credut card instance

        customer        name of the customer
        bank            name of the bank
        acnt            the account identifier
        limit           credit limit
        apr             annual percentage rate
        """

        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card assuming sufficient credit limit.

        Return true if charge was processed.
        Return false and assess 5rs if charge is denied.
        """

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def processed_monthly(self):
        """Assess monthly interest on outstanding balance"""

        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == '__main__':

    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings','5391 0375 9387 5309', 2500))
    print (wallet[0])
    wallet[0].charge(20)
    wallet[0].make_payment(-10)
    print (wallet[0].get_balance())
