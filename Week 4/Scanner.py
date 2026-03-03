class Scanner:
    @staticmethod
    def main():
     try:
        averageWeight = int(input("Average Egg Weight(g): "))
        if averageWeight < 43:
            size = "Too Small"
            print(size)
        elif averageWeight <= 51:
            size = "Medium"
            print(size)
        elif averageWeight <= 59:
            size = "Large"
            print(size)
        elif averageWeight <= 67:
            size = "Extra-Large"
            print(size)
        elif averageWeight <= 72:
            size = "Jumbo"
            print(size)
        elif averageWeight > 72:
            size = "King-Size"
            print(size)
     except ValueError:
         print("Invalid input. Please enter an integer")

Scanner.main()