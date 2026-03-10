class Calculator:
    @staticmethod
    def main():
        total = 0

        for i in range(0, 4):
            n = int(input("Enter a number: "))
            total += n
            print(total)
        print("Total is " + str(total))





Calculator.main()