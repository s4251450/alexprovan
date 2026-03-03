class InfringementNotices:
    @staticmethod
    def main():
     try:
        exceedingSpeedLimit = int(input("Enter the exceeding speed limit (in km/h): "))
        if 20<= exceedingSpeedLimit <=24:
            zone = int(input("Enter the zone number: "))
            if zone == 110:
                print("The penalty for being in between 20km/h and 24km/h in a 110km zone is 370$ and an automatic license suspension of 3 months.")

        elif exceedingSpeedLimit < 10:
            penalty = 231
            demeritPoints = 1
            print(f"The penalty for being less then 10km/h over the speed limit is a fine of {penalty}$ and {demeritPoints} demerit point")

        elif exceedingSpeedLimit <= 24:
            penalty = 370
            demeritPoints = 3
            print(f"The penalty for being in between 10km/h and 24km/h over the speed limit is a fine of {penalty}$ and {demeritPoints} demerit point")
        elif exceedingSpeedLimit <= 29:
            penalty = 509
            licenseSuspension = 3
            print(f"The penalty for being in between 25km/h and 29km/h over the speed limit is a fine of {penalty}$ and an automatic license suspension of {licenseSuspension} months.")
        elif exceedingSpeedLimit <= 34:
            penalty = 601
            licenseSuspension = 3
            print(f"The penalty for being in between 30km/h and 34km/h over the speed limit is a fine of {penalty}$ and an automatic license suspension of {licenseSuspension} months.")
        elif exceedingSpeedLimit <= 39:
            penalty = 693
            licenseSuspension = 6
            print(f"The penalty for being in between 35km/h and 39km/h over the speed limit is a fine of {penalty}$ and an automatic license suspension of {licenseSuspension} months.")
        elif exceedingSpeedLimit <= 44:
            penalty = 786
            licenseSuspension = 6
            print(f"The penalty for being in between 40km/h and 44km/h over the speed limit is a fine of {penalty}$ and an automatic license suspension of {licenseSuspension} months.")
        elif exceedingSpeedLimit >= 45:
            penalty = 925
            licenseSuspension = 12
            print(f"The penalty for being 45km/h or over 45km/h of the speed limit, there is a fine of {penalty}$ and an automatic license suspension of {licenseSuspension} months.")
        else:
            print("You have entered an invalid input.")
     except ValueError:
         print("Invalid input. Please enter an integer")



InfringementNotices.main()
