screen summon():
    tag menu
    add "ui/store.png"
    $ renpy.transition(dissolve)
   
    hbox:
        textbutton _("return") action ShowMenu("lobby") 
        yalign 0.1

    hbox:
        yalign 0.5
        xalign 0.5
        vbox: 
            if persistent.default_balance >= 1000:
                add "ui/gacha.png"
            else:
                add "ui/gacha_disabled.png"
    use header()


