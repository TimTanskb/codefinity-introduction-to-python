produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]
#print(groceries)

for section in range(len(groceries)):
    for item in range(len(groceries[section])):
        print("Item name: ", groceries[section][item])