# Exercise 2 Shopping Cart Program
from main import quantity

item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like?"))
total = price * quantity

print(f"you have bought {quantity} X {item}/s")
print(f"Your total is ${total}")