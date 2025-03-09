def convert(number, choice):
    if choice == "f":
        result = number - 32*(5/9)
    elif choice == "c":
        result = number * (9/5) + 32

        

temperature = float(input("Do you want to convert\na) Fahrenheit to Celsius\nb) or Celsius to Fahrenheit\n>>:"))
number = ("What is the temperature you would like to convert?\n>>")

f_to_c = ["fahrenheit to celcius", "a", "a.", "a)", "A"]
c_to_f = ["celsius to fahrenheit", "b", "B", "b)", "b."]

if temperature in f_to_c:
    convert(number, "f")
elif temperature in c_to_f:
    convert(number, "c")

