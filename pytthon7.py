days = int(input("Enter number of days (28-31): "))
start = int(input("Starting weekday (0=Mon, 6=Sun): "))

if days < 28 or days > 31 or start < 0 or start > 6:
    print("Invalid input")
else:
    print("Mon Tue Wed Thu Fri Sat Sun")
    print("    " * start, end="")

    for day in range(1, days + 1):
        print(f"{day:3}", end="")

        if (start + day) % 7 == 0:
            print()

    if (start + days) % 7 != 0:
        print()