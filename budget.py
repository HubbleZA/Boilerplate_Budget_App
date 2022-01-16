class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.value = 0
        self.description = ''

    def deposit(self, value, description=''):
        self.value += value
        self.description = description
        self.ledger.append({"amount": value, "description": description})

    def withdraw(self, value, description=''):
        if not self.check_funds(value):
            return False
        else:
            self.value -= value
            self.description = description
            self.ledger.append({"amount": -value, "description": description})
            return True

    def get_balance(self):
        return self.value

    def transfer(self, value, category):
        if not self.check_funds(value):
            return False
        else:
            self.withdraw(value, "Transfer to " + str(category.name))
            category.deposit(value, "Transfer from " + str(self.name))
            return True

    def check_funds(self, value):
        if self.value < value:
            return False
        else:
            return True

    def __str__(self):
        n = str(self.name)
        for i in self.ledger:
            print(i)
        total = ('Total: ' + str(self.get_balance()))
        return total



def create_spend_chart(categories):
    return print("")