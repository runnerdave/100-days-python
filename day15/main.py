import sys
from art import logo

class CoinCollection:
    def __init__(self):
        self.collection = {
            'quarter': {'value': 0.25, 'qty': 0},
            'dime': {'value': 0.10, 'qty': 0},
            'nickel': {'value': 0.05, 'qty': 0},
            'penny': {'value': 0.01, 'qty': 0},
        }

    def get_collection(self):
        return self.collection

class CoffeeMachine:
    def __init__(self):
        self.water = 0.0
        self.milk = 0.0
        self.coffee = 0.0
        self.coffee_types = {
            'Latte': {'price': 2.50, 'water': 200, 'milk': 200, 'coffee': 40},
            'StrongLatte': {'price': 4.50, 'water': 200, 'milk': 200, 'coffee': 80},
            'ShortBlack': {'price': 2.00, 'water': 100, 'milk': 0, 'coffee': 40},
        }
        self.coins = CoinCollection()
        self.__build()

    def __count_money(self, coins):
        total_value = 0
        for _, details in coins.get_collection().items():
            value = details['value']
            quantity = details['qty']
            total_value += value * quantity
        return total_value
    
    def print_coffee_options(self):
        print("These are the coffee options:")
        i = 1
        for coffee_type, details in self.coffee_types.items():
            print(f"{i}: {coffee_type} ${details['price']}")
            i += 1

    def check_resources(self, coffee_type):
        coffee_type = self.coffee_types[coffee_type]
        if coffee_type != None:
            if coffee_type['water'] > self.water:
                print("Sorry not enough water")
                return False
            if coffee_type['milk'] > self.milk:
                print("Sorry not enough milk")
                return False
            if coffee_type['coffee'] > self.coffee:
                print("Sorry not enough coffee")
                return False
            return True
        return False

    # def insert_coins(self):
    #     keep_inserting = True
    #     user_coins = purse
    #     while keep_inserting:

            

    def serve_order(self):
        self.print_coffee_options()
        choice = input("What would you like?(select a number) ")
        if choice == "off":
            sys.exit()
        match choice:
            case "1":
                if self.check_resources('Latte'):
                    insert_coins()

            case "2":
                self.check_resources('StrongLatte')
            case "3":
                self.check_resources('ShortBlack')
            case "report":
                print(self)
            case _:
                print("Choice not available")



    def __build(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.coins.get_collection()['quarter']['qty'] = 10
        self.coins.get_collection()['dime']['qty'] = 10
        self.coins.get_collection()['nickel']['qty'] = 10
        self.coins.get_collection()['penny']['qty'] = 10

    def __repr__(self):
        return f"Water: {self.water}ml \nMilk: {self.milk}ml \nCoffee: {self.coffee}g\nMoney: ${self.__count_money(self.coins)}"


if __name__ == '__main__':
    print(logo)
    coffeeMachine = CoffeeMachine()
    # print(coffeeMachine)
    coffeeMachine.serve_order()
