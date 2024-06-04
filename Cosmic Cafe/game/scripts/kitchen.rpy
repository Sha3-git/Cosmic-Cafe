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
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"

                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"

                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"

                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"

                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"
                imagebutton idle "ui/items/ingredient1.png"

    
    hbox:
        xalign 0.85
        yalign 0.5
        add "gui/cafe_menu/selections.png"
    text "kitchen"