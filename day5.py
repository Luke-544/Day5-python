#while loops
#let's create a simple while loop first

while 1==1:
    print("Help me!")

#let's now look into a more detailed loop
name =""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)
print("Your out of the loop")

#There is another way of writing the code above
name = None
while not name:
    name = input("Enter your name: ")

print("Hello "+name)
print("You made it out of the loop!")

