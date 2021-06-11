import random

print("Who is going to pay the bill?")
list_name = input("Tell me the names that are going to pay the bill, separated by a coma and a space (, ) ")

names = list_name.split(", ")

number_names = len(names)-1

print(names[random.randint(0,number_names)])
