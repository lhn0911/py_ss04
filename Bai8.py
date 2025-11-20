products = {"A": 120, "B": 80, "C": 300, "D": 50}

if "A" in products:
    print("Sản phẩm A tồn tại, giá:", products["A"])
else:
    print("Sản phẩm A đã bị xóa")


def get_value(item):
    return item[1]


sorted_products = dict(sorted(products.items(), key=get_value))

print(sorted_products)

total_value = sum(products.values())
print(total_value)

for key in list(products.keys()):
    if products[key] > 200:
        del products[key]

print(products)
