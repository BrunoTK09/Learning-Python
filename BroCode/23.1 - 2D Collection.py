
#fruits =     ["apple", "orange", "banana", "coconut"]
#vegetables = ["celery", "carrots", "potatoes"]
#meats =      ["chicken", "fish", "turkey"]

groceries = [("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "potatoes"),
             ("chicken", "fish", "turkey")]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()