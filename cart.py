foods = []
prices = []
Total = 0

while True:
    food = input("Enter a food to buy or q to quit: ")
    if food.lower() == "q":
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(price)
print("_______Your Cart______")
for food in foods:
    print(food.title(), end=" ")
for price in prices:
    Total += int(price)

print()
print(f"Your total amount is : ${Total}")
