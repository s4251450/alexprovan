class integerInterval:
    @staticmethod
    def main():
     try:
        lowerLimit = int(input("Enter lower limit: "))
        upperLimit = int(input("Enter upper limit: "))
        integer = int(input("Enter an integer: "))
        if integer < lowerLimit or integer > upperLimit:
            print(f"The integer {str(integer)} is outside the interval ({str(lowerLimit)}, {str(upperLimit)})")
        elif integer > lowerLimit and integer < upperLimit:
            print(f"The {str(integer)} is inside the interval ({str(lowerLimit)}, {str(upperLimit)})")
        else:
            print("You have entered an integer as a limit")
     except ValueError:
         print("Invalid input. Please enter an integer")
integerInterval.main()