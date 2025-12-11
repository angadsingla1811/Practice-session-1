# Enhancing with discount and conditional statements
Discount = True
discount_value = 0
name = (input("Hello sir. What's your name?"))
if (Discount):
    print("Hi", name ,". Today is your lucky day. We have a discount on sandwiches and juices!!")
    discount_value = 0.10
else:
    print("Sorry. We have nothing special today!!")
print("We have two items, sandwich and juice.")
print("The sandwich costs 50.5 rupees and the juice costs 40.5 rupees")
sandwich = int(input("How many sandwiches would you like to eat:"))
juice = int(input("How many juices would you like to drink:"))
total = sandwich * 50.5 + juice * 40.5
total_with_discount = total - (discount_value * total)
print("Hey", name,"your bill costs:", total_with_discount)