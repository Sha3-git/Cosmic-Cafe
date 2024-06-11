screen kitchen():
    tag menu
    add "ui/kitchen.png"
    #add "gui/cafe_menu/menu.png"
    use drink_notif
    
    frame:
        background "gui/cafe_menu/menu.png"
        padding (40, 50, 0, 50)  # Add padding around the viewport (left, top, right, bottom)
        has viewport id "vp":
            mousewheel True
            xmaximum 1200
            ymaximum 1100
            xalign 0.05
            $ rows = round(len(ingredients) /3) + (len(ingredients) % 3)
            grid 3 rows:
                spacing 30
                for i in range(len(persistent.inventory)):
                    vbox:
                        text str(persistent.inventory[i]["characteristic"]) color "#fff" xalign 0.5
                        imagebutton idle "ui/items/" + persistent.inventory[i]["name"] + ".png" action Function(select_ingredient, persistent.inventory[i]["name"]) 
                        text str(persistent.inventory[i]["multiplier"]) color "#fff" xalign 0.5
    
    imagebutton idle "ui/Return.png" hover "ui/Return_hover.png" action(Show("cafe"))yalign 0.95 xalign 0.95  at rotate_arrow    
    
    hbox:
        xalign 0.85
        yalign 0.5
        add "gui/cafe_menu/selections.png"
    hbox: 
        xalign 0.73
        yalign 0.8
        if len(selected_ingredients) >= 3:
            imagebutton idle "ui/Create.png" hover "ui/Create.png" at hover_create_transform action [Function(session_user.update_drinks, selected_ingredients), Function(clear_ingredients)]
        else:
            imagebutton idle "ui/Create_disabled.png"

    hbox:
        xalign 0.83
        yalign 0.5
        grid 3 1:
            spacing 135
            if len(selected_ingredients) > 0:
                for ingredient in selected_ingredients:
                    imagebutton idle "ui/items/" + ingredient + ".png" action Function(deselect_ingredient, ingredient)
            
            #imagebutton idle ing_1
            #imagebutton idle ing_2
            #imagebutton idle ing_3
    #text "[persistent.recipes[0]['name']] "
    #text "kitchen [persistent.drinks[0]['multiplier']]"

transform hover_create_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0
transform rotate_arrow:
    rotate 180
init python:
    selected_ingredients = []

    def select_ingredient(name):
        global selected_ingredients
        # Find the ingredient in the inventory
        for item in persistent.inventory:
            if item["name"] == name:
                if item["multiplier"] > 0 and len(selected_ingredients) < 3:
                    item["multiplier"] -= 1
                    selected_ingredients.append(name)
                    renpy.restart_interaction()
                break

    def deselect_ingredient(name):
        global selected_ingredients
        # Find the ingredient in the inventory
        for item in persistent.inventory:
            if item["name"] == name:
                item["multiplier"] += 1
                break
        selected_ingredients.remove(name)
        renpy.restart_interaction()
    def clear_ingredients():
        selected_ingredients.clear()
        for item in persistent.inventory:
            if item["multiplier"] <= 0:
                persistent.inventory.remove(item)
        












