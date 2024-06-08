screen cafe():
    $ renpy.transition(dissolve)
    tag menu
    add "ui/cafe.png"
    

            
    frame:
        background "gui/cafe_menu/Cafe Menu.png"
        xalign 0.5
        yalign 0.5
        xsize 601  # Set the frame size to match the background image size
        ysize 832
        padding(60, 150, 60, 0)
        has viewport id "cafe":
            xmaximum 601
            ymaximum 400
            spacing 5  # Adjust spacing between the frames, if you need to reduce it further you can use a smaller value.
            vpgrid :  # Adjust spacing between rows
                cols 1
                spacing 50
                draggable True
                mousewheel True
                scrollbars "vertical"
                for i in range(5):
                        vbox:
                            text "alyssa"
                            hbox:
                                box_wrap True
                                text " alyssaalyssaalyssaalyssa something sweet and something salty" color "#fff" xalign 0.0 size 25
     
            
    hbox:
        xalign 0.05
        yalign 0.95
        textbutton "kitchen" action Show("kitchen")
            


    use header()

style cafe_button:
    hover_color "#ce3dd3"
    color "#ffffff"
#style order_style:
    