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
            xmaximum 1200
            ymaximum 600
            vbox: 
                add "gui/frame.png"
                add "gui/frame.png"
            scrollbars "vertical"
            


    use header()

style cafe_button:
    hover_color "#ce3dd3"
    color "#ffffff"
