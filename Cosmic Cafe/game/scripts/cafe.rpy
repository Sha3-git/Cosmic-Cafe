screen cafe():
    $ renpy.transition(dissolve)
    tag menu
    add "ui/cafe.png"
    
    hbox:
        xalign 0.5
        yalign 0.5
        #textbutton _("Serve Alyssa") action Jump("alyssa") text_color "#fff" style "cafe_button"
        viewport id "vp":
            xalign 0.5
            yalign 0.5
            mousewheel True
            xmaximum 1200
            ymaximum 600
            vbox: 
                add "ui/order.png" xalign 0.5 yalign 0.5
            vbox:
                xalign 0.2 
                text "alyssa\n" color "#fff"
                text "something sweet" color "#fff"
            vbox: 
                add "ui/order.png" xalign 0.5 yalign 0.7
            scrollbars "vertical"
    hbox:
        xalign 0.05
        yalign 0.95
        textbutton "kitchen" action Show("kitchen")
            


    use header()

style cafe_button:
    hover_color "#ce3dd3"
    color "#ffffff"
#style order_style:
    