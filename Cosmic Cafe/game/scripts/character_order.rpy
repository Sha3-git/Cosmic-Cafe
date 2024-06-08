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
            text "[current_order['sentence']]"
    frame: 
        xsize 547
        ysize 780
        xalign 0.9
        yalign 0.7
        background "gui/cafe_menu/drink_menu.png"
    frame:
        background "ui/Characters/Alyssa.png"
        xsize 355
        ysize 448
        yalign 1.0