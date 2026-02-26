import random
# Key Python Topics:
# OOP (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation (random.shuffle())
# Instructions:

# Exercise 1: Quizz
# Answer the following questions:

# What is a class? It's the blueprint for an object type, defining the attributes and methods (actions) that can be taken on that object. 
# What is an instance? An instance is the actual object that's of that class type. 
# What is encapsulation? Encapsulating a bunch of different actions into one class
# What is abstraction? When a lot of the functionality is hidden in the background, so a user can call one thing and it will cause many actions to take place in the background without the user knowing
# What is inheritance? When a new class takes on the attributes and methods of an existing class
# What is multiple inheritance? A child class can inherit from more than one parent class
# What is polymorphism? When different objects respond to the same function or method in their own way. 
# What is method resolution order or MRO? the sequence Python follows to search for a method or attribute in a class heirarchy. Inward to outer





# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"Card('{self.suit}', '{self.value}')"
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
        

class Deck:
    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        values = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')

        self.cards = [Card(s,v) for s in suits for v in values]
    
    def shuffle(self):
        if len(self.cards) != 52:
            print("Cannot shuffle: some cards are missing!")
            return
        
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None 
        
deck = Deck()
print(f"Deck created with {len(deck.cards)} cards.")
deck.shuffle()
dealt_card = deck.deal()
print(f"You were dealt: {dealt_card}")
print(f"Cards remaining in deck: {len(deck.cards)}")        