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
print("1 ticket costs 100 rupees")
people_go = float(input("How many people are going:"))
print("1 popcorn costs 50 rupees")
num_pop = float(input("How many popcorns will you buy:"))
if (people_go):
    Discount = True
    disc_value = 0.10
    GST_value = 0.18
    print("Because 4 or more than 4 people are going you get a 10% discount!")
total = 100 * people_go + 50 * num_pop
total_with_discount = total - (disc_value * total)
total_with_GST = total_with_discount + (GST_value * total_with_discount)
print("So your bill adss up to:", total_with_GST)
print("1 Refill available! Have fun and enjoy your movie!!")