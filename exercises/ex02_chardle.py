"""EX02 - Chardle - A cute step toward wordle."""

__author__ = "730398449"

def main() -> None:
    contains_char(word=input_word(), letter=input_letter())

def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5: 
        print("Error: Word must contain 5 characters.")
        exit()
        return word
    else: 
        return word

def input_letter() -> str:
    letter:str = input("Enter a single character: ")
    if len(letter) != 1: 
        print("Error: Character must be a single character.")
        exit()
    else: 
        return letter
    
def contains_char (word:str, letter: str) -> None: 
    print ("Searching for " + letter + " in " + word)
    count: int= 0
    if letter == word[0]: 
        count +=1
        print (letter + " found at index 0")
    if letter == word[1]: 
         count +=1
         print (letter + " found at index 1")
    if letter == word[2]:
        count +=1
        print (letter + " found at index 2")
    if letter == word[3]: 
         count +=1
         print (letter + " found at index 3")
    if letter == word[4]:
        count +=1
        print (letter + " found at index 4")
    if count>1:
         print (str(count) + " instances of " + letter + " found in " + word)
    elif count==1: 
        print ( "1 instance of " + letter + " found in " + word)
    else: 
     print ("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()