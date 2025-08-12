import random
# TODO: will be accomplished in the future

# suits for hearts, diamonds, clubs, & spades
suits = ["H", "D", "C", "S"]
card_vals = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
total_cards = []

for card in card_vals:
    for suit in suits:
        total_cards.append(str(card + suit))

random.shuffle(total_cards)

print(len(total_cards))
for card in total_cards:
    print(card)

class BlackJack:
    # member variables
    dealer_hand = []
    dealer_val = 0
    player_hand = []
    player_val = 0
    curr_deck = []    

    # constructor
    def __init__(self, deck):
        self.curr_deck = deck
    
    def calc_val(self, hand):
        val = 0
        for card in hand:
            # get value from first char
            placeholder = card[0]
            if placeholder.isdigit():
                val += int(placeholder)
            elif placeholder == 'A':
                val += 11
            else:
                val += 10
        return val
    
    def deal_card(self, hand):
        hand.append(self.curr_deck.pop(0))  
        return
    
    def print_cards(self, hand):
        for card in hand:
            print(card)
    
    # run method to play game
    def run(self):
        print("starting blackjack")
        random.shuffle(self.curr_deck)
        self.deal_card(self.player_hand)
        self.deal_card(self.player_hand)
        self.player_val = self.calc_val(self.player_hand)
        print(self.player_val)
        self.print_cards(self.player_hand)
        
        self.deal_card(self.dealer_hand)
        self.deal_card(self.dealer_hand)
        self.dealer_val = self.calc_val(self.dealer_hand)
        
        print(self.dealer_val)
        print(self.dealer_hand[0])

bj = BlackJack(total_cards)
bj.run()