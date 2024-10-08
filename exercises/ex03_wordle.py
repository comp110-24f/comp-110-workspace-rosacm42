"""Wordle Exercise"""

___author___ = 730398449


def input_guess(guess_length: int) -> str:
    word: str = input(f"Enter a {guess_length} character word: ")
    while len(word) != guess_length:
        word: str = input(f"That wasn't {guess_length} chars! Try again: ")
    return word


def contains_char(word_search: str, single_character_search: str) -> bool:
    """Contains_char searches match of a single character withina word."""
    assert len(single_character_search) == 1
    index = 0
    while index < len(word_search):
        if word_search[index] == single_character_search:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    "Compare guess word with secret word."
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    index = 0
    s = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            s += GREEN_BOX
        elif contains_char(word_search=secret, single_character_search=guess[index]):
            s += YELLOW_BOX
        else:
            s += WHITE_BOX
        index += 1
    return s


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    index = 1
    while index < 7:
        print("=== Turn " + str(index) + "/6 ===")
        guess = input_guess(len(secret))
        # guess = input_guess(index(guess) = single_character_search)
        print(emojified(guess, secret))
        if guess == secret:
            print(" You won in " + str(index) + "/6 turns! ")
            return  # could use return or return none to end this while loop
        index += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
