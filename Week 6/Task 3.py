class Task3:
    @staticmethod
    def main():
        names = []
        for i in range(4):
            name = input("Enter a name: ")

            names.append(name)
        targetName = input("What name do you want to search for: ")
        for name in names:
            print(f"Name: {name}")
            if targetName in names:
                found = True
            else:
                found = False




        if found == True:
            print(f"Target found. \n{targetName} Index: {names.index(targetName)}")
        else:
            print(f"Target({targetName}) not found")

Task3.main()