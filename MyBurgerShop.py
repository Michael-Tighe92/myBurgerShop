# implement the classes listed below 

class Order:
    def __init__(self):
        self.totalPrice = 0
        self.Orders = []
    def addPrice (self,p):
        self.totalPrice += p
    def displayPrice (self):
        print(self.totalPrice)
    def addOrder (self,o):
        self.Orders.append(o)
    def displayOrders (self):
        for i in range (len(self.Orders)):
            print(self.Orders[i])

 
def user_input_burger(obj):
    inProcess = True
    while inProcess == True:
        print("What condiment do you want with your burger? ")
        print("1.) Ketchup")
        print("2.) Mayo")
        print("3.) None")
        userChoice = input("Please choose from one of these options! ")
        if userChoice == '1':
            inProcess = False
            obj.addOrder("Burger w/ Ketchup")
            obj.addPrice(5)
        elif userChoice == '2':
            inProcess = False
            obj.addOrder("Burger w/ Mayo")
            obj.addPrice(6)
        elif userChoice == '3':
            obj.addOrder("Burger w/o Condiment")
            obj.addPrice(4.50)
            inProcess = False
        else:
            print("You need to choose from one of the options listed!")
    
     
def user_input_drink(obj):
    inProcess = True
    while inProcess == True:
        print("What size do you want with your drink? ")
        print("1.) Small")
        print("2.) Medium")
        print("3.) Large")
        userChoice = input("Please choose from one of these options! ")
        if userChoice == '1':
            inProcess = False
            obj.addOrder("Small Soda")
            obj.addPrice(1.75)
        elif userChoice == '2':
            inProcess = False
            obj.addOrder("Medium Soda")
            obj.addPrice(2.50)
        elif userChoice == '3':
            obj.addOrder("Large Soda")
            obj.addPrice(3.25)
            inProcess = False
        else:
            print("You need to choose from one of the options listed!")
     
def user_input_side(obj):  
    inProcess = True
    while inProcess == True:
        print("What side do you want? ")
        print("1.) Salad")
        print("2.) Fries")
        print("3.) Onion Rings")
        userChoice = input("Please choose from one of these options! ")
        if userChoice == '1':
            inProcess = False
            obj.addOrder("Salad")
            obj.addPrice(2.50)
        elif userChoice == '2':
            inProcess = False
            obj.addOrder("Fries")
            obj.addPrice(3)
        elif userChoice == '3':
            obj.addOrder("Onion Rings")
            obj.addPrice(3.25)
            inProcess = False
        else:
            print("You need to choose from one of the options listed!")
     
def user_input_combo(obj):
    user_input_burger(obj)
    user_input_side(obj)
    user_input_drink(obj)
    
     
def take_order():
    o = Order() 
    inOrder = True
    orderisDone = False
    #ask user for name for the order
    userName = input("Please enter your name: ")
    #repeat taking order until client is done
    while inOrder == True:
        print("Hello " + userName + "! What do you want to order?")
        print("1.) Burger")
        print("2.) Side")
        print("3.) Drink")
        print("4.) Combo")
        print("5.) Finish Order")
        print("6.) Cancel Order")
        userInput = input("Please choose from one of these options! ")
        if userInput == '1':
            user_input_burger(o)
        elif userInput == '2':
            user_input_side(o)
        elif userInput == '3':
            user_input_drink(o)
        elif userInput == '4':
            user_input_combo(o)
        elif userInput == '5':
            print("You have finished your order!")
            print("Processing the order details...")
            inOrder = False
            orderisDone = True
        elif userInput == '6':
            print("You have canceled your order!")
            inOrder = False
        else:
            print("You need to choose from one of the options listed in the menu!")
    #display order details
    if orderisDone == True:
        print("Displaying order details...")
        print("Your orders are: ")
        o.displayOrders()
        print("Your total is: ")
        o.displayPrice()
    #display a thank you message
    print("Thank you for choosing Burger Shop " + userName + "!")
        
print("Welcome to Burger Shop")
take_order()