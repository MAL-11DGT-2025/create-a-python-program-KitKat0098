print("Hello, world!")
print("My favourite colour is purple")

#This code welcomes a person to wonderland
name = input("What is your name? ")
print(f"Welcome to wonderland {name}!")

#This code asks user for name and calls them old
age = int(input("How old are you? "))
print(f"Wow! {age} is old! You are so very old!")

if age > 25:
    print("You are old")
    #This statement calls the person old if theyre older than 25
if age >= 13 or age <= 19:
    print("You are a teenager")