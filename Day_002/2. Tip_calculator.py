print("Welcome to tip calculator")
total_bill = float(input("How much was the bill? $ "))
people = int(input("How many people to split the bill? "))
tip = float(int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 10)
value = (total_bill * tip) / people
print("Each person should pay %s" % value)