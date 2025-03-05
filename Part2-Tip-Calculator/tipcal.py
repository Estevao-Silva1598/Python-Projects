print("Welcome to the tip calculator!")

#Here the program recieves the inputs such as the bill, tip percentage and the number of people
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#Here we calculate the total percentage of how much each people will pay with the tip
percentage = 1.0 + tip / 100

#Now we calculate the total and then we round it to 2 decimal parcels
total = bill * percentage / people
total = round(total, 2)

print(f"Each person should pay: ${total}")