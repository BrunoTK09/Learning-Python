# Conditional Expressions = A one-line shortcut for if-else statement (ternary operator)
#                           Print on assign one of two values based on condition
#                           X if condition else Y

num = 5
a = 6
b = 7
age = 21
temperature = 30
user_role = "admin"

#print(X if condition else Y)
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited access"

print(access_level)