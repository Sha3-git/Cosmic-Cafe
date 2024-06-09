screen cafe():
    $ renpy.transition(dissolve)
    tag menu
    add "ui/cafe.png"
    text "[persistent.orders[0]['character']]"
            
    frame:
        background "gui/cafe_menu/Cafe Menu.png"
        xalign 0.5
        yalign 0.7
        xsize 601  # Set the frame size to match the background image size
        ysize 832
        padding(60, 150, 20, 0)
        has viewport id "cafe":
            xmaximum 601
            ymaximum 400
            spacing 5  # Adjust spacing between the frames, if you need to reduce it further you can use a smaller value.
            vpgrid :  # Adjust spacing between rows
                cols 1
                spacing 90
                draggable True
                mousewheel True
                scrollbars "vertical"
                
                for order in persistent.orders:
                        vbox:
                            
                            text "[order['character']]"
                            hbox:
                                box_wrap True
                                textbutton ("[order['sentence']]") action [Function(select_order, order), Show("order")]
     
            
    hbox:
        xalign 0.05
        yalign 0.95
        textbutton "kitchen" action Show("kitchen")
            


    use header()

style cafe_button:
    hover_color "#ce3dd3"
    color "#ffffff"
#style order_style:
init python:
    #current_order = {}
    def select_order(order):
        current_order["character"] = order["character"]
        current_order["sentence"] = order["sentence"]
        current_order["characteristics"] = order["characteristics"]
        current_order["profit"] = order["profit"]
        renpy.restart_interaction()
