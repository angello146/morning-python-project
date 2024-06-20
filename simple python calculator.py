#A simple python calculator



def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error Division by Zero"
    else:
        return a / b

def calculator(a, b):
    print("select operation")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(add(num1, num2))
        elif choice == "2":
            print(subtract(num1, num2))
        elif choice == "3":
             print(multiply(num1, num2))
        elif choice == "4":
             print(divide(num1, num2))
    else :
       print("Invalid input")

if __name__ == "__main__":
    calculator(1, 2)