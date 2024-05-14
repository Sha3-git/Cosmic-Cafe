# animated video
image lobbybg = Movie(channel="movie_dp", play="/animated/background.webm")

screen lobby():
    add  "lobbybg"
    #outgoing transition
    $ renpy.transition(dissolve)
    tag menu
    $ files = str(renpy.list_slots())
    hbox:
        textbutton _("store") action Show("store")
    hbox: 
        style "lobby_shop"
        imagebutton idle "ui/shop.png" hover "ui/shop.png" at hover_button_transform action Show("store")
    hbox: 
        style "lobby_play"
        imagebutton idle "ui/play.png" hover "ui/play_hover.png" action Show("cafe")

    text "files [files]" yalign 1.0
    use header()

style lobby_shop:
    yalign 0.95 
    xalign 0.95
style lobby_play:
    xalign 0.95
    yalign 0.5

transform hover_button_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0