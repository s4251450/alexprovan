class Question4:
    @staticmethod
    def main():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        total = num1 + num2


        #having the loop run through the program for the user to keep guessing the total
        #Using selection nested in an iteration to determine if the users guess matches the total or in range of the total
        #Name: Alexander Provan, ID: s4251450
        while True:
            guess = int(input(f"What is {num1} + {num2}? "))
            if guess == total:
                print(f"\033[92mCorrect!\033[0m")
                break
            elif guess < total -5 or guess > total +5:
                print(f"\033[91mYou are more than 5 off the answer\033[0m")
            elif guess > total or guess < total:
                print(f"\033[93mYou are between -5 and +5 from the answer\033[0m")

Question4.main()