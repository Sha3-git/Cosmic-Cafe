screen recipes():
    tag menu
    text "recipe"
    fixed:
        viewport id "recipe":
            mousewheel True
            xmaximum 1920
            ymaximum 1080
            grid 4 4 spacing -4:
                for r in recipes:
                    if r["name"] in persistent.recipes:
                        imagebutton idle "gui/recipe_menu/" + r["name"] + ".png"
                    else:
                        imagebutton idle "gui/recipe_menu/" + r["name"] + " Locked.png"

init -1 python:
    recipes = [
    {
        "name": "Void Cocoa",
        "rarity": "Common",
        "price": 870,
        "ingredients": ["Constellation Cocoa", "Comet Ice", "Milky Way"],
        "characteristics": ["Rich","Warm", "Cold"],
        "unlocked": True
    },
    {
        "name": "Space Static",
        "rarity": "Common",
        "price": 585,
        "ingredients": ["Comet Ice", "Bottled Nebula", "Sparkling Rain"],
        "characteristics": ["Cold","Sweet", "Fizzy"],
        "unlocked": True
    },
    {
        "name": "Planetary Boba",
        "rarity": "Common",
        "price": 390,
        "ingredients": ["Planet Pearls", "Milky Way", "Comet Ice"],
        "characteristics": ["Tangy","Warm", "Cold"],
        "unlocked": True
    },
    {
        "name": "Sun Proximity",
        "rarity": "Uncommon",
        "price": 555,
        "ingredients": ["Lunar Lavendar", "Sparkling Rain", "Comet Ice"],
        "characteristics": ["Floral","Fizzy", "Cold"],
        "unlocked": True
    },
    {
        "name": "High Energy",
        "rarity": "Uncommon",
        "price": 675,
        "ingredients": ["Shot of Gamma", "Milky Way", "Quantum Foam"],
        "characteristics": ["Energizing","Warm", "Sweet"],
        "unlocked": True
    },
    {
        "name": "Megastructure",
        "rarity": "Uncommon",
        "price": 375,
        "ingredients": ["Lenakaiea Leaves","Stardust Sugar", "White Dwarf Water"],
        "characteristics": ["Herbal","Sweet", "Refreshing"],
        "unlocked": True
    },
    {
        "name": "Sweet and Savoury",
        "rarity": "Uncommon",
        "price": 810,
        "ingredients": ["Shot of Gamma","Salt from Sirius", "Bottled Nebula"],
        "characteristics": ["Energizing","Sweet", "Salty"],
        "unlocked": True
    },
    {
        "name": "Sakura",
        "rarity": "Rare",
        "price": 1170,
        "ingredients": ["Sakura Boba", "Starfruit Essence", "Milky Way"],
        "characteristics": ["Warm","Sweet", "Sweet"],
        "unlocked": True
    },
    {
        "name": "Clean Space",
        "rarity": "Rare",
        "price": 870,
        "ingredients": ["Meteor Mint","Venus Vanilla", "Milky Way"],
        "characteristics": ["Fresh","Creamy", "Warm"],
        "unlocked": True
    },
    {
        "name": "Honey Bee",
        "rarity": "Rare",
        "price": 900,
        "ingredients": ["Halley's Honey","Venus Vanilla", "Milky Way"],
        "characteristics": ["Sweet","Creamy", "Warm"],
        "unlocked": True
    },
    {
        "name": "Earthly Crunch",
        "rarity": "Rare",
        "price": 960,
        "ingredients": ["Aurora Almonds","Venus Vanilla", "Milky Way"],
        "characteristics": ["Nutty","Creamy", "Warm"],
        "unlocked": True
    },
    {
        "name": "Phenomena",
        "rarity": "Epic",
        "price": 1200,
        "ingredients": ["Pulsar Pearls","Starfruit Essence", "Milky Way"],
        "characteristics": ["Sweet","Sweet", "Warm"],
        "unlocked": True
    },
    {
        "name": "Juicy Petals",
        "rarity": "Epic",
        "price": 1365,
        "ingredients": ["Celestial Cherry", "Sakura Boba", "White Dwarf Water"],
        "characteristics": ["Fruity","Sweet", "Refreshing"],
        "unlocked": True
    },
    {
        "name": "Far Out",
        "rarity": "Epic",
        "price": 930,
        "ingredients": ["Pluto Pistachio","White Dwarf Water", "Quantum Foam"],
        "characteristics": ["Nutty","Refreshing", "Sweet"],
        "unlocked": True
    },
    {
        "name": "Sunlight",
        "rarity": "Legendary",
        "price": 30915,
        "ingredients": ["Orion Orange", "Supergawp", "Quantum Foam"],
        "characteristics": ["Citrusy","Nutty", "Sweet"],
        "unlocked": False
    },
    {
        "name": "Epitome",
        "rarity": "Legendary",
        "price": 30645,
        "ingredients": ["Supergawp","Pulsar Pearls", "White Dwarf Water"],
        "characteristics": ["Nutty","Sweet", "Refreshing"],
        "unlocked": False
    }
]

