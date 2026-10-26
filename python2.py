attended = int(input("Classes attended: "))
total = int(input("Total classes: "))

if total == 0 or attended < 0 or attended > total:
    print("Invalid input")
else:
    percentage = attended / total * 100
    print("Attendance:", percentage, "%")

    extra = 0
    while (attended + extra) / (total + extra) * 100 < 75:
        extra += 1

    print("Extra classes needed:", extra)