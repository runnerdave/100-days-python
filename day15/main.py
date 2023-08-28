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

    def count_money(self):
        total_value = 0
        for details in self.collection.values():
            value = details['value']
            quantity = details['qty']
            total_value += value * quantity
        return total_value


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

    def insert_coins(self):
        user_coins = CoinCollection()
        print("")
        for coin, values in user_coins.get_collection().items():
            qty = input(f"Enter number of {coin}s(0 if none): ")
            values['qty'] = int(qty)
        print("")
        return user_coins

    def add_money_from_coffee(self, money):
        for coin, values in self.coins.get_collection().items():
            values['qty'] += money.get_collection()[coin]['qty']

    def return_change(self, price, money):
        change = money.count_money() - price
        change_00 = change*100
        coins = self.coins.get_collection()
        while change_00 > 0:
            if change_00 % 25 == 0:
                quarters = change_00/25
                coins['quarter']['qty'] -= quarters
                change_00 -= 25*quarters
            if change_00 % 10 == 0:
                dimes = change_00/10
                coins['dime']['qty'] -= dimes
                change_00 -= 10*dimes
            if change_00 % 5 == 0:
                nickels = change_00/5
                coins['nickel']['qty'] -= nickels
                change_00 -= 5*nickels
            if change_00 > 0:
                pennies = change_00
                coins['penny']['qty'] -= pennies
                change_00 = 0
        return round(change, 2)
    
    def use_ingredients(self, coffee_type):
        self.water -= self.coffee_types[coffee_type]['water']
        self.milk -= self.coffee_types[coffee_type]['milk']
        self.coffee -= self.coffee_types[coffee_type]['coffee']
    
    def make_coffee(self, coffee_type):
        if self.check_resources(coffee_type):
            money_inserted = self.insert_coins()
            price = self.coffee_types[coffee_type]['price']
            if money_inserted.count_money() < price:
                print("​Sorry that's not enough money. Money refunded.​")            
            else:
                self.add_money_from_coffee(money_inserted)
                self.use_ingredients(coffee_type)
                print(f"Here is your {coffee_type}. Enjoy!")
                if money_inserted.count_money() >= price:
                    change = self.return_change(price, money_inserted)
                    print(f"Here is ${change} dollars in change.")

    def serve_order(self):
        self.print_coffee_options()
        choice = input("What would you like?(select a number) ")
        if choice == "off":
            sys.exit()
        match choice:
            case "1":
                self.make_coffee('Latte')
            case "2":
                self.make_coffee('StrongLatte')
            case "3":
                self.make_coffee('ShortBlack')
            case "report":
                print(self)
            case _:
                print("Choice not available")
        print("")

    def __build(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        self.coins.get_collection()['quarter']['qty'] = 10
        self.coins.get_collection()['dime']['qty'] = 10
        self.coins.get_collection()['nickel']['qty'] = 10
        self.coins.get_collection()['penny']['qty'] = 10

    def __repr__(self):
        return f"Water: {self.water}ml \nMilk: {self.milk}ml \nCoffee: {self.coffee}g\nMoney: ${self.coins.count_money()}"


if __name__ == '__main__':
    print(logo)
    coffeeMachine = CoffeeMachine()
    while True:
        coffeeMachine.serve_order()
