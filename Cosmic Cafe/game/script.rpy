# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
define persistent.loaded = False
default persistent.default_balance = 10
init python:
    class player_object:       
        def __init__(self, name, balance, ingredients):
            self.name = name
            self.balance = balance
            self.ingredients = ingredients
        def update_bal(self, price, amount):
            self.balance = self.balance - price
            persistent.default_balance = self.balance

            
           



label start:
    $ renpy.transition(dissolve)
    $ username = "default"
    $ session_user = player_object("user1", persistent.default_balance, [])
    if persistent.loaded:
        $ FileLoad("auto-1", page="auto", newest = True)
        #$ persistent.loaded = False
        call screen lobby
        #"loaded is set to [persistent.loaded]"
    else:
        $ username = renpy.input("Enter your name: ", length=32)
        $ renpy.retain_after_load()
        $ persistent.loaded = True
        call screen lobby
    

 