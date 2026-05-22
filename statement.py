balance = 1000
while True:
    print("1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        amount = int(input("Enter amount: "))
        balance += amount
    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance -= amount
    elif choice == 3:
        print("Balance:", balance)
    elif choice == 4:
        break