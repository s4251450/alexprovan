class StringExercise:
    @staticmethod
    def main():
        sentence = "I am a student of RMIT"
        capitalizedSentence = "This is sentence will be Capitalized"
        print(capitalizedSentence)
        print(capitalizedSentence.capitalize())
        caseFoldSentence = "This SEntence will Be REDUCED to lower cASE"
        print(caseFoldSentence)
        print(caseFoldSentence.casefold())
        lowerCaseSentence = "This is the sAME THING but only for english"
        print(lowerCaseSentence)
        print(lowerCaseSentence.lower())
        swapCaseSentence = "This is the SWAP caSE it becomes swapped caSE"
        print(swapCaseSentence)
        print(swapCaseSentence.swapcase())
        titleSentence = "This is tHE TItLE SenTENCE"
        print(titleSentence)
        print(titleSentence.title())
        upperCaseSentence = "This is upper cASE"
        print(upperCaseSentence)
        print(upperCaseSentence.upper())

StringExercise.main()