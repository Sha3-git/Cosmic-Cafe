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
                imagebutton idle "ui/gacha.png" hover "ui/gacha.png" at hover_summon_transform action ShowMenu("summoned")
            else:
                add "ui/gacha_disabled.png"
    hbox: 
        yalign 0.7
        xalign 0.5
        add "ui/cost.png" 

    use header()


transform hover_summon_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0