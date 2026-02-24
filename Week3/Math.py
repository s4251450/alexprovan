class Math:
        @staticmethod
        def main():
            firstNumber = float(input("First Number: "))
            secondNumber = float(input("Second Number: "))

            sum = firstNumber + secondNumber
            difference = firstNumber - secondNumber
            product = firstNumber * secondNumber
            quotient = firstNumber / secondNumber

            print(f"The sum of {firstNumber} and {secondNumber} is {sum}")
            print(f"The difference of {firstNumber} and {secondNumber} is {difference}")
            print(f"The product of {firstNumber} and {secondNumber} is {product}")
            print(f"The quotient is {quotient:.2f}")


Math.main()