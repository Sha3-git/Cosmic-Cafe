screen drink_notif():
    hbox:
        xalign 1.0
        yalign 0.08
        $ sss = [created_drink["name"]]
        text "[sss]"
        if created_drink["name"] != "":
            add "gui/kitchen_menu/Common Create.png"
    