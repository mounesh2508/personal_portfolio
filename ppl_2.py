invent = {}
def add_pro():
    pro = input("Product name: ").lower()
    if pro in invent:
        print("Product exists. Use update option.")
        return
    qty = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    invent[pro] = {"qty": qty, "price": price}
    print(pro," Product is added.")
def update_pro():
    pro = input("Product name to update: ").lower()
    if pro not in invent:
        print("Product not found.")
        return
    qty = int(input("New quantity: "))
    price = float(input("New price : "))
    invent[pro].update({"qty": qty, "price": price})
    print("Product updated.")
def search_pro():
    pro = input("Product name to search: ").lower()
    if pro in invent:
        d = invent[pro]
        print(f"{pro.title()} - Qty: {d['qty']}, Price: {d['price']}")
    else:
        print("Product not found.")  
def display_invent():
    print("\nCurrent Inventory:")
    if not invent:
        print("Inventory is empty.")
        return
    print(f"{'Product':<15}{'Qty':<10}{'Price':<10}")
    for pro, details in invent.items():
        print(f"{pro:<15}{details['qty']:<10}{details['price']:<10}")
while True:
    print("\nPocket Bazaar - Grocery Inventory")
    print("1. Add Product\n2. Update Product\n3. Display Inventory\n4. Search Product\n5. Exit")
    choice = input("Choose (1-5): ")
    if choice == "1":
        add_pro()
    elif choice == "2":
        update_pro()
    elif choice == "3":
        display_invent()
    elif choice == "4":
        search_pro()
    elif choice == "5":
        print("Good bye!")
        break
    else:
        print("Invalid choice. Try again.")
