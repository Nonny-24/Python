#Strings

message = 'Hello World'
print(message)

message = """Michael's World
is awesome"""
print(message)

#Advanced concepts - Strings

message = 'Hello'   #Index/positions
print(message[0])
print(message[1]) 

print(message[-1])

print(len(message))

message = ' Hello, World! '
print(message.strip())     #Removes leading and trailing whitespaces
print(message.lower())
print(message.split(','))
#Uppercase method
print(message.upper())
#Replace method
print(message.replace('World', 'coders'))
