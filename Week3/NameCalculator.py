class NameCalculator:
    @staticmethod
    def main():
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name:")
        fullName = firstName + " " + lastName
        print("Hello, my name is " + fullName+".")
NameCalculator.main()