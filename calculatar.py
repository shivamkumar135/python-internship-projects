def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    while True:
        print("\n--- Interactive Calculator & Unit Converter ---")
        print("1. Basic Arithmetic (+, -, *, /)")
        print("2. Unit Conversion (Km to Miles, Celsius to Fahrenheit)")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("\nSelect Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            op_choice = input("Choose operation (1/2/3/4): ")
            
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                continue
                
            if op_choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif op_choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif op_choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif op_choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operation choice!")
                
        elif choice == '2':
            print("\nSelect Conversion:")
            print("1. Kilometers to Miles")
            print("2. Celsius to Fahrenheit")
            
            conv_choice = input("Choose conversion (1/2): ")
            
            try:
                val = float(input("Enter value to convert: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
                
            if conv_choice == '1':
                print(f"Result: {val} km = {km_to_miles(val):.2f} miles")
            elif conv_choice == '2':
                print(f"Result: {val}°C = {celsius_to_fahrenheit(val):.2f}°F")
            else:
                print("Invalid conversion choice!")
                
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()