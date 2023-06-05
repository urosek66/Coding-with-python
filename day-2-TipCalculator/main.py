# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
tip_number = bill * (tip / 100)
bill = bill + tip_number
people = int(input("How many people to split the bill? "))
bill = bill / people
# total_bill = round(bill, 2)
total_bill = "{:.2f}".format(bill)
message = f"Each person should pay: ${total_bill}"
print(message)
