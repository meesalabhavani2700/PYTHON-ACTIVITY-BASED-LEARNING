products = [
    ("Pen", 10, 5),
    ("Book", 50, 3),
    ("Bag", 500, 12)
]

for name, price, quantity in products:
    value = price * quantity

    print("Product:", name)
    print("Stock value:", value)

    if quantity < 10:
        print("Reorder quantity:", 10 - quantity)
    else:
        print("Stock sufficient")