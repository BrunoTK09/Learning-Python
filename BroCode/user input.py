#input() = A function that prompts the user to enter data
#          Return the entered data as string

name = input("What is your name? ")
age = int(input("How old are you? "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")