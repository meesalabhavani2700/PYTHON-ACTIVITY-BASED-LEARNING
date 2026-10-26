marks = [
    [80, 75, 90],
    [70, 85, 80],
    [95, 90, 88]
]

names = ["Asha", "Ravi", "Priya"]
totals = []

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])
    totals.append(total)

    print(names[i], "Total:", total)
    print("Average:", average)

top = totals.index(max(totals))
print("Top student:", names[top])