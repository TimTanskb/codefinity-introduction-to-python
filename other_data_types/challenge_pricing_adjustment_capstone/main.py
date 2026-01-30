grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

Eggs_price = grocery_inventory.get("Eggs")
#print(Eggs_price)
#print(Eggs_price[2])
if Eggs_price[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": (Eggs_price[0], Eggs_price[1] - 1.00, Eggs_price[2])})
else:
    print("The price of Eggs is reasonable")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

Milk_stock = grocery_inventory.get("Milk")
if Milk_stock[2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": (Milk_stock[0], Milk_stock[1], Milk_stock[2] + 20)})
else:
    print("Milk has sufficient stock.")

Apples_price = grocery_inventory.get("Apples")
if Apples_price[1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)