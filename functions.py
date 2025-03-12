def greeting():
    print("Ola...soy Dora!")

def greeting_w_name(name):
    print(f"Ola {name}.")

def add(a, b):
    print(a + b)
#add(5, 25)
#add(55, 7)
#add(23, 54)

def minus(a, b):
    print(a - b)

def divide(a, b):
    print(a / b)

def multiply(a, b):
    print(a * b)

operation = input("Which operation do you want to use(+, -, *, /)?")
a = input("Enter your first number: ")
b = input("Enter your second number: ")

if operation == "+":
    add(a, b)
elif operation == "-":
    minus(a, b)
elif operation == "/":
    divide(a, b)
elif operation == "*":
    multiply(a, b)


#minus(34, 4)
#greeting_w_name("Catherine")
#greeting_w_name("Peter Parker")
#greeting_w_name("Spiderman")
#greeting()
