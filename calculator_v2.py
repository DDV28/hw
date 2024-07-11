import math

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Error! Division by zero."

    def sqrt(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error! Cannot take the square root of a negative number."

    def exponent(self):
        return self.x ** self.y

    def run(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exponent")

        while True:
            choice = input("Enter choice (1/2/3/4/5/6): ")

            if choice in ('1', '2', '3', '4', '5', '6'):
                if choice == '5':
                    num = float(input("Enter number: "))
                    print(f"The result is: {self.sqrt(num)}")
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    calc = Calculator(num1, num2)

                    if choice == '1':
                        print(f"The result is: {calc.add()}")
                    elif choice == '2':
                        print(f"The result is: {calc.subtract()}")
                    elif choice == '3':
                        print(f"The result is: {calc.multiply()}")
                    elif choice == '4':
                        print(f"The result is: {calc.divide()}")
                    elif choice == '6':
                        print(f"The result is: {calc.exponent()}")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")

Calculator.run(Calculator)
