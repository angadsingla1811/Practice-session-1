#HW - Homework Activity : Movie Ticket Bill
"""
•	Ask the user:
•	Price of 1 movie ticket
•	Number of people
•	Price of popcorn
•	Number of popcorns
•	Apply 10% discount if people > 4
•	Add 18% GST at the end
•	Print final bill
"""

print("Hello Sir/Madam. Today I am your movie manager.")
price_mov_tick = float(input("How much is the price of one movie ticket:"))
people_go = float(input("How many people are going:"))
price_pop = float(input("What is the price of 1 popcorn:"))
num_pop = float(input("How many popcorns will you buy:"))
if (people_go):
    Discount = True
    disc_value = 0.10
    GST_value = 0.18
    print("Because 4 or more than 4 people are going you get a 10% discount!")
total = price_mov_tick * people_go + price_pop * num_pop
total_with_discount = total - (disc_value * total)
total_with_GST = total_with_discount + (GST_value * total_with_discount)
print("So your bill adss up to:", total_with_GST)