screen store():
    tag menu
    add "ui/store.png"
    $ renpy.transition(dissolve)
    #$ bal = renpy.store.session_user.balance
    $ bal = 5
    text "balance: " + str(bal)
    #$ bal = session_user.balance
    #text "balance:" + str(bal)
   
    hbox:
        xalign 0.5
        text "welcome to test cafe" style "cafe_text"
    hbox:
        textbutton _("return") action ShowMenu("lobby") 
        yalign 0.1

    hbox:
        yalign 0.5
        xalign 0.5
        textbutton _("item 1") action Function(session_user.update_bal, 1, 2)             
        textbutton _("item 2") action Function(session_user.update_bal, 3, 2) 
        