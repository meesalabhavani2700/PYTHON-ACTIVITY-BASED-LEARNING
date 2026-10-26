balance = float(input("Enter opening balance: "))

amount = float(input("Enter transaction amount: "))
choice = input("Enter D for deposit or W for withdrawal: ")

if amount <= 0:
    print("Invalid amount")
elif choice == "D":
    balance += amount
elif choice == "W" and amount <= balance:
    balance -= amount
else:
    print("Transaction rejected")

print("Final balance:", balance)