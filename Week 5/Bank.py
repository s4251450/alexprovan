class Bank:
    @staticmethod
    def main():
        balance = 300

        while balance > 0:
           try:
            withdrawAmount = int(input("Enter withdraw amount: "))
            if withdrawAmount < balance:
                balance -= withdrawAmount
                print("Congratulations your new balance is: " + str(balance) + "$")
            elif withdrawAmount == balance:
                balance -= withdrawAmount
                print("Poor you, your closing balance is: " + str(balance) + "$")
            elif withdrawAmount > balance:
                withdrawAmount -= balance
                print("Sorry, withdrawal disallowed as it would over spend your account by: " + str(abs(withdrawAmount)) + "$")
            else:
                print("Something went wrong, try again")
           except ValueError:
               print("Something went wrong, try again")






Bank.main()