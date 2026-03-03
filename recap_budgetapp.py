'''
class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def __str__(self):
        return f"{self.name:*^30}\n"
        
'''

ledger = []



def deposit(amount, description):
    amount = int(input("Enter amount: "))
    description = input("Enter description: ")
    ledger.append({'amount': amount, 'description': description})


def get_amount():
    total = 0
    for item in ledger:
        total += item['amount']
    return total