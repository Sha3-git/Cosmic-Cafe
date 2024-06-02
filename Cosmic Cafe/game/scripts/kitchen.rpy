screen kitchen():
    tag menu
    add "ui/kitchen.png"
    viewport id "vp":
            add "gui/cafe_menu/menu.png"
            mousewheel True
            xmaximum 1200
            ymaximum 600
            grid 3 1:
                xalign 0.03
                spacing 30
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
    
    hbox:
        add "gui/cafe_menu/menu.png"
    hbox:
        xalign 0.85
        yalign 0.5
        add "gui/cafe_menu/selections.png"
    text "kitchen"