class SalaryCalculator:
    @staticmethod
    def main():
        representativeName = input("Please enter your representative name: ")
        try:
         weeklySales = int(input("Please enter your weekly sales: "))
        except ValueError:
            print("Invalid Input. Please enter an integer")
        salary = 200

        commissions = weeklySales-200
        if commissions > 0:
            salary += commissions * 0.05


        if weeklySales > 2000:
            salary += 50
        print(f"{representativeName}'s Salary is {salary}$")

SalaryCalculator.main()