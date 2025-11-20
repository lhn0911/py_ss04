products = {"A": 120, "B": 80, "C": 300, "D": 50}

# 1. Kiểm tra sản phẩm "A"
if "A" in products:
    print("Sản phẩm A tồn tại, giá:", products["A"])
else:
    print("Sản phẩm A đã bị xóa")

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]))

print(sorted_products)

total_value = sum(products.values())
print(total_value)

for key in list(products.keys()):
    if products[key] > 200:
        del products[key]

print(products)
