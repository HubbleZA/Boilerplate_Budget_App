class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.value = 0

    def deposit(self, value, description=''):
        self.value += value
        self.description = description
        self.ledger.append({"amount": value,"description": description})

    def withdraw(self, value, description=''):
        if self.check_funds(value) == False:
            return False
        else:
            self.value -= value
            self.description = description
            self.ledger.append({"amount": -value,"description": description})
            return True

    def get_balance(self):
        print(self.value)

    def transfer(self, value, catagory):
        if self.check_funds(value) == False:
            return False
        else:
            self.withdraw(value, "Transfer to " + str(catagory.name))
            catagory.deposit(value, "Transfer from " + str(self.name))
            return True

    def check_funds(self, value):
        if self.value < value:
            return False



def create_spend_chart(categories):
    return