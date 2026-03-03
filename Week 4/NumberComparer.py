class NumberComparer:
    @staticmethod
    def main():
       try:
        value1 = int(input("Please enter a number: "))
        value2 = int(input("Please enter a number: "))
        if value1 > value2:
            print(value1)
        elif value1 < value2:
            print(value2)
        else:
            print("Values are the same")
       except ValueError:
           print("Invalid input")
NumberComparer.main()