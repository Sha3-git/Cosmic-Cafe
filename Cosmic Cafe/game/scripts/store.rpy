style my_text_button:
    idle_color "#ffff"  # Color when the button is idle
    hover_color "#d6a1eb"  # Color when the button is hovered
screen store():
    tag menu
    add "ui/store.png"
    $ renpy.transition(dissolve)
    #$ bal = renpy.store.session_user.balance
   
   
   
        

    $ rows = round(len(ingredients) /3) + (len(ingredients) % 3)
    $ size = len(persistent.inventory)
    
    
    fixed:
        viewport id "vp":
            mousewheel True
            xmaximum 1300
            ymaximum 800
            xalign 0.5
            yalign 0.7
            grid 5 rows:
                spacing 50
                for i in range (len(ingredients)):
                    vbox:
                        imagebutton idle "ui/ingredients/" + ingredients[i]["name"]+ ".png" action [Function(session_user.update_inventory, ingredients[i]["name"], ingredients[i]["characteristic"], ingredients[i]["price"]), Function(session_user.update_bal, ingredients[i]["price"], 1), Play("sound", "music/sfx/money_spent.mp3")]
                        text str(ingredients[i]["characteristic"]) color "#fff" xalign 0.5
               
    use header()
    use return()





