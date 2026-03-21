class Task2:
    @staticmethod
    def main():


        numbers = []
        highestNumber = 0
        lowestNumber = 100



        for i in range(4):
            num = int(input("Enter a Number in between 1 and 100: "))
            numbers.append(num)
            if num > highestNumber:
                highestNumber = num
            if num < lowestNumber:
                lowestNumber = num


        targetNumber = int(input("What number will you search for: "))




        for number in numbers:
            print(number)
            if targetNumber in numbers:
                found = True
            else:
                found = False



        print(f"Highest number: {highestNumber}")
        print(f"Lowest number: {lowestNumber}")


        if found == True:
            print(f"Target found. Number: {targetNumber}, Index: {str(numbers.index(targetNumber))} ")
        else:
            print(f"Target({targetNumber}) not found")



Task2.main()