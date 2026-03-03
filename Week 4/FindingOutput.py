class FindingOutput:
    @staticmethod
    def main():
        MAX = 25
        LIMIT = 100
        num1 = 12
        num2 = 25
        num3 = 87

        #Task2.1
        if num1 < MAX:
            print("Apple")
        #Output: True


        #Task 2.2
        if num2 <= MAX:
            print("Apple")
            print("Orange")
        #True

        # Task 2.3
        if MAX > num3:
            print("Apple")
            print("Orange")

        #False


        #Task 2.4
        if num3 >= LIMIT:
            print("Apple")
            print("Orange")
            print("Pear")
            #False
        # Task 2.5
        if num2 == MAX:
            print("apple")
      #  print("orange")
      #  print("pear")
        #error indentation otherwise true
        # Task 2.6
        if num3 - num2 > 2 * MAX:
            print("apple")
        else:
            print("orange")
            #apple is true
        # Task 2.7
        if LIMIT + num3 <= 150:
            print("apple")
        #print("orange")
        #indent error
        else:
         print("pear")
        #pear
        # Task 2.8
        if 2 * num1 != num2:
            print("apple")
        else:
            print("orange")

        print("pear")

        #apple is true
        # Task 2.9
        if LIMIT % num1 + 4 == num1 + (MAX - num2):
            print("apple")
            print("orange")
        else:
            print("pear")
        print("banana")
            # Task 2.10
        if num1 < MAX:
            print("banana")
        #False


FindingOutput.main()