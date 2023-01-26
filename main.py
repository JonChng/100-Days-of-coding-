############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
from art import logo
from replit import clear



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def hit(hand):
  add_card = random.choice(cards)
  return hand.append(add_card)

def check_hand(hand):
  count = 0

  for i in hand:
    count += i 
  #Checking value of hand
  if count > 21:
    #If value of hand >21, check if hand contains a ace. If True, minus 10 from count to set ace value as 1.
    if 11 in hand:
      ind = hand.index(11)
      hand[ind] = 1
      count -= 10
     
      return count
    else:
      #False for lose
      
      return count
  else:
    #True for have not lost yet
    return count


def check_win(playerhand, dealerhand):
  dealer = check_hand(dealerhand)
  player = check_hand(playerhand)

  if player > 21 and dealer <= 21:
    print(f"Dealer hand: {dealerhand}. Count: {dealer}")
    print(f"Your hand: {playerhand}. Count: {player}")
    print("Dealer wins.")

  elif player <= 21 and dealer > 21:
    print(f"Dealer hand: {dealerhand}. Count: {dealer}")
    print(f"Your hand: {playerhand}. Count: {player}")
    print("You win.")

  elif player <=21 and dealer <= 21:

    if player < dealer:
      print(f"Dealer hand: {dealerhand}. Count: {dealer}")
      print(f"Your hand: {playerhand}. Count: {player}")
      print("You lose.")

    elif player > dealer:
      print(f"Dealer hand: {dealerhand}. Count: {dealer}")
      print(f"Your hand: {playerhand}. Count: {player}")
      print("You win.")
    else:
      print(f"Dealer hand: {dealerhand}. Count: {dealer}")
      print(f"Your hand: {playerhand}. Count: {player}")
      print("It is a draw.")
  else:
    print(f"Dealer hand: {dealerhand}. Count: {dealer}")
    print(f"Your hand: {playerhand}. Count: {player}")
    print("It is a draw.")
    

ok = True

while ok:
  print(logo)
  #Dealing hands one by one
  player_hand = []
  dealer_hand = []
  
  for i in range(2):
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
  
  #Show player cards and one of the dealers cards
  print(f"Your hand is: {player_hand}")
  print(f"The dealer has the card [{dealer_hand[0]}] as one of his cards.")
  
  #Ask if player would like to hit. Must first check players hand to ensure cards are not above 21.
  
  while check_hand(player_hand) < 21:
    ask = input("Would you like to hit? Y or N: ")
    if ask.upper() == "Y":
      hit(player_hand)
  
      count = check_hand(player_hand)
      print(f"Your new hand is {player_hand} with a count of {count}.")
  
    if ask.upper() == "N":
      break
  
  #Check dealers cards. If value < 15, dealer is forced to hit. 
  
  while check_hand(dealer_hand) <= 15:
    hit(dealer_hand)
  
  #Check winner with check_win()
  check_win(player_hand,dealer_hand)

  cont = input("Would you like to play again? Y or N: ")

  if cont.upper() == "Y":
    clear()
    ok = True
  else:
    ok = False

    





