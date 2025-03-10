from art import logo

print(logo)

# Function to calculate the highest bid
def highest_bid(bidding_record):
    highest_amount= 0
    winner = ""

    for bidder in bidding_record:

        if bidding_record[bidder] > highest_amount:
            winner = bidder
            highest_amount = bidding_record[bidder]

    print(f"The winner is {winner}, with a bid of {highest_amount}€")


# Create the Action dicitonary
bids = {}

more_bidders = True

while more_bidders:

    # Ask the user for input
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    # Save data into dictionary
    bids[name] = bid

    # Ask if there are new bids to be added
    new_bid = input("Are there any other bidders?\n"
                "Type 'yes' to add a new bidder, type 'no' to continue\n")

    # Clearing the screen
    print("\n" *40)

    if new_bid == "no":
        more_bidders = False

        # Finding the highest bid
        highest_bid(bids)