image summon_anim = Movie(channel="movie_dp", play="/animated/summonanim.webm", loop=False)
screen summoned():
    tag menu
    #$ reset_movie()
    add "summon_anim"
   

    #timer 1 action Function(renpy.show, "ui/drink_recipes/drink1.png")
    timer 0.5 action Play("sound", "music/sfx/summon.mp3")
    timer 1.0 action [Show("recipe_summon") ]
    timer 10.0 action [Hide("recipe_summon"), Show("summon")]
    imagebutton idle "ui/Return.png" hover "ui/Return_hover.png" action [Hide("recipe_summon"), Show("summon")]  yalign 0.95 xalign 0.05

    

screen recipe_summon():
    text "[summoned_recipe]"
    hbox:
        xalign 0.5
        yalign 0.5
        add "ui/recipe_summons/" + summoned_recipe + ".png"

init python:
    def reset_movie():
        renpy.show('summon_anim', what=Movie(channel="movie_dp", play="/animated/summonanim.webm", loop=False))