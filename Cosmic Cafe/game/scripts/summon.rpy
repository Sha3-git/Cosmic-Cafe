screen summon():
    tag menu
    add "ui/store.png"
    $ renpy.transition(dissolve)
    hbox:
        yalign 0.5
        xalign 0.5
        vbox: 
            if persistent.default_balance >= 1000:
                imagebutton idle "ui/gacha.png" hover "ui/gacha.png" at hover_summon_transform action [Show("summoned"), Function(gacha)]
            else:
                add "ui/gacha_disabled.png"
    hbox: 
        yalign 0.7
        xalign 0.5
        add "ui/cost.png" 

    use header()
    use return()


transform hover_summon_transform:
    on hover:
        linear 0.1 zoom 1.05
    on idle:
        linear 0.1 zoom 1.0

default summoned_recipe = ""

init python:
    def gacha():
        gacha = random.choice(recipes)
        persistent.default_balance -= gacha["price"]
        nopity = random.randint(1, 100) % 2
        if nopity == 0:
            global summoned_recipe
            summoned_recipe = gacha["name"]
        else:
            global summoned_recipe
            summoned_recipe = "nothing"
        recipe_exists = False
        for persistent_recipe in persistent.recipes:
            if persistent_recipe["name"] == gacha["name"]:
                recipe_exists = True
                break
        if not recipe_exists:
            persistent.recipes.append(gacha)
            