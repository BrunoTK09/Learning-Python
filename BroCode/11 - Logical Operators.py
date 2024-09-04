#   Logical operators = evaluate multiple conditions (or, and, not)
#                       or  = at least one condition must be True
#                       and = bot conditions must be True
#                       not = inverts the condition (not False, not True)

'''temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")'''

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It's HOT outside 🥵")
    print("It's SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It's HOT outside 🥶")
    print("It's SUNNY ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It's WARM outside 😊")
    print("It's SUNNY ☀️")

    if temp >= 28 and not is_sunny:
        print("It's HOT outside 🥵")
        print("It's CLOUDY ☀️")
    elif temp <= 0 and not is_sunny:
        print("It's HOT outside 🥶")
        print("It's CLOUDY ☀️")
    elif 28 > temp > 0 and not is_sunny:
        print("It's WARM outside 😊")
        print("It's CLOUDY ☀️")