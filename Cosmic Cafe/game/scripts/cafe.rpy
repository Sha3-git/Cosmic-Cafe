screen cafe():
    $ renpy.transition(dissolve)
    tag menu
    add "ui/cafe.png"
    hbox:
        xalign 0.5
        yalign 0.5
        textbutton _("Serve Alyssa") action Jump("alyssa") text_color "#fff" style "cafe_button"

    use header()

style cafe_button:
    hover_color "#ce3dd3"
    color "#ffffff"
