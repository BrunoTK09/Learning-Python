# Typecasting = the process of converting a variable from one data to another
#               str(), int(), float(), bool()

name = "Bro Code"
age = 21
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print("======================================================================================================")
gpa = int(gpa)
print(gpa)

#print("======================================================================================================")
#age = float(age)
#print(age)

print("======================================================================================================")
age = str(age)
print(age)
print(type(age))

print("======================================================================================================")
age = str(age)
age += "1"
print(age)

print("======================================================================================================")
name = bool(name)
print(name)