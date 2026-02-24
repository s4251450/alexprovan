class Calculator:
    @staticmethod
    def main():
        total = 0
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        num3 = input("Enter third number: ")
        num4 = input("Enter fourth number: ")
        print(f"Running total: {total}")
        total += int(num1)
        print(f"running total + {num1} is {total}")
        total += int(num2)
        print(f"running total + {num2} is {total}")
        total += int(num3)
        print(f"running total + {num3} is {total}")
        total += int(num4)
        print(f"running total + {num4} is {total}")

Calculator.main()