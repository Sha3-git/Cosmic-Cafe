screen drink_notif():
    hbox:
        xalign 1.0
        yalign 0.08
      
        if created_drink["rarity"] != "":
            add "gui/kitchen_menu/"+ str(created_drink["rarity"]) +" Create.png"
    if created_drink["name"] != "":
        add "ui/recipe_icons/"+ str(created_drink["name"]) + ".png" xalign 0.5 yalign 0.06
        timer 2.0 action [Hide('drink_notif'), Function(clear_created_drink)]
    text "[created_drink['name']]" color "#fff" xalign 0.9 yalign 0.12 size 40 

# Function to clear the created_drink dictionary
init python:
    def clear_created_drink():
        global created_drink
        created_drink = {"name": "", "rarity": "", "price": 0, "characteristics": [], "multiplier": 0}
   
    