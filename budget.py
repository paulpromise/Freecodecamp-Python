class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry['description'][:23]  # max 23 chars
            amount = f"{entry['amount']:.2f}"       # 2 decimal places
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    
    def withdraw(self, amount, description=''):
        if self.get_balance() >= amount:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False
        
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False


def create_spend_chart(categories):
    # Calculate total spent per category
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    chart = "Percentage spent by category\n"

    # Percentage bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for pct in percentages:
            chart += " o " if pct >= i else "   "
        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")
