"""EX02 - Chardle - A cute step toward wordle."""

__author__ = "730398449"


def main() -> (
    None
):  # I believe the main function is always defined at the beginning of code
    contains_char(
        word=input_word(), letter=input_letter()
    )  # this function call contains functions within itself that work from the inside out and ends with putting the inputs from the functions in the parameters into contains_char


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return word
    else:
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if (
        len(letter) != 1
    ):  # length of letter function is important to eventually look for specific chars with using index function
        print("Error: Character must be a single character.")
        exit()
    else:  # there is only an else and if statement requires here no elif, there are only 2 outputs
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if (
        letter == word[0]
    ):  # these series of if statements are necessary in order to account for each of the possible matches, which increases the count up to 4
        count += 1
        print(letter + " found at index 0")
    if letter == word[1]:
        count += 1
        print(letter + " found at index 1")
    if letter == word[2]:
        count += 1
        print(letter + " found at index 2")
    if letter == word[3]:
        count += 1
        print(letter + " found at index 3")
    if letter == word[4]:
        count += 1
        print(letter + " found at index 4")
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    elif (
        count == 1
    ):  # I added this after realizing it was missing since a match/ word count of 1 had not been accounted for
        print(
            "1 instance of " + letter + " found in " + word
        )  # always make sure the spacing and syntax is correct for print statements
    else:
        print(
            "No instances of " + letter + " found in " + word
        )  # make sure there are only quotations around what need them, in order to have this concatenate properly


if __name__ == "__main__":
    main()
