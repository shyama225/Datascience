import 1numpy as np

def calculator():
    print("NumPy Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root (applies to both numbers)")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid input.")
        return

    try:
        num1 = float(input("Enter first number: "))
        if choice != '6':
            num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    if choice == '1':
        print(f"Result: {np.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {np.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {np.multiply(num1, num2)}")
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"Result: {np.divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {np.power(num1, num2)}")
    elif choice == '6':
        print(f"Square root of {num1} is: {np.sqrt(num1)}")

if __name__ == "__main__":
    calculator()
