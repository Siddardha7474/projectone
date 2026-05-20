a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Choose operation: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid Choice")