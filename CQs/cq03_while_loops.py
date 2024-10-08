"""CQ03 While Loop."""

__author__ = "730398449"


def num_instances(phrase: str, search_char: str) -> int:
    """Character matching While Loop."""
    count: int = 0
    index: int = 0  # this assures that the index and count values begin with 0
    while index < len(
        phrase
    ):  # in order for the loop to keep running this would continue to be true until false, then the loop would end
        if (
            phrase[index] == search_char
        ):  # matching of the index character with the one you ate searching for
            count = (
                count + 1
            )  # in order for the loop to not be infinate ther ehas to be a +1 to the index and count to eventually result as false
        index = index + 1
    return count
