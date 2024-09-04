unit = input("Is tis temperature in Celsius or fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in fahrenheit is: {temp}ºF")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")
