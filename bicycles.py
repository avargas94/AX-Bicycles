class Bicycles():

    def __init__(self, model, weight, price):
        self.model = model
        self.weight = weight
        self.price = price
        
    def __repr__(self):
        return "{model}, {weight}, {price}".format(model=self.model, weight=self.weight, price=self.price)
    
class Shop():

    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.perc_markup = .20
        self.profit = 0
        
    def create_inventory(self, bicycle, qty):
        self.inventory[bicycle] = qty
        
    def show_inventory(self):
        current_inventory = []
        
        for bicycle in self.inventory:
            if self.inventory[bicycle] > 0:
                current_inventory.append(bicycle)
        return current_inventory
        
    def markup(self, c):
        price = c * shop.perc_markup + c 
        return price
        
    def transaction_profit(self):
        pass
        
    def store_profit(self):
        pass
        
    def remove_inventory(self, bike):
        self.inventory -= 1
        
class Customer():
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bike_budget = []
        self.customer_options = []
        self.customer_selection = None
        self.sold = None
        
    def budget(self, bicycle):
        if shop.markup(bicycle.price) <= self.money:
            self.bike_budget.append(bicycle)
            
    def selection(self):
        print("Here are the bicycles that are in your budget.")
        for bicycle in self.bike_budget:
            self.customer_options.append(bicycle.model)
        return self.customer_options
        
    def purchase(self):
        self.customer_selection = input("Please select the bike that you would like to purchase. ")
        
        if self.customer_selection == "HIGHTOWER CC 29 XO":
            self.sold = bike1
        elif self.customer_selection == "SIRRUS EXPERT CARBON X1":
            self.sold = bike2
        elif self.customer_selection == "AMERICANO ROHLOFF 56CM BLACK":
            self.sold = bike3
        elif self.customer_selection == "DOMANE ALR 3":
            self.sold = bike4
        elif self.customer_selection == "DOMANE SLR 6 DISC":
            self.sold = bike5
        elif self.customer_selection == "SILQUE S 7":
            self.sold = bike6
        else:
            print("We don't have the bike in stock!")
        print("\n")    
        print("{name} you have purchase the {model} for ${price}. You have ${remaining} remaining in your wallet!".format(name=self.name, model=self.sold.model, price=shop.markup(self.sold.price), remaining=self.money-shop.markup(self.sold.price)))
        
        shop.remove_inventory(self.sold.model)
        shop.calcuate_profit()
        shop.total_profit()
        
if __name__ == "__main__":
    
    ryan = Customer("Ryan", 200)
    andrew  = Customer("Andrew", 500)
    dante = Customer("Dante", 1000)
    
    shop = Shop("AX Bicycles")
    
    print("Welcome to {}".format(shop.name))
    
    bike1 = Bicycles("HIGHTOWER CC 29 XO", 20, 800)
    bike2 = Bicycles("SIRRUS EXPERT CARBON X1", 25, 450)
    bike3 = Bicycles("AMERICANO ROHLOFF 56CM BLACK", 24, 350)
    bike4 = Bicycles("DOMANE ALR 3", 25, 250)
    bike5 = Bicycles("DOMANE SLR 6 DISC", 15, 100)
    bike6 = Bicycles("SILQUE S 7", 15, 150)
    
    shop.create_inventory(bike1, 1)
    shop.create_inventory(bike2, 1)
    shop.create_inventory(bike3, 1)
    shop.create_inventory(bike4, 1)
    shop.create_inventory(bike5, 1)
    shop.create_inventory(bike6, 1)
    
    print('Here are the bicycles that we carry!\n')
    
    for bicycle in shop.inventory:
        print("Model: {}".format(bicycle.model))
        print("Price: ${}".format(shop.markup(bicycle.price)))
        print("Weight: {}".format(bicycle.weight))
    print("\n")
    
    print("Welcome {name}! {name}'s budget is ${money}\n".format(name=andrew.name, money=andrew.money))
    
    for bicycle in shop.show_inventory():
        andrew.budget(bicycle)
    for bike in andrew.selection():
        print(bike)
        
    andrew.purchase()
 
        
    
    

    
    