from datetime import datetime
class Task7:
    @staticmethod
    def main():


        #Store details
        storeName = "Woolworth's"
        address = "44 Main Street"
        contactNumber = "1300 1210 1678"

        #Transaction details
        title = "TAX INVOICE"
        date = datetime.now()
        dateFormat = date.strftime("%d/%m/%Y")

        #First item
        firstItem = "Milk"
        firstItemPrice = 5

        #Second item
        secondItem = "Just Right"
        secondItemPrice = 8

        #Third item
        thirdItem = "Butter"
        thirdItemPrice = 4

        #Calculated Costs
        addedPrice = firstItemPrice + secondItemPrice + thirdItemPrice
        GST = 0.1
        totalGST = addedPrice * GST
        totalPrice = addedPrice + totalGST



        #Creating Invoice
        print("=" * 50)
        print(storeName)
        print(address)
        print(contactNumber)
        print("="*50)
        print(title)
        print("Date of transaction: " + str(dateFormat))
        print("-"*50)
        print(firstItem + " " + str(firstItemPrice) + "$")
        print(secondItem + " " + str(secondItemPrice) + "$")
        print(thirdItem + " " + str(thirdItemPrice) + "$")
        print("-" *50)
        print("Price Without GST: " + str(addedPrice) + "$")
        print("GST: 10%")
        print("Total price including GST: " + str(totalPrice))




#Initiate Main Method
Task7.main()