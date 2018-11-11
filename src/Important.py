# plik z potrzebnymi zmiennymi

max_x = 20
max_y = 10
debug = False

ignore_keys = [27, 91]
move_keys = [65, 66, 67, 68]
look_keys = "wasd"
attack_keys = "ijkl"

amountItem = 10
amountGold = 5
amountMonster = 10
amountWall = 10
amountFood = 5

# not used yet
object_amount = {
    'Item': 10,
    'Monster': 10,
    'Gold': 5,
    'Wall': 10,
    'Food': 5,
    'StairsUp': 1,
    'StairsDown': 1,
    'Hero': 1
}

look_message = {
    'any object': "default",
    'Item': "It's a nice item! Pick it up",
    'Monster': "It's a scary monster! Attack with [i j k l]",
    'Gold': "It's a shiny gold! Pick it up",
    'Wall': "It's a wall! Maybe it can break..?",
    'Food': "Warm and healthy food",
    'StairsUp': "We can return to a safer place!",
    'StairsDown': "We can travel to a cooler place!",
    'Sword': "It's the lhe legnedary sword. Pick it up for extra damage. ",
    'Hero': "You need a mirror for that"
}

defeat_message = {
    'any object': "default.",
    'Item': ":(",
    'Monster': "Gaah!",
    'Gold': ":(",
    'Wall': "It hurt!",
    'Food': ":(((",
    'StairsUp': "Stairs are not impressed.",
    'StairsDown': "Stairs are not impressed.",
    'Sword': "The legnedary sword was weak after all.",
    'Hero': "You need an evil twin for that."
}

attack_message = {
    'any object': "default. ",
    'Item': "Don't attack items :( ",
    'Monster': "Grr! ",
    'Gold': "Don't attack gold :( ",
    'Wall': "It's falling on you! ",
    'Food': "Worst idea ever. ",
    'StairsUp': "Stairs are not impressed. ",
    'StairsDown': "Stairs are not impressed. ",
    'Sword': "The legnedary sword bends! ",
    'Hero': "You need an evil twin for that. "
}

collision_message = {
    'any object': "default",
    'Item': "Oh yeah!",
    'Monster': "Ouch!",
    'Gold': "Oh yeah!",
    'Wall': "Bump!",
    'Food': "Delicious!",
    'StairsUp': "Available only in full version.",
    'StairsDown': "Available only in full version.",
    'Sword': "The legnedary sword increases your damage. Nice.",
    'Hero': "You need a clone for that."
}
