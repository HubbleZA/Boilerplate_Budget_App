class Category:

    def __init__(self, name):
        self.name = name

    def deposit(self, value, description=''):
        self.value = value
        self.description = description

    def withdraw(self, value, description=''):
        self.value = value
        self.description = description

    def get_balance(self):
        self.balance = 3

    def transfer(self, value, catagory):
        self.value = value
        self.catagory = catagory


def create_spend_chart(categories):
    return