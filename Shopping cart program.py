# shopping cart program
import time

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item(q to quit): ")

    if food == "q"or food == "Q":
        break
    while food == "":
        print("Please enter a food item")
        food = input("Enter food item(q to quit): ")
    else:   
        price = float(input(f"Enter the price of a {food}$: "))

        while price == str("") or price == 0:
            print("Please enter a number")
            price = float(input(f"Enter the price of a {food}$: ")) 
        foods.append(food)
        prices.append(price)

print ("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")
    for price in prices:
        total += price
print()
print(f"Your total is {total}$")
time.sleep(3)
retry = input("Would you like to try again? (y/n): ")
if retry == "y":
    print("close the program") # dont know how to restart this shit :)
else:
    print("goodbye")
    quit()
       