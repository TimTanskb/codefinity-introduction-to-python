# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
index = 0
print("Processing started")
for item in inventory.values():
    product = list(inventory.keys())
    print("Processing", product[index])
    index += 1
    while item[0] < item[1]:
        item[0] += item[2]
        #print(inventory)
        if item[0] > discount_threshold:
            item[3] = True

print("Processing completed")
            