
fruits = ["apple", "banana", "cherry"]

print(fruits)

print(fruits[0])         #Index/position

fruits[1] = "grapes"

print(fruits)

#Append method for adding items to our list

fruits.append("kiwi")

print(fruits)

fruits.insert(1, "orange")

print(fruits)

#Remove method to remove items to our list

fruits.remove("kiwi")

print(fruits)

#Sort method for sorting items to our list

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)
