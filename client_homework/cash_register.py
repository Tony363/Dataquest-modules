import locale

locale.setlocale(locale.LC_ALL,'en_US')

class CashRegister:

    def __init__(self):
        self.item = 0
        self.total_price = 0

    def price(self):
        print(self.price)

    def additem(self,price):

        self.price = price
        self.item += 1
        self.total_price += self.price
        
    def getTotal(self):
        return self.total_price

    def getCount(self):
        return self.item

if __name__ == "__main__":
    print("Welcome, what can I do for you")
    print()

    instance = CashRegister()

    while True: 
        try:       
            instance.additem(float(input('what would you like? ')))
            print()
        except ValueError:
            print('please enter price') 
            print()
            continue

        query = input("anything else?: [y]/n ")
        print()

        if query.lower() == 'n':
            print('that\'s {} number of items'.format(instance.getCount()))
            print('total price will be $', locale.currency(instance.getTotal()))
            break
    

        

    