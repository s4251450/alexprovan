class Calculator:
    @staticmethod
    def main():
        total = 0
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        num3 = input("Enter third number: ")
        num4 = input("Enter fourth number: ")



        print(f"Running total is 0")
        total += int(num1)
        print(f"running total: 0 + {num1} is {total}")
        total += int(num2)
        runningTotal = int(num1)
        print(f"running total {runningTotal} + {num2} is {total}")
        total += int(num3)
        runningTotal = int(num1) + int(num2)
        print(f"running total: {runningTotal} + {num3} is {total}")
        total += int(num4)
        runningTotal = int(num1) + int(num2) + int(num3)
        print(f"running total {runningTotal} + {num4} is {total}")


        print(total)

Calculator.main()