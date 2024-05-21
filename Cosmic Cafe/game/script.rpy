﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
default persistent.loaded = False
default persistent.default_balance = 1000
default persistent.name = "user"
default inventory = []
define purchase_state = False

init python:
    class player_object:       
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance
        def update_bal(self, price, amount):
            self.balance = self.balance - price
            persistent.default_balance = self.balance
        def update_inventory(self, name, characteristic, price):
            ingredient = {
                "name": name,
                "characteristic": characteristic,
                "multiplier": 1
            }
            if self.balance >= price:
                if len(inventory) > 0:
                    for x in range(len(inventory)):
                        if ingredient["name"] == inventory[x]["name"]:  
                            inventory[x]["multiplier"] += 1
                else:
                    inventory.append(ingredient)
                purchase_state = True
            else:
                purchase_state = False


    '''def update_inventory(name, characteristic):
        ingredient = {
            "name": name,
            "characteristic": characteristic,
            "multiplier": 1
        }
        inventory.append(ingredient)
        if len(inventory) > 0:
            for x in range(len(inventory)):
                if ingredient["name"] == inventory[x]["name"]:  
                    inventory[x]["multiplier"] += 1
        else:
            inventory.append(ingredient)'''
           




label start:
    $ renpy.transition(dissolve)
    $ username = "default"
    $ session_user = player_object(persistent.name, persistent.default_balance)
    if persistent.loaded:
        $ FileLoad("auto-1", page="auto", newest = True)
        #$ persistent.loaded = False
        call screen lobby
        #"loaded is set to [persistent.loaded]"
    else:
        $ persistent.name = renpy.input("What is your name?", length=32)
        $ renpy.retain_after_load()
        $ persistent.loaded = True
        call screen lobby
    
image cafe = "ui/cafe.png"
label alyssa:
    $ renpy.transition(dissolve)
    show cafe
    #$ order = generate_order()
    $ order = gen_order()
    "[order[1]]" 
    call screen cafe

