n = int(input("Enter an odd number: "))

if n < 3 or n % 2 == 0:
    print("Enter an odd number greater than 2")
else:
    for i in range(n):
        spaces = abs(n // 2 - i)

        if i == n // 2:
            print("*" * n)
        elif i == 0 or i == n - 1:
            print(" " * (n // 2) + "*")
        else:
            inner = n - 2 * spaces - 2
            print(" " * spaces + "*" + " " * inner + "*")