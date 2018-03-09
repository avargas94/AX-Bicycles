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
        self.sprofit = 0
        self.tprofit = 0
        
    def create_inventory(self, bicycle, qty):
        self.inventory[bicycle] = qty
        
    def show_inventory(self):
        current_inventory = []
        
        for bicycle in self.inventory:
            if self.inventory[bicycle] > 0:
                current_inventory.append(bicycle)
        return current_inventory
        
    def check_inventory(self, bike):
        if self.inventory[bike] != 0:
            return True
        else:
            return False
        
    def markup(self, c):
        price = c * self.perc_markup + c 
        return price
        
    def transaction_profit(self, sale):
        self.tprofit = self.markup(sale) - sale 
        print("AX Bicycles made a profit of ${}".format(self.tprofit))
        
    def store_profit(self, sale):
        self.sprofit += self.markup(sale) - sale
        print("Total Sales for the day ${}\n".format(self.sprofit))
        
    def remove_inventory(self, bike):
        self.inventory[bike] -= 1
            
        
class Customer():
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bike_budget = []
        self.customer_options = []
        self.customer_selection = None
        self.sold = None
        
    def budget(self, bicycle, shop):
        if shop.markup(bicycle.price) <= self.money:
            self.bike_budget.append(bicycle)
            
    def selection(self):
        print("Here are the bicycles that are in your budget.")
        for bicycle in self.bike_budget:
            self.customer_options.append(bicycle.model)
        return self.customer_options
        
    def purchase(self, shop, bike):
        while True:
            
            bike1 = bike[0]
            bike2 = bike[1]
            bike3 = bike[2]
            bike4 = bike[3]
            bike5 = bike[4]
            bike6 = bike[5]
            
            self.customer_selection = input("Please select the bike that you would like to purchase. ")
            self.customer_selection = self.customer_selection.upper()
        
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
            
            if shop.check_inventory(self.sold):
                if self.sold.price < self.money:   
                    print("\n")    
                    print("{name} you have purchase the {model} for ${price}. You have ${remaining} remaining in your wallet!\n".format(name=self.name, model=self.sold.model, price=shop.markup(self.sold.price), remaining=self.money-shop.markup(self.sold.price)))
                    
                    shop.remove_inventory(self.sold)
                    shop.transaction_profit(self.sold.price)
                    shop.store_profit(self.sold.price)
                    return
                else:
                    print("You have selected a bicycle that is out side your price range.")
                    continue
            else: 
                print("We no longer have that in stock! Please select one that we have in stock.")

    

    
    