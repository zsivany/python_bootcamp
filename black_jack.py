# import module for the deck dealing
import random


#Universal Deck class for handling the cards. Shuffling and hitting and initial dealing. Now it set for black_jack but it parametrized for any other games

class Deck(object):

    suits = 'S H D C'.split()
    ranks = '2 3 4 5 6 7 8 9 X J Q K A'.split()
    init_deck  = [r + s for s in suits for r in ranks]
    deck = random.sample(init_deck, 52)

    def __init__(self, deck_counter = len(deck)):
        self.deck_counter = deck_counter

    def black_jack_init(self, number_of_cards = 2):
        init_deck = Deck.deck
        init_card = []
        i = 0
        for i in range(number_of_cards):
            init_card.append(Deck.deck.pop())
        print len(Deck.deck)
        return init_card

    def get_deck_number(self):
        return len(Deck.deck)

    def card_deal(self):
        return Deck.deck.pop()

    def deck_shuffle(self):
        print "Deck is shuffled."
        Deck.deck = random.sample(Deck.init_deck, 52)
        print (Deck.deck)
        
        

#Player class to set up the player's attributes and methods
class Player(object):

    def __init__(self, bankroll = 100, hand = [], point = 0, win = 0, loss = 0):
        self.bankroll = bankroll
        self.hand = hand
        self.point = point
        self.loss = loss
        self.win = win
        
    def show_hand(self):
        print self.hand

    def hit(self, card):
        return self.hand.append(card)

    def stat(self):
        return self.win, self.loss


#Dealer class to set up the player's attributes and methods.
#Upgrade idea: it could inheritate from Player's class

class Dealer(object):

    def __init__(self, bankroll = 100, hand = [], point = 0, win = 0, loss = 0):
        self.bankroll = bankroll
        self.hand = hand
        self.point = point
        self.loss = loss
        self.win = win
        
        
    def show_hand(self):
        print self.hand

    def hit(self, card):
        return self.hand.append(card)

    def stat(self):
        return self.win, self.loss

# function for evaulate the first two cards for blackjack
def eval_blackjack(cards):
    if cards[0][0] == 'A' and cards[1][0] == 'A':
        print "You have BlackJack"
        return True

# function for asses the cards' value and count them
def eval_cards(cards):
    counter = 0
    for c in cards:
        #print c
        if c[0] == 'A':
            print "You gotta an ACE! Select a value:"
            v = raw_input("11 or 1: ")
            if int(v) == 11:
                counter += 11
            elif int(v) == 1:
                counter += 1
        elif c[0] == "K" or c[0] == "Q" or c[0] == "J" or c[0] == "X":
            counter += 10
        else:
            counter += int(c[0])
    return counter

# function to check each player is busted or not        
def busted(point):

    if point > 21:
        return True

# function to evaluate the players cards and decide who won the game
def eval_game(player_point, dealer_point):

    if player_point >= dealer_point:
        return True
    else:
        return False



# initial the first objects for the game
d = Deck()
p = Player()
de = Dealer()
bet = 0

# function for the end of game's stats.
def game_over():
    print "Game over"
    print "Game stats:"
    print "Player bankroll", p.bankroll
    print "Player wins/loses: ", p.win," / " ,p.loss 
    print "Dealer bankroll", de.bankroll
    print "Dealer wins/loses: ", de.win," / " ,de.loss

# function for the new game initialization
def new_game():
    
    print "Would you like to play : y/n"
    answer = raw_input()
    if answer == "y":
        print "Number of cards: ", d.get_deck_number()
        player()
    elif answer == "n":
        return game_over()
    else:
        return game_over()

# dealer function (logic and rules)
def dealer():

    de.hand = d.black_jack_init(2)
    
    print "Dealer Round"
    de.show_hand()
    de.point = eval_cards(de.hand)
    # the loop which ensures the dealer's logic ( call if cards' value less then 16 and stand if greater then 17)
    while de.point < 17:
        de.hit(d.card_deal())
        de.show_hand()
        t = []
        t.append(de.hand[-1])
        de.point += eval_cards(t)
        if busted(de.point):
            print "Dealer Busted"
            de.show_hand()
            print de.point
            de.bankroll -= int(bet)
            p.bankroll += 2 * int(bet)
            de.loss += 1
            p.win +=1
            print "Dealer's bankroll: ", de.bankroll
            return new_game()
            break
        de.show_hand()
    
    print de.point
    
    if eval_game(p.point, de.point):
        print "Player wins, Dealer lose!"
        de.bankroll -= int(bet)
        p.bankroll += 2 * int(bet)
        p.win +=1
        de.loss +=1
        new_game()
        
    else:
        print "Dealer wins, Player lose!"
        de.bankroll += int(bet)
        p.bankroll -= 2 * int(bet)
        p.loss += 1
        de.win += 1
        new_game()
    
# player function (logic and rules)    
def player():
       
    p.hand = d.black_jack_init(2)
    print "Player Round"
    p.show_hand()
    
    global bet
    
    #blackjack evaulation
    if eval_blackjack(p.hand):
        print "Player win"
        de.bankroll -= int(bet)
        p.bankroll += 2 * int(bet)
        p.win +=1
        de.loss +=1
        return new_game()
    p.point = eval_cards(p.hand)
    print "Your point: ", p.point
    bet = raw_input("Please give a bet: " )
    a = "hitorstand"
    while a != "s":
        print "Do you want (h)it or (s)tand?"
        a = raw_input("h or s: ")
        if a == "h":
            p.hit(d.card_deal())
            p.show_hand()
            t = []
            t.append(p.hand[-1])          
            p.point += eval_cards(t)
            print "Your point: ", p.point
            if busted(p.point):
                print "Player Busted"
                p.bankroll -= int(bet)
                de.bankroll += int(bet)
                p.loss += 1
                de.win += 1
                print p.bankroll
                print "End of busted if"
                new_game()
                break
            else:
                print "You can continue"
        elif a == "s":
            print "You stand"
            print "Player points against dealer: ", p.point
            dealer()
            

   
# call the game
new_game()
