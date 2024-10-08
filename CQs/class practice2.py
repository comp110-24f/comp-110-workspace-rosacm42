my_numbers: list[float] = []
my_numbers: list[float] = list()

my_numbers.append(1.5)


# make a list fo an item 
game_points: list[int] = [102,86,94]
# print(game_points[2])

# changing value of an item 
game_points[1]=72
# print(game_points)
# print(len(game_points))
game_points.pop(1)
# print(game_points)

# Can we change individual chars on the strings this way? 
my_name: str= "Izzi"
# my_name[3]= "y" # didn't work- convert it 
name_as_list: list[str] = list(my_name)
# print(name_as_list)
name_as_list[3] = "y"
# print (name_as_list)
name_as_list.append("e")
# print (name_as_list)

name_as_list.insert(4,"i")
# print(name_as_list)

grocery_list: list[str] = ["banana", "apple", "carrot"]
grocery_list.append("beans")
print(grocery_list)
grocery_list.pop(1)
print (grocery_list)