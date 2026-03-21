class Question3:
    @staticmethod
    def main():

        amount = int(input("How many items would you wish to purchase: "))
        subTotal = 0
        #Iterating through the amount to get prices and adding each price to subtotal then calculating final cost
        #Name: Alexander Provan, ID s4251450
        for i in range(amount):
            item = float(input("Price of item: "))
            subTotal += item
        gst = 0.1 * subTotal
        finalTotal = gst + subTotal
        print(f"Total prices entered: {amount} \nGST: {gst} \nTotal: {finalTotal}")


Question3.main()
