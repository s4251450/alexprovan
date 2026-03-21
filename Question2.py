class Question2:
    @staticmethod
    def main():
        temperature = int(input("What is the temperature in celsius: "))
        #using selection to determine what clothes to wear based on the temperature in celsius.
        #name Alexander Provan, ID: s4251450
        if temperature <= 0:
            print("Grab your snow jacket")
        elif temperature <= 10:
            print("Wear some thermals")
        elif temperature <= 20:
            print("Grab a jumper")
        elif temperature <= 30:
            print("Nice weather today. Enjoy the sun.")
        elif temperature > 30:
            if temperature == 35:
                print("Time to go home")
            else:
                print("Wear sunscreen and a hat!")


Question2.main()