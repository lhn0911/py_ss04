products = {"A": 120, "B": 80, "C": 300, "D": 50}

for key in list(products.keys()):
    if products[key] < 100:
        del products[key]

print(products)
products["E"] = 200
print(products)
count_products = len(products)
print(count_products)
