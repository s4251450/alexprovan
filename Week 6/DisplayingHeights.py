class DisplayingHeights:
    @staticmethod
    def main():
        heights = []
        for i in range(5):
            height = int(input("Height: "))
            heights.append(height)
        for height in heights:
            print("Height is " + str(height) + "cm")



DisplayingHeights.main()