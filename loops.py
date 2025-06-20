#For loops

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
numbers = [1, 4, 24, 7, 60]
for number in numbers:
    print(number)
    
#While loops[using a while loop to count from 1 to 5]

count = 1
while count <= 5:
    print(count)
    count += 1      #Increments the count by 1
    
    
#Loops Control Statements[For loops]

fruits = ["orange", "grapes", "lemon", "pineapple", "stars"]
for fruit in fruits:
    if fruit == "pineapple":
        break
    print(fruit)    #Exits the loop if pineapple is found

print()

for fruit in fruits:
    if fruit == "pineapple":
        continue    #Skips the pineapple variable and moves to the iteration
    print(fruit) 
       
print()

for fruit in fruits:
    if fruit == "pineapple":
        pass        #Placeholder, no action is needed for pineapple
    print(fruit) 
    
#While loops conditional statements

count = 0
while count <= 5:
    print(count)
    count += 1 
    if count == 4:
        break     #Exits the loop when the count reached, in this case the count is 4  