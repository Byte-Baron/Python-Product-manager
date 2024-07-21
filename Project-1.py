
product01 =input("Enter the first product name :")
number01=int(input("Enter the Number of "+product01+": "))

product02 =input("Enter the second product name :")
number02=int(input("Enter the Number of "+product02+": "))

product03 =input("Enter The third product name :")
number03=int(input("Enter the Number of "+product03+": "))

print("\n")
print ("You have :",number01,product01," ",number02,product02," &",number03,product03)

'''
products = {}

while True:
    print("1. Add product")
    print("2. Sell product")
    print("3. View products")
    print("4. Quit")

    action = input("What would you like to do? ")

    if action == "1":
        name = input("Enter the name of the product: ")
        quantity = int(input("Enter the quantity of the product: "))
        products[name] = products.get(name, 0) + quantity
    elif action == "2":
        name = input("Enter the name of the product: ")
        quantity = int(input("Enter the quantity to sell: "))
        if products.get(name, 0) >= quantity:
            products[name] = products.get(name, 0) - quantity
        else:
            print("Not enough products available.")
    elif action == "3":
        for product, quantity in products.items():
            print(f"{product}: {quantity}")
    elif action == "4":
        break
'''
