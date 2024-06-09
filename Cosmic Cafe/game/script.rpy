# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
default persistent.loaded = False
default persistent.default_balance = 100000000
default persistent.name = "user"
default persistent.inventory = []
default persistent.drinks = []
default persistent.recipes = []
define purchase_state = False
default created_drink = {"name":"", "rarity":""}
default persistent.orders = []
default sell_state = False
default current_order = { "character": "","sentence": "","characteristics": "","profit": ""}

init python:
    class player_object:       
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance
        def update_bal(self, price, amount):
            if self.balance >= price:
                self.balance = self.balance - price
                persistent.default_balance = self.balance
        def update_inventory(self, name, characteristic, price):
            placeholder_ingredient = {
                "name": name,
                "characteristic": characteristic,
                "multiplier": 1
            }
            if self.balance >= price:
                ingredient_found = False

                for item in persistent.inventory:
                    if placeholder_ingredient["name"] == item["name"]:
                        item["multiplier"] += 1
                        ingredient_found = True
                        break

                if not ingredient_found:
                    persistent.inventory.append(placeholder_ingredient)
                purchase_state = True
                
            else:
                purchase_state = False
        def create_drink(self, ingredients):
            purchase_state = True;
        def update_drinks(self, select_ingredient):
            # Check if the selected ingredients match any recipe
            for recipe in recipes:
                if set(select_ingredient) == set(recipe["ingredients"]) and recipe["unlocked"]:
                    drink_name = recipe["name"]
                    rarity = recipe["rarity"]
                    price = recipe["price"]
                    characteristics = recipe["characteristics"]
                    
                    recipe_found = False
                    # Check if the drink already exists in persistent.drinks
                    for drink in persistent.drinks:
                        if drink["name"] == drink_name:
                            drink["multiplier"] += 1
                            #created_drink = {"name":drink_name, "rarity":rarity}
                            created_drink["name"] = drink_name
                            created_drink["rarity"] = rarity
                            recipe_found = True
                            break

                    # If the drink does not exist, add it to persistent.drinks
                    if not recipe_found:
                        persistent.drinks.append({
                            "name": drink_name,
                            "characteristics": characteristics,
                            "rarity": rarity,
                            "price": price,
                        "multiplier": 1
                        })
                        #created_drink = {"name":drink_name, "rarity":rarity}
                        created_drink["name"] = drink_name
                        created_drink["rarity"] = rarity
                else:
                    created_drink["name"] = "Inedible Soda"
                    created_drink["rarity"] ="Common"

        def sell_drink(self, drink, current):
            global sell_state
            order_chars = current["characteristics"]
            drink_chars = drink["characteristics"]
            match_count = 0

            for char in order_chars:
                if char in drink_chars:
                    match_count += 1
            if len(order_chars) == 1 and match_count >= 1:
                self.balance += current["profit"]
                persistent.default_balance = self.balance
                result = "Match"
                sell_state = True
            elif len(order_chars) == 2 and match_count >= 2:
                self.balance += current["profit"]
                persistent.default_balance = self.balance
                result = "Match"
                sell_state = True
            elif len(order_chars) == 3 and match_count == 3:
                self.balance += current["profit"]
                persistent.default_balance = self.balance
                result = "Match"
                sell_state = True
            else:
                result = "No Match"
                sell_state = False
            for d in persistent.drinks:
                if d["name"] == drink["name"]:
                    d["multiplier"] -= 1
                    if d["multiplier"] <= 0:
                        persistent.drinks.remove(d)
            for order in persistent.orders:
                if order == current:
                    persistent.orders.remove(order)
            
                




    '''def update_persistent.inventory(name, characteristic):
        ingredient = {
            "name": name,
            "characteristic": characteristic,
            "multiplier": 1
        }
        persistent.inventory.append(ingredient)
        if len(persistent.inventory) > 0:
            for x in range(len(persistent.inventory)):
                if ingredient["name"] == persistent.inventory[x]["name"]:  
                    persistent.inventory[x]["multiplier"] += 1
        else:
            persistent.inventory.append(ingredient)'''
           


image splash = Movie(channel="movie_dp", play="/animated/splash_screen.webm")
label splashscreenn:
    show  splash with dissolve 
    with Pause(12.5)
    return
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

