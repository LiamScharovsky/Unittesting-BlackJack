import unittest
from blackJackImproved import Player, Dealer, Deck, Game, Human

class Tests(unittest.TestCase):
    
    def test_deal_to_dealer(self):
        deck = Deck()                                 #open deck
        dealer = Dealer([])                           #give dealer an empty hand
        dealer.hitSelf(deck)                          #tell dealer to give himself a card
        self.assertEqual(1, len(dealer.hand))         #assert that 1 is equal to the number of cards in dealer's hand

    def test_deal_to_player(self):
        player = Player("hand", "name")               #calls for player class
        message = player.printBust()                  #records the message from player bust
        self.assertAlmostEqual (None, message)        #makes sure nothing is being returned, just printed

    def test_number_of_cards_per_deck(self):
        
        deck = Deck()                                 #opens deck
        nDeck = deck.cards                        
        self.assertAlmostEqual(52, len(nDeck))        #checks that a single deck should have 52 cards
        

    def test_correct_score(self):
        player = Player([], "Liam")                    #call class with parameters needed
        score = player.getScore()                      #use method of class
        self.assertAlmostEqual (0, score)              #compare

    def test_push_message(self):
        deck = Deck()                                                 #class used for parameter for Game
        human = Human([deck.dealCard(),deck.dealCard()])              #class used for parameter for Game
        dealer = Dealer([deck.dealCard(),deck.dealCard()])            #class used for parameter for Game
        game = Game(human,dealer)                                 #1st class, but needs other classes
        message = game.playerPushes()                             #method from 1st class
        self.assertAlmostEqual (None, message)                     #compare

if __name__ == '__main__':
    unittest.main()