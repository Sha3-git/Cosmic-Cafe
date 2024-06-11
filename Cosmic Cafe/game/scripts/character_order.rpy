
screen order():
    tag menu
    add "ui/cafe.png"
    frame: 
        xalign 0.3
        yalign 0.9
        xsize 960
        ysize 250
        background "gui/cafe_menu/Chat Bubble.png"
        padding(20,0,0,30)
 
        hbox: 
            yalign 0.4
            xalign 0.15
            xsize 950
            box_wrap True
            $ character_dialogue = current_order['sentence']
            if drink_interaction: 
                if sell_state:
                    $ character_dialogue = "Thanks for this drink! It really reminds me of the earliest days of galactica street"
                else:
                    $ character_dialogue = random.choice(dislike_sentences)

            text "[character_dialogue]"
            #text "[sell_state]"
    if not sell_state:
        frame: 
            xsize 710
            ysize 710
            xalign 1.1
            yalign 0.7
            background "gui/cafe_menu/drink_menu.png"
            padding (0, 50, 0, 0)
        
            vpgrid:
                spacing 50
                cols 1
                draggable True
                mousewheel True
                xalign 0.3
                scrollbars "vertical"
                for drink in persistent.drinks:
                    vbox:
                        xsize 400
                        text "[drink['multiplier']]" color "#fff"
                        imagebutton idle "ui/recipe_icons/" + drink["name"] + ".png" action [Function(session_user.sell_drink, drink, current_order), Function(select_drink)] xalign 0.5
                        $ chars = ""
                        for c in drink['characteristics'] :
                            $ chars = chars + " " + c
                        text "[chars]" xalign 0.5 color "#fff"
    else:
        imagebutton idle "ui/Complete.png" yalign 0.85 xalign 0.85 action [Show("cafe"), Function(clear_order_state)]
    frame:
        background "ui/characters/"+ current_order['character'] +".png"
        xsize 355
        ysize 448
        yalign 1.0
    imagebutton idle "ui/Return.png" hover "ui/Return_hover.png" action(Show("cafe"))yalign 0.05 xalign 0.1 
    textbutton ("Cancel Order")  action [Function(cancel_order, current_order), Show("cafe")] text_style "cancel_order_text" xalign 0.55 yalign 0.9
    use header()

style cancel_order_text:
    idle_color "#ffff"  # Color when the button is idle
    hover_color "#ac4dd1"  # Color when the button is hovered


default drink_interaction = False     
init python:
    def select_drink():
        global drink_interaction
        drink_interaction = True
    def clear_order_state():
        global sell_state
        global drink_interaction
        sell_state = False
        drink_interaction = False
    def cancel_order(order):
        for p in persistent.orders:
            if order["sentence"] == p["sentence"] and order["character"] == p["character"]:
                persistent.orders.remove(p)


    dislike_sentences = [
    "I don't much like this drink can you give me something else?",
    "This drink isn't to my taste, could I have a different one?",
    "I'm not fond of this drink, can I try something else?",
    "This drink isn't really my thing, can you give me another?",
    "I don't really enjoy this drink, could you offer me a different one?",
    "I'm not liking this drink, can I get a different one?",
    "This drink isn't very good, can I have another one instead?",
    "I'm not a fan of this drink, could I have something else?",
    "This drink doesn't suit me, could you get me a different one?",
    "I don't care for this drink, can you give me another option?",
    "This drink isn't for me, can I try something else?"
]