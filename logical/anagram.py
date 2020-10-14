class AnagramDetection:
    
    # Convert upper case
    def toUpper(self, word):
        return word.upper()

    # Remove space if any
    def removeSpace(self, word):
        try:
            return word.replace(' ','')
        except AttributeError:
            return word

    #will return sorted list 
    def sortWord(self, word):
        return sorted(word)

   
    def isAnagram(self, first_word, second_word):
        try:
            # Convert word to upper case
            upper_first_word = self.toUpper(first_word)
            upper_second_word = self.toUpper(second_word)
            # Remove all space if any
            first_without_space = self.removeSpace(upper_first_word)
            second_without_space = self.removeSpace(upper_second_word)
            # Sort word and get list
            sorted_first_word = self.sortWord(first_without_space)
            sorted_second_word = self.sortWord(second_without_space)
            # If both list are equal return True else False
            return sorted_first_word == sorted_second_word
        except Exception as e:
            return e

if __name__ == "__main__":
    first_word = input("First word :")
    second_word = input("Second word :")
    anagram = AnagramDetection().isAnagram(first_word, second_word)
    print(anagram)