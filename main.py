from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}

ok = True

while ok:
  name = input("What is your name? ")
  bid = float(input("What is your bid? "))

  bids[name] = bid

  play = input("Are there anymore bidders? Y or N:")

  if play.upper() == "Y":
    clear()

  elif play.upper() == "N":
    ok = False


winning_bid = max(bids.values())

for i in bids.keys():
  if bids[i] == winning_bid:
    bidder = i


print(f"The winner is {bidder} with a bid of {winning_bid}.")