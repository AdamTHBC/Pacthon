from Item_Effect import ItemEffect

################# Item #################
ItemName = {
    'potion1': "Healing Potion",
    'potion2': "Strength Potion",
    'potion3': "Antidote",
    'gem1': "Pearl",
    'gem2': "Diamond",
    'map': "World Map",
    'telescope': "telescope"
}

ItemGraphics = {
    'potion1': "( H )",
    'potion2': "( S )",
    'potion3': "( A )",
    'gem1': "((* )",
    'gem2': "[\|/]",
    'map': "/=x=/",
    'telescope': "-==<)"
}

ItemDescription = {
    'potion1': "A red, glowing healing potion. Drinking it restores 2 HP.",
    'potion2': "A black, hot strength potion. Drinking ir increases damage by 1 for 10 steps.",
    'potion3': "A milky, light antidote. Restores your status to normal.",
    'gem1': "A beautiful pearl without practical use.",
    'gem2': "A beautiful diamond without practical use.",
    'map': "A map of the known world, priceless during longer trips.",
    'telescope': "A handy telescope out of steel. Allows you watching places far, far away."
}

ItemPrice = {
    'potion1': 2,
    'potion2': 2,
    'potion3': 5,
    'gem1': 10,
    'gem2': 15,
    'map': 5,
    'telescope': 5
}

ItemEffectType = {
    'potion1': 'boost',
    'potion2': 'boost',
    'potion3': 'boost',
    'gem1': None,
    'gem2': None,
    'map': 'action',
    'telescope': 'action'
}

ItemEffect = {
    'potion1': ItemEffect('hp', 2),
    'potion2': ItemEffect('damage', 1, 10),
    'potion3': ItemEffect('status', -100),
    'gem1': None,
    'gem2': None,
    'map': ItemEffect('hp', 0),
    'telescope': ItemEffect('hp', 0)
}

############## Equipment ###############

DictionaryEquipment = {
    'armor1': "",
    'armor2': "",
    'sword1': "",
    'sword2': "",
    'helmet1': "",
    'helmet2': "",
    'shield1': "",
    'shield2': ""
}
