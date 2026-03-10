class HighestScore:
    @staticmethod
    def main():
        try:
         students = int(input("Enter number of students: "))

         for student in range(students):
            grade = int(input(f"Enter grade for student no. {student + 1}: "))
            if grade > 100:
                print("Grade is higher than 100")
                break
            elif grade < 0:
                print("Grade is lower than 100")
                break
            elif student == 0:
                bestStudent = student
                highestScore = grade
            elif student >= 1:
                if grade > highestScore:
                    bestStudent = student
                    highestScore = grade





            print(f"Student No. {student + 1} Grade: {grade}%")

         print(f" The top scorer was Student No. {bestStudent + 1} with the highest grade of: {highestScore}%")
        except:
         print("Something went wrong :(")

HighestScore.main()