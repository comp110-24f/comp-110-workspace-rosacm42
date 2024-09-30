"""EX01- Tea Party"""

__author__: str = "730398449"


def main_planner(guests: int) -> None:
    """Determining the cost of a tea party based on the number of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


# A return function here is not needed since return: none, was stated when defining the function


def tea_bags(people: int) -> int:
    """Address tea bags for each guest."""
    return int(people * 2)


def treats(people: int) -> int:
    """Address the number of guests attending."""
    return int(tea_bags(people=people) * 1.5)


# I was able to apply the tea_bags function here with the appropriate arguments


def cost(tea_count: int, treat_count: int) -> float:
    """Adding the cost of tea bags and treats"""
    return (tea_count) * 0.50 + (treat_count) * 0.75


# Make sure the parameters here match, the outcome is a float not an integer


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
