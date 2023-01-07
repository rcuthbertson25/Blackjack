import random
dealer_count=0
user_count=0
cards= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

def CardCounter(hand,count):
  try:
    if int(hand)%1 == 0:
      count += int(hand)
      return count
  except:
    if hand == "A":
      if count + 11 > 21:
        count += 1
        return count
      else:
        count += 11
        return count
    count += 10
    return count

def CardOutput(hand):
  out = ""
  for card in hand:
    out += (str(card) + " ")
  return out

def Blackjack():
  print("Welcome to Draftkings Blackjack!")
  starting_balance = int(input("Deposit Starting Balance: $"))
  account_balance = starting_balance
  win = 0
  loss = 0
  print()

  play = input("Deal Hand? (Y) or (N): ")
  while account_balance > 0 and play == "Y":
      user_count = 0
      dealer_count = 0
      user_cards = []
      dealer_cards = []
  
      wager = int(input("Insert wager: $"))
      if account_balance - wager < 0:
        print("Insignificant Funds. Try again.")
        continue
      else:
        account_balance -= wager
        print()
      
      dealer=random.choice(cards)
      dealer_cards.append(dealer)
      
      card1=random.choice(cards)
      card2=random.choice(cards)
      user_cards.append(card1)
      user_cards.append(card2)
    
      dealer_count = CardCounter(dealer,dealer_count)
      user_count = CardCounter(card1,user_count)
      user_count = CardCounter(card2,user_count)
      
      dealer_output = "Dealer's Hand: "
      user_output = "Your Hand: "
    
      dealer_output += str(CardOutput(dealer_cards))
      dealer_output += ("(" + str(dealer_count) + ")")
    
      user_output += str(CardOutput(user_cards))
      user_output += ("(" + str(user_count) + ")")
      
      print(dealer_output)
      print(user_output)
      print()
      
      if user_count == 21:
        print("Blackjack! You Win!")
        payout = wager * 1.5
        account_balance += payout
        win += 1
        print("Current Account Balance: ${}".format(account_balance))
        print()
        print("------------------------------")
        print()
        play = input("Deal Hand? (Y) or (N): ")
        print()
        
      else:
        ongoing = True
        bust = False
        while ongoing == True:
          dec = int(input("Hit(1), Stand(2): "))
          if dec == 1:
            card3=random.choice(cards)
            user_cards.append(card3)
            user_output = "Your Hand: "
            user_output += CardOutput(user_cards)
            user_count = CardCounter(card3,user_count)
            user_output += ("(" + str(user_count) + ")")
            print(user_output)
            print()
            if user_count > 21:
              bust = True
              break
            elif user_count == 21:
              break
            continue
          else:
            ongoing = False
            print()
            continue
  
      if bust == True:
        print("Bust! You Lose!")
        print("Current Account Balance: ${}".format(account_balance))
        print()
        print("------------------------------")
        print()
        loss += 1
        play = input("Deal Hand? (Y) or (N): ")
        continue
        
      card4 = random.choice(cards)
      dealer_cards.append(card4)
      dealer_count = CardCounter(card4,dealer_count)
    
      dealer_output = "Dealer's Hand: "
      dealer_output += CardOutput(dealer_cards)
      dealer_output += ("(" + str(dealer_count) + ")")
      print(dealer_output)
    
      if dealer_count == 21:
        print ("Dealer got Blackjack! Better luck next time!")
        print("Current Account Balance: ${}".format(account_balance))
        print()
        print("------------------------------")
        print()
        loss += 1
        play = input("Deal Hand? (Y) or (N): ")
        continue
      else:
        while dealer_count <= 16:
          card = random.choice(cards)
          dealer_cards.append(card)
          dealer_count = CardCounter(card,dealer_count)
          dealer_output = "Dealer's Hand: "
          dealer_output += CardOutput(dealer_cards)
          dealer_output += ("(" + str(dealer_count) + ")")
          print(dealer_output)
        print()
        if dealer_count > 21:
          print("Dealer Bust! You Win!")
          account_balance += wager*2
          win += 1
          print("Current Account Balance: ${}".format(account_balance))
          print()
          print("------------------------------")
          print()
          play = input("Deal Hand? (Y) or (N): ")
        else:
          if dealer_count > user_count:
            print("Dealer wins!")
            print("Current Account Balance: ${}".format(account_balance))
            print()
            print("------------------------------")
            print()
            loss += 1
            play = input("Deal Hand? (Y) or (N): ")
          elif dealer_count < user_count:
            print("You win!")
            account_balance += wager*2
            win += 1
            print("Current Account Balance: ${}".format(account_balance))
            print()
            print("------------------------------")
            print()
            play = input("Deal Hand? (Y) or (N): ")
          else:
            print("Tie!")
            print("Current Account Balance: ${}".format(account_balance))
            print()
            print("------------------------------")
            print()
            account_balance += wager
            play = input("Deal Hand? (Y) or (N): ")
  if account_balance == 0:
    print("Insignificant funds. Deposit to play again!")
    print()
    print("Session final stats:")
    print("W/L: {0}-{1}".format(win,loss))
    profit = account_balance - starting_balance
    if profit < 0:
      out = "Profit: -$" + str(abs(profit))
    else:
      out = "Profit: $" + str(profit)
    return out
  elif play == "N":
    return "Thanks for playing!"
print(Blackjack())