opening = int(input("Opening stock: "))
received = int(input("Stock received: "))
dispatched = int(input("Stock dispatched: "))
recorded = int(input("Recorded closing stock: "))

expected = opening + received - dispatched

print("Expected stock:", expected)

if expected == recorded:
    print("Stock matches")
else:
    print("Stock discrepancy:", recorded - expected)

if expected < 10:
    print("Replenishment needed:", 10 - expected)