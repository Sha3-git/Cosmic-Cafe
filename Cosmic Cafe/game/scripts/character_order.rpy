screen order():
    tag menu
    add "ui/cafe.png"
    frame: 
        xalign 0.25
        yalign 0.9
        xsize 960
        ysize 250
        background "gui/cafe_menu/Chat Bubble.png"
        hbox: 
            yalign 0.3
            xalign 0.1
            box_wrap True
            $ character_dialogue = current_order['sentence']
            if drink_interaction: 
                if sell_state:
                    $ character_dialogue = "Thanks for this drink! It really reminds me of the earliest days of galactica street"
                else:
                    $ character_dialogue = "I don't much like this drink can you give me something else?"
            text "[character_dialogue]"
            text "[sell_state]"
    frame: 
        xsize 547
        ysize 780
        xalign 0.9
        yalign 0.7
        background "gui/cafe_menu/drink_menu.png"
        padding (40, 50, 0, 50)
        has viewport id "order":
            xmaximum 540
            ymaximum 780
            vpgrid:
                cols 3
                draggable True
                mousewheel True
                scrollbars "vertical"
                for drink in persistent.drinks:
                    vbox:
                        imagebutton idle "ui/recipe_icons/" + drink["name"] + ".png" action [Function(session_user.sell_drink, drink, current_order), Function(select_drink)]
    frame:
        background "ui/Characters/Alyssa.png"
        xsize 355
        ysize 448
        yalign 1.0
default drink_interaction = False     
init python:
    def select_drink():
        global drink_interaction
        drink_interaction = True