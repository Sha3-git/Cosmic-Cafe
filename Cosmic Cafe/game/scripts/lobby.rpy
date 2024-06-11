# animated video
image lobbybg = Movie(channel="movie_dp", play="/animated/background.webm")
image lobbybg2 = Movie(channel="movie_dp", play="/animated/background_nights.webm")
screen lobby():
    if persistent.time_of_day:
        $ bg =  "lobbybg"
    if not persistent.time_of_day:
        $ bg = "lobbybg2"
    add bg
    imagebutton idle "gui/gear.png" xalign 0.02 yalign 0.03 hover "gui/gear.png" at hover_settings_transform action MainMenu(confirm = False)
    #add "<loop 0> muic/lobby_music.mp3"
    timer 1.0 action Function(play_lobby_music)
    #outgoing transition
    $ renpy.transition(dissolve)
    tag menu
    vbox: 
        style "lobby_shop"
        #text "shop" color "#ffffff" xalign 0.5 size 20 
        imagebutton idle "ui/shop.png" hover "ui/shop.png" at hover_shop_transform action [Show("store"), Play("sound", "music/sfx/click.mp3")]
    hbox:
        style "lobby_ticket"
        imagebutton idle "ui/menu_ticket.png" hover "ui/menu_ticket.png" at hover_ticket_transform action [Show("summon"), Play("sound", "music/sfx/click.mp3")]
    hbox: 
        style "lobby_play"
        imagebutton idle "ui/play.png" hover "ui/play_hover.png" action [Show("cafe"), Play("sound", "music/sfx/click.mp3")]
    vbox:
        style "lobby_recipe"
        imagebutton idle "ui/Recipes.png" hover "ui/Recipes.png" at hover_recipe_transform action [Show("recipes"), Play("sound", "music/sfx/click.mp3")]
    vbox:
        style "lobby_inventory"
        imagebutton idle "ui/Inventory.png" hover "ui/Inventory.png" action [Show("recipes"), Play("sound", "music/sfx/click.mp3")]

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
style lobby_inventory:
    xalign 0.1
    yalign 1.02

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

transform hover_recipe_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

transform hover_inventory_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

transform hover_settings_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0


init python:
    def play_lobby_music():
        renpy.music.play("music/lobby_music.mp3", loop=True)