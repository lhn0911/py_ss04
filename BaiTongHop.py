products = []


def exists(product_id):
    for p in products:
        if p[0] == product_id:
            return True
    return False


def add_product():
    product_id = input("Nhập mã sản phẩm: ")
    if exists(product_id):
        print(" Mã sản phẩm đã tồn tại. Không thể thêm!")
        return

    name = input("Nhập tên sản phẩm: ")
    qty = int(input("Nhập số lượng: "))
    price = float(input("Nhập giá: "))

    product = (product_id, name, qty, price)
    products.append(product)

    print("Thêm sản phẩm thành công!")


def show_products():
    if not products:
        print("Danh sách sản phẩm trống!")
        return

    print("\n--- DANH SÁCH SẢN PHẨM ---")
    for p in products:
        print(f"Mã: {p[0]} | Tên: {p[1]} | Số lượng: {p[2]} | Giá: {p[3]}")
    print("---------------------------\n")


def find_product():
    product_id = input("Nhập mã sản phẩm cần tìm: ")

    for p in products:
        if p[0] == product_id:
            print("Đã tìm thấy sản phẩm:")
            print(f"Mã: {p[0]}, Tên: {p[1]}, SL: {p[2]}, Giá: {p[3]}")
            return

    print("Không tìm thấy sản phẩm!")


def update_product():
    product_id = input("Nhập mã sản phẩm cần cập nhật: ")

    for i, p in enumerate(products):
        if p[0] == product_id:
            print("Nhập thông tin mới:")
            name = input("Tên mới: ")
            qty = int(input("Số lượng mới: "))
            price = float(input("Giá mới: "))

            products[i] = (product_id, name, qty, price)
            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sản phẩm để cập nhật!")


def delete_product():
    product_id = input("Nhập mã sản phẩm cần xóa: ")

    for p in products:
        if p[0] == product_id:
            products.remove(p)
            print("Xóa sản phẩm thành công!")
            return

    print("Không tìm thấy sản phẩm để xóa!")


while True:
    print("\n===== MENU QUẢN LÝ SẢN PHẨM =====")
    print("1. Thêm sản phẩm mới")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Tìm kiếm sản phẩm theo mã")
    print("4. Cập nhật thông tin sản phẩm")
    print("5. Xóa sản phẩm theo mã")
    print("0. Thoát chương trình")
    print("================================")

    choice = input("Chọn chức năng (0-5): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        find_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "0":
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
