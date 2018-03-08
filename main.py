from bicycles import *

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
    
    print("{name}'s budget is ${money}\n".format(name=andrew.name, money=andrew.money))
    for bicycle in shop.show_inventory():
        andrew.budget(bicycle)
    for bike in andrew.selection():
        print(bike)
    andrew.purchase()
    
    print("{name}'s budget is ${money}\n".format(name=ryan.name, money=ryan.money))
    for bicycle in shop.show_inventory():
        ryan.budget(bicycle)
    for bike in ryan.selection():
        print(bike)
    ryan.purchase()
    
    print("{name}'s budget is ${money}\n".format(name=dante.name, money=dante.money))
    for bicycle in shop.show_inventory():
        dante.budget(bicycle)
    for bike in dante.selection():
        print(bike)
    dante.purchase()