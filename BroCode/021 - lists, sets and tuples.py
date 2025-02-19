#   Collection = single "variable" used to store multiple values
#   List       = [] ordered and changeable. Duplicates OK
#   Set        = {} unordered and immutable, but Add/remove OK. NO duplicates
#   Tuple      = () ordered and unchangeable. Duplicates OK. FASTER


                                                #LIST
#fruits = ["apple", "orange", "Banana", "coconut"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#print("apple" in fruits)
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("apple"))
#print(fruits.count("banana"))

#print(fruits[0])

#fruits[0] = "pineapple"
#for fruit in fruits:
#    print(fruit)

                                                #SET
#fruits = {"apple", "orange", "Banana", "coconut", "coconut"}
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()

#print(fruits)
                                                #TUPLE
fruits = ("apple", "orange", "Banana", "coconut", "coconut")
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#print(fruits.index("apple"))
#print(fruits.count("coconut"))
#for fruit in fruits:
#    print(fruit)