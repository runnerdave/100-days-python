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
    WATER_CAPACITY = 1000
    MILK_CAPACITY = 1000
    COFFEE_CAPACITY = 1000

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
        for i, (coffee_type, details) in enumerate(self.coffee_types.items(), start=1):
            print(f"{i}: {coffee_type} ${details['price']}")

    def check_resources(self, coffee_type):
        coffee_type = self.coffee_types.get(coffee_type)
        if coffee_type:
            if coffee_type['water'] > self.water:
                print("Sorry, not enough water")
                return False
            if coffee_type['milk'] > self.milk:
                print("Sorry, not enough milk")
                return False
            if coffee_type['coffee'] > self.coffee:
                print("Sorry, not enough coffee")
                return False
            return True
        return False

    def insert_coins(self):
        user_coins = CoinCollection()
        print("")
        for coin, values in user_coins.get_collection().items():
            qty = input(f"Enter the number of {coin}s (0 if none): ")
            values['qty'] = int(qty)
        print("")
        return user_coins

    def add_money_from_coffee(self, money):
        for coin, values in self.coins.get_collection().items():
            values['qty'] += money.get_collection()[coin]['qty']

    def return_change(self, price, money):
        change = money.count_money() - price
        change_00 = int(change * 100)
        coins = self.coins.get_collection()
        denominations = [25, 10, 5, 1]

        for denomination in denominations:
            if change_00 >= denomination:
                coins_qty = change_00 // denomination
                coins[f'quarter']['qty'] -= coins_qty
                change_00 -= denomination * coins_qty

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
                print("Sorry, that's not enough money. Money refunded.")
            else:
                self.add_money_from_coffee(money_inserted)
                self.use_ingredients(coffee_type)
                print(f"Here is your {coffee_type}. Enjoy!")
                if money_inserted.count_money() >= price:
                    change = self.return_change(price, money_inserted)
                    print(f"Here is ${change} dollars in change.")

    def serve_order(self):
        self.print_coffee_options()
        choice = input("What would you like? (select a number) ")
        if choice == "off":
            sys.exit()
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.coffee_types):
                coffee_type = list(self.coffee_types.keys())[choice - 1]
                self.make_coffee(coffee_type)
                print("")
                return
        print("Choice not available")
        print("")

    def __build(self):
        self.water = self.WATER_CAPACITY
        self.milk = self.MILK_CAPACITY
        self.coffee = self.COFFEE_CAPACITY
        coins_collection = self.coins.get_collection()
        coins_collection['quarter']['qty'] = 10
        coins_collection['dime']['qty'] = 10
        coins_collection['nickel']['qty'] = 10
        coins_collection['penny']['qty'] = 10

    def __repr__(self):
        return f"Water: {self.water}ml \nMilk: {self.milk}ml \nCoffee: {self.coffee}g\nMoney: ${self.coins.count_money()}"


if __name__ == '__main__':
    print(logo)
    coffeeMachine = CoffeeMachine()
    while True:
        coffeeMachine.serve_order()