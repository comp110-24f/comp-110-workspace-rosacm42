"""Mutating Functions."""

___author___= 730398449

def manual_append(my_list:list[int], integer:int) -> None: 
    my_list.append(integer)

def double(my_list:list[int]) -> None: 
   index=0
   while index< len(my_list):
       my_list[index]= my_list[index] *2
       index +=1

list_1: list[int]
list_1= [1,2,3]

list_2: list[int]
list_2= list_1

double(my_list=list_2)
print (list_1)
print (list_2)





