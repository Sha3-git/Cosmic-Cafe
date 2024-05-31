image summon_anim = Movie(channel="movie_dp", play="/animated/summonanim.webm")

screen summoned():
    add "summon_anim"
    #timer 1 action Function(renpy.show, "ui/drink_recipes/drink1.png")
    timer 1.0 action Show("recipe_summon")

init python:
    def show():
        renpy.show("")
screen recipe_summon():
    hbox:
        xalign 0.5
        yalign 0.5
        add "ui/drink_recipes/drink1.png"
