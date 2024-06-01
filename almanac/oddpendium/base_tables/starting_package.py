def starting_package(hp, highest_ability_score):
    """
    This function matches your highest Ability Score against your Hit Points
    to find your starting package. Weapons have their damage roll listed.
    Arcana are rolled randomly. If two characters would have the same equipment,
    the second character takes their starting package from the column to the left,
    or right if this is not possible.
    """

    table = {
        1: [
            "Sword (d6), Pistol (d6), Modern Armour, Sense nearby unearthly beings",     "Rifle (d8), Bayonet (d6), Lighter Boy Arcanum",     "Musket (d8), Modern Armour, Hound Arcanum",     "Club (d6), Throwing Knives Arcanum",     "Cane (d6), Acid, Spyglass Arcanum",     "Pistol Brace (d8), Canary, Ether",     "Musket (d8), Pocket-watch, Bomb",     "Halberd (d8), Fake Pistol, Artificial Lung",     "Garotte (d6), Musket (d8), Mute"
        ], 2: [
            "Musket (d8), Sword (d6), Flashbang, Sense nearby Arcana.",     "Musket (d8), Hatchet (d6), Hawk Arcanum",     "Hatchet (d6), Pistol (d6), Bolt-Cutters Arcanum",     "Musket (d8), Mule Arcanum",     "Pistol (d6), Bell, Steel Wire, Smoke-bomb",     "Longaxe (d8), Ferret, Fire Oil",     "Staff (d8), Tongs, Glue",     "Pistol (d6), Net, Prosthetic Leg, Trumpet",     "Pistol (d6), Grease, Hacksaw, One Arm"
        ], 3: [
            "Club (d6), Immunity to extreme heat and cold.",     "Musket (d8), Protective Gloves Arcanum",     "Musket (d8), Mallet, Marbles, Fancy Hat Arcanum",     "Pick-Axe (d6), Manacles Arcanum",     "Longaxe (d8), Throwing Axes, Fire Oil",     "Club (d6), Ether, Crowbar, Flute",     "Hatchet (d6), Net, Fire Oil, Burnt Face",     "Club (d6), Paint, Crowbar, Loud Lungs",     "Pistol (d6), Cigars, Poison, Fugitive"
        ], 4: [
            "Pistol (d6), Knife (d6), Telepathy if target fails wil save",     "Claymore (d8), Pistol (d6), 2 Acid Flasks Arcanum",     "Musket (d8), Bayonet (d6), Mutt with telepathic link.",     "Pistol (d6), Toxin-Immune Rocket",     "Pistol (d6), Saw, Animal Trap, Spyglass",     "Bow (d6), Knife (d6), Rocket, Fire Oil",     "Pistol (d6), Whip (d6), Cigars, Lost Eye",     "Musket (d8), Accordion, No Nose/Scent",     "Sword (d6), Shield Armour, Illiterate"
        ], 5: [
            "Blunderbuss (d8), Hatchet (d6), Mutt, Dreams show your undiscovered surroundings",     "Pistol Brace (d8), Steel Wire, Grappling Hook Arcanum",     "Machete (d6), Pistol Brace (d8), Talking Parrot, Never Sleep",     "Harpoon Gun (d8), Baton (d6), Acid, Slightly Magnetic",     "Dagger (d6), Fire Oil, Mirror",     "Sword & Dagger (d8), Magnifying Glass, Lost Eye",     "Pistol (d6), Acid, Animal Repellent, Prosthetic Hand",     "Sword (d6), Steel Wire, Ugly Mutation",     "Sword (d6), Ferret, Tattered Clothes, Debt (3g)"
        ], 6: [
            "Musket (d8), Hatchet (d6), Flashbang",     "Rifle (d8), Mace (d6), Eagle, Poison",     "Club (d6), 3 Bombs, Rocket, Darkvision",     "Maul (d8), Dagger (d6), Chain",     "Longaxe (d8), Rum, Bomb",     "Pistol (d6), Knife (d6), Bomb, Saw",     "Pistol (d6), Bomb, Shovel, Glowing Eyes",     "Staff (d8), Throwing Knives (d6)",     "Mace (d6), Pigeon, Disfigured"
        ]
    }

    if 3 <= highest_ability_score <= 9:
        column = 0
    elif highest_ability_score == 10:
        column = 1
    elif highest_ability_score == 11:
        column = 2
    elif highest_ability_score == 12:
        column = 3
    elif highest_ability_score == 13:
        column = 4
    elif highest_ability_score == 14:
        column = 5
    elif highest_ability_score == 15:
        column = 6
    elif highest_ability_score == 16:
        column = 7
    elif highest_ability_score == 17:
        column = 8
    elif highest_ability_score == 18:
        column = 9
    else:
        return "Invalid highest ability score"

    if 1 <= hp <= 6:
        return table[hp][column]
    else:
        return "Invalid HP"

# Example usage
print(starting_package(3, 10))
