# animated video
image lobbybg = Movie(channel="movie_dp", play="/animated/background.webm")

screen lobby():
    add  "lobbybg"
    #add "<loop 0> muic/lobby_music.mp3"
    timer 1.0 action Function(play_lobby_music)
    #outgoing transition
    $ renpy.transition(dissolve)
    tag menu
    $ files = str(renpy.list_slots())
    hbox:
        textbutton _("store") action Show("store")
    vbox: 
        style "lobby_shop"
        text "shop" color "#fff" xalign 0.5 size 30 
        imagebutton idle "ui/shop.png" hover "ui/shop.png" at hover_shop_transform action Show("store")
    hbox:
        style "lobby_ticket"
        imagebutton idle "ui/menu_ticket.png" hover "ui/menu_ticket.png" at hover_ticket_transform action Show("summon")
    hbox: 
        style "lobby_play"
        imagebutton idle "ui/play.png" hover "ui/play_hover.png" action Show("cafe")
    vbox:
        style "lobby_recipe"
        imagebutton idle "ui/Recipes.png" hover "ui/Recipes.png" action Show("recipes")

    text "files [files]" yalign 1.0
    use header()

style lobby_shop:
    yalign 0.95 
    xalign 0.95
style lobby_ticket:
    yalign 0.94 
    xalign 0.85
style lobby_play:
    xalign 0.95
    yalign 0.5
style lobby_recipe:
    xalign 0.2
    yalign 0.98

transform hover_shop_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

transform hover_ticket_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

init python:
    def play_lobby_music():
        renpy.music.play("music/lobby_music.mp3", loop=True)