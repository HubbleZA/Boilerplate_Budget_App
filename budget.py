import math
import itertools


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
        n = '*' * round((30 / 2) - (len(str(self.name)) / 2)) + str(self.name) + '*' * (
            math.floor((30 / 2) - (len(str(self.name)) / 2))) + '\n'
        for i in self.ledger:
            n = (n + str(i['description'])[:23])
            desclen = len(str(i['description'])[:23])
            n = n + str("{:.2f}".format(float(i['amount']))).rjust(30 - desclen) + '\n'
        n = n + str('Total: ' + str(self.get_balance()))
        return n


def create_spend_chart(categories):
    spentlist = []
    n = 0
    totalspent = 0
    for k in categories:
        spent = 0
        for i in k.ledger:
            if i['amount'] < 0:
                spent = spent + i['amount']
            else:
                pass
        totalspent = totalspent + spent
        spentlist.append({'Name': k.name, 'Amount': spent})
        n += 1
    for i in spentlist:
        i['Percentage'] = round((i['Amount'] / (totalspent) * 100),-1)
    graphlist = []
    prt = "Percentage spent by category\n"
    for i in reversed(range(11)):
        graphlist.append(f"{(str(10 * i) + '|').rjust(4) + ' ' * 10}\n")
    place = 2
    for i in spentlist:
        place += 3
        numlist = 0
        for k in graphlist:
            t = k.index('|')
            num = int(k[:t])
            percentage = int(i['Percentage'])
            if percentage == 10:
                percentage = percentage - 1
            if percentage >= num:
                change = list(k)
                change[place] = 'o'
                change = "".join(change)
                graphlist[numlist] = change
            numlist += 1
    for i in graphlist:
        prt = prt + i
    prt = prt + "-".rjust(5)
    prt = prt + "---"*len(categories) + "\n"
    wordlist = ""
    for i in categories:
        wordlist = wordlist + i.name + " "
    for x in itertools.zip_longest(*wordlist.split(), fillvalue=' '):
        prt = prt + ('  '.join(x)).rjust(12) + "  " + "\n"
    #removing the last \n from the last line
    prt = prt[:-1]
    return prt
