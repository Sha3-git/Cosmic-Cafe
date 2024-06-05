screen kitchen():
    tag menu
    add "ui/kitchen.png"
    #add "gui/cafe_menu/menu.png"
    
    frame:
        background "gui/cafe_menu/menu.png"
        padding (40, 50, 0, 50)  # Add padding around the viewport (left, top, right, bottom)
        has viewport id "vp":
            mousewheel True
            xmaximum 1200
            ymaximum 1100
            xalign 0.05
            grid 3 7:
                spacing 30
                vbox:
                    imagebutton idle "ui/items/ingredient1.png" action Function(select_ingredient, "ui/items/ingredient1.png") tooltip "10"
                    text "10" color "#fff" xalign 0.5
                vbox:
                    imagebutton idle "ui/items/ingredient2.png" action Function(select_ingredient, "ui/items/ingredient2.png") tooltip "10"
                    text "10" color "#fff" xalign 0.5
                vbox:
                    imagebutton idle "ui/items/ingredient1.png" action Function(select_ingredient, "ui/items/ingredient1.png") tooltip "10"
                    text "10" color "#fff" xalign 0.5
    
    hbox:
        xalign 0.85
        yalign 0.5
        add "gui/cafe_menu/selections.png"

    hbox:
        xalign 0.83
        yalign 0.5
        grid 3 1:
            spacing 135
            if len(selected_ingredients) > 0:
                for ingredient in selected_ingredients:
                    imagebutton idle ingredient action Function(deselect_ingredient, ingredient)
            
            #imagebutton idle ing_1
            #imagebutton idle ing_2
            #imagebutton idle ing_3
    text "kitchen"

init python:
    selected_ingredients = []

    def select_ingredient(name):
        global selected_ingredients
        if len(selected_ingredients) < 3:
            #if name not in selected_ingredients:
                selected_ingredients.append(name)
                renpy.restart_interaction()

    def deselect_ingredient(name):
        global selected_ingredients
        #if name in selected_ingredients:
        selected_ingredients.remove(name)
        renpy.restart_interaction()












