class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in cart")
            
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitems__(self, index):
        return self.items[index]
    
    def __iter__(self):
        return iter(self.items)
    
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item, end=', ')