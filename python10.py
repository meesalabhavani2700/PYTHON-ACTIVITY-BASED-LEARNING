prepared = [100, 120, 90]
served = [90, 100, 85]

total_waste = 0

for i in range(len(prepared)):
    waste = prepared[i] - served[i]
    percentage = waste / prepared[i] * 100
    total_waste += waste

    print("Day", i + 1)
    print("Leftovers:", waste)
    print("Waste percentage:", round(percentage, 2), "%")

    if percentage > 10:
        print("High food waste")

print("Total leftovers:", total_waste)