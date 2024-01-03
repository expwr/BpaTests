import random

class Pizzas:
    def __init__(self, menu_code, pizza_name, total_inventory, price):
        self.menu_code = menu_code
        self.pizza_name = pizza_name
        self.total_inventory = total_inventory
        self.price = price

    def getValue(self):
        return self.price * self.total_inventory

    def toString(self):
        return f"Menu Code: {self.menu_code}\nMenu Name: {self.pizza_name}\nMenu Price: ${self.price}\nTotal Pizza Count: {self.total_inventory}\nTotal Inventory Cost: ${self.getValue()}\n"

# Driver Section
if __name__ == "__main__":
    num_pizzas = input("Enter the number of pizza items to create (1 to 10): ")
    while not num_pizzas.isdigit() or int(num_pizzas) > 10:
        if not num_pizzas.isdigit():
            print("WARNING! You cannot enter letters. Try again please.")
        else:
            print("WARNING! You entered too low or too high for the quantity. Try again please.")
        num_pizzas = input("Enter the number of pizza items to create (1 to 10): ")

    num_pizzas = int(num_pizzas)
    pizzas_list = []

    for x in range(num_pizzas):
        menu_code = input("Enter the three-letter or number menu code: ")
        while len(menu_code) > 3:
            print("Menu code should not exceed 3 characters.")
            menu_code = input("Enter the three-letter or number menu code: ")

        pizza_name = input("Enter the pizza name: ")
        total_inventory = input("Enter the total inventory to keep for that pizza: ")
        while not total_inventory.isdigit():
            print("WARNING! You cannot enter letters. Try again please.")
            total_inventory = input("Enter the total inventory to keep for that pizza: ")

        total_inventory = int(total_inventory)
        price1 = random.randint(10, 20)
        price = "{:.2f}".format(price1)

        pizza = Pizzas(menu_code, pizza_name, total_inventory, price)
        pizzas_list.append(pizza)

    print("\nListed below is your current pizza inventory:")
    for pizza in pizzas_list:
        print(pizza.toString())
