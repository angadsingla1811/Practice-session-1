#Price of sandwiches or juice
name = (input("Hello sir. What's your name?"))
print("We have two items, sandwich and juice.")
print("The sandwich costs 50.5 rupees and the juice costs 40.5 rupees")
sandwich = int(input("How many sandwiches would you like to eat:"))
juice = int(input("How many juices would you like to drink:"))
total = sandwich * 50.5 + juice * 40.5
print("Hey", name,"your bill costs:", total)