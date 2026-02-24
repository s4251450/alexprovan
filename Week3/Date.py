class Date:
    @staticmethod
    def main():
        day = str(input("Please enter a day of the week: ")).capitalize()
        month = str(input("Please enter a month of the year: ")).capitalize()
        date = int(input("Please enter a date: "))
        year = int(input("Please enter a year: "))
        if date == 1:
            print(f"The American Formatted date is {day} {month} {date}st {year}")
            print(f"The European Formatted date is {day} {date}st {month} {year}")
            print(f"The Japanese Formatted date is {year} {month} {date}st {day}")
        elif date == 2:
            print(f"The American Formatted date is {day} {month} {date}nd {year}")
            print(f"The European Formatted date is {day} {date}nd {month} {year}")
            print(f"The Japanese Formatted date is {year} {month} {date}nd {day}")
        elif date == 3:
            print(f"The American Formatted date is {day} {month} {date}rd {year}")
            print(f"The European Formatted date is {day} {date}rd {month} {year}")
            print(f"The Japanese Formatted date is {year} {month} {date}rd {day}")
        elif date >=4:
            print(f"The American Formatted date is {day} {month} {date}th {year}")
            print(f"The European Formatted date is {day} {date}th {month} {year}")
            print(f"The Japanese Formatted date is {year} {month} {date}th {day}")
Date.main()