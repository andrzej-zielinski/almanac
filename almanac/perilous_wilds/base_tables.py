import random
from almanac.perilous_wilds.monster_traits import MONSTER_TRAIT
from almanac.perilous_wilds.data.creature import Creature
from almanac.perilous_wilds.data.steading import Steading, Population, Prosperity, Defenses, SteadingSize

# Simulate rolling a dice with n sides
def roll_dice(n):
    return random.randint(1, n)

def roll_dice(dice_type, num_dice=1, choose_best=False):
    """
    Simulates rolling a number of dice and returns the result.

    Parameters:
        dice_type (int): The type of dice to roll (e.g., 6 for d6).
        num_dice (int): The number of dice to roll.
        choose_best (bool): Whether to choose the highest roll if rolling more than one die.

    Returns:
        int: The result of the dice roll.
    """
    rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
    if choose_best:
        return max(rolls)
    return sum(rolls)

# Generate the region name
def generate_region_name():
    """
When you need to create a new region and need inspiration, roll one up. First, roll \n
1d12 for the region name template. Then, roll for each component of that template \n
until you have a complete name. Rewrite or re-roll any result you don’t like
    """
    terrains = ["Bay", "Bluffs", "Bog", "Cliffs", "Desert", "Downs", "Dunes", "Expanse", "Fells", "Fen", "Flats", "Foothills",
                "Forest", "Groves", "Heath", "Heights", "Hills", "Hollows", "Jungle", "Lake", "Lowland", "March", "Marsh",
                "Meadows", "Moor", "Morass", "Mounds", "Mountains", "Peaks", "Plains", "Prairie", "Quagmire", "Range",
                "Reach", "Sands", "Savanna", "Scarps", "Sea", "Slough", "Sound", "Steppe", "Swamp", "Sweep", "Teeth", "Thicket",
                "Upland", "Wall", "Waste", "Wasteland", "Woods"]
    adjectives = ["Ageless", "Ashen", "Black", "Blessed", "Blighted", "Blue", "Broken", "Burning", "Cold", "Cursed", "Dark",
                "Dead", "Deadly", "Deep", "Desolate", "Diamond", "Dim", "Dismal", "Dun", "Eerie", "Endless", "Fallen", "Far",
                "Fell", "Flaming", "Forgotten", "Forsaken", "Frozen", "Glittering", "Golden", "Green", "Grim", "Holy",
                "Impassable", "Jagged", "Light", "Long", "Misty", "Perilous", "Purple", "Red", "Savage", "Shadowy",
                "Shattered", "Shifting", "Shining", "Silver", "White", "Wicked", "Yellow"]
    nouns = ["Ash", "Bone", "Darkness", "Dead", "Death", "Desolation", "Despair", "Devil", "Doom", "Dragon", "Fate", "Fear",
            "Fire", "Fury", "Ghost", "Giant", "God", "Gold", "Heaven", "Hell", "Honor", "Hope", "Horror", "King", "Life",
            "Light", "Lord", "Mist", "Peril", "Queen", "Rain", "Refuge", "Regret", "Savior", "Shadow", "Silver", "Skull",
            "Sky", "Smoke", "Snake", "Sorrow", "Storm", "Sun", "Thorn", "Thunder", "Traitor", "Troll", "Victory", "Witch"]

    template_roll = roll_dice(12)
    if 1 <= template_roll <= 4:
        return f"{random.choice(adjectives)} {random.choice(terrains)}"
    elif 5 <= template_roll <= 6:
        return f"{random.choice(terrains)} of the {random.choice(nouns)}"
    elif 7 <= template_roll <= 8:
        return f"The {random.choice(terrains)} {random.choice(adjectives)}"
    elif 9 <= template_roll <= 10:
        return f"{random.choice(nouns)} {random.choice(terrains)}"
    elif template_roll == 11:
        return f"{random.choice(nouns)}'s {random.choice(adjectives)} {random.choice(terrains)}"
    elif template_roll == 12:
        return f"{random.choice(adjectives)} {random.choice(terrains)} of the {random.choice(nouns)}"

# Generate the place name
def generate_place_name() -> str:
    """
When you need to create a new place and are at a loss, roll one up. First, roll 1d12 \n
for the place name template. Then, roll for each component of that template until \n
you have a complete name. Rewrite or re-roll any result you don’t like. 
    """
    places = ["Barrier", "Beach", "Bowl", "Camp", "Cave", "Circle", "City", "Cliff", "Crater", "Crossing", "Crypt",
              "Den", "Ditch", "Falls", "Fence", "Field", "Fort", "Gate", "Grove", "Hill", "Hole", "Hut", "Keep", "Lake",
              "Marsh", "Meadow", "Mountain", "Pit", "Post", "Ridge", "Ring", "Rise", "Road", "Rock", "Ruin", "Shrine",
              "Spire", "Spring", "Stone", "Tangle", "Temple", "Throne", "Tomb", "Tower", "Town", "Tree", "Vale", "Valley",
              "Village", "Wall"]
    adjectives = ["Ancient", "Ashen", "Black", "Bloody", "Blue", "Bright", "Broken", "Burning", "Clouded", "Copper",
                  "Cracked", "Dark", "Dead", "Doomed", "Endless", "Fallen", "Far", "Fearsome", "Floating", "Forbidden",
                  "Frozen", "Ghostly", "Gloomy", "Golden", "Grim", "Hidden", "High", "Iron", "Jagged", "Lonely", "Lost",
                  "Low", "Near", "Petrified", "Red", "Screaming", "Sharp", "Shattered", "Shifting", "Shining", "Shivering",
                  "Shrouded", "Silver", "Stalwart", "Stoney", "Sunken", "Thorny", "Thundering", "White", "Withered"]
    nouns = ["Arm", "Ash", "Blood", "Child", "Cinder", "Corpse", "Crystal", "Dagger", "Death", "Demon", "Devil", "Doom",
             "Eye", "Fear", "Finger", "Fire", "Foot", "Ghost", "Giant", "Goblin", "God", "Gold", "Hand", "Head", "Heart",
             "Hero", "Hope", "King", "Knave", "Knight", "Muck", "Mud", "Priest", "Queen", "Sailor", "Silver", "Skull",
             "Smoke", "Souls", "Spear", "Spirit", "Stone", "Sword", "Thief", "Troll", "Warrior", "Water", "Witch", "Wizard"]

    template_roll = roll_dice(12)
    if 1 <= template_roll <= 2:
        return f"The {random.choice(places)}"
    elif 3 <= template_roll <= 4:
        return f"The {random.choice(adjectives)} {random.choice(places)}"
    elif 5 <= template_roll <= 6:
        return f"The {random.choice(places)} of the {random.choice(nouns)}"
    elif 7 <= template_roll <= 8:
        return f"The {random.choice(nouns)}'s {random.choice(places)}"
    elif 9 <= template_roll <= 10:
        return f"{random.choice(places)} of the {random.choice(adjectives)} {random.choice(nouns)}"
    elif 11 <= template_roll <= 12:
        return f"The {random.choice(adjectives)} {random.choice(nouns)}"
    return "Invalid roll"

def roll_for_treasure(monster_damage_die, monster_traits=[]) -> str:
    """
    Decides the treasure based on the monster's damage die and traits.

    Parameters:
        monster_damage_die (int): The damage die type for the monster (e.g., 6 for d6).
        monster_traits (list): List of special traits the monster may have.

    Returns:
        str: The description of the treasure found.
    """
    # Determine extra dice based on traits
    extra_dice = 0
    best_of_two = False

    for trait in monster_traits:
        if trait == 'Hoarder':
            best_of_two = True
        elif trait in ['Lord over others', 'Ancient and noteworthy']:
            extra_dice += 1
        elif trait == 'Far from home':
            extra_dice += 6  # adding directly as rations

    # Roll dice
    num_dice = 1 + extra_dice
    damage_die_roll = roll_dice(monster_damage_die, num_dice=num_dice, choose_best=best_of_two)

    # Consult the treasure table
    return describe_treasure(damage_die_roll)

def describe_treasure(roll):
    """
    Returns a description of the treasure based on the roll number.

    Parameters:
        roll (int): The roll number.

    Returns:
        str: The description of the treasure.
    """
    treasures = {
        1: "A few coins, 2d8 or so",
        2: "A useful item",
        3: "Several coins, about 4d10",
        4: "A small valuable (gem, art), worth 2d10x10 coins, 0 weight",
        5: "Some minor magical trinket",
        6: "Useful clue (map, note, etc.)",
        7: "Bag of coins, 1d4x100, 1 weight per 100",
        8: "A small item (gem, art) of great value (2d6x100 coins, 0 weight)",
        9: "A chest of coins and other small valuables. 1 weight, worth 3d6x100 coins.",
        10: "A magical item or magical effect",
        11: "Many bags of coins, 2d4x100 or so",
        12: "A sign of office (crown, banner) worth at least 3d4x100 coins",
        13: "A large art item (4d4x100 coins, 1 weight)",
        14: "Unique item worth at least 5d4x100 coins",
        15: "Everything needed to learn a new spell, and roll again",
        16: "A portal or secret path (or directions to one), and roll again",
        17: "Something relating to one of the characters, and roll again",
        18: "A hoard: 1d10x1000 coins and 1d10x10 gems worth 2d6x100 each"
    }

    # Normalize roll within table range
    adjusted_roll = min(max(1, roll), 18)
    return treasures[adjusted_roll]

import random

def roll_item_detail():
    """
    Rolls for a specific item detail based on the type of item (utility or art).

    Returns:
        str: The specific type of item found.
    """
    # Roll once for general category (1-12)
    roll = random.randint(1, 12)

    # Define item types
    utility_items = [
        "key/lockpick", "potion/food", "clothing/cloak", "decanter/vessel/cup",
        "cage/box/coffer", "instrument/tool", "book/scroll", "weapon/staff/wand"
    ]
    art_items = [
        "trinket/charm", "painting/pottery", "ring/gloves", "carpet/tapestry",
        "statuette/idol", "flag/banner", "bracelet/armband", "necklace/amulet",
        "belt/harness", "hat/mask", "orb/sigil/rod", "crown/scepter"
    ]

    # Decide the category based on roll
    if roll <= 8:  # Utility items
        item_category = "Utility Item"
        specific_item = random.choice(utility_items)
    else:  # Art items
        item_category = "Art Item"
        specific_item = random.choice(art_items)

    return f"Category: {item_category}, Item: {specific_item}"

def find_treasure_multiple_rolls(num_rolls, monster_damage_die, monster_traits=[]):
    """
    Finds treasure by rolling multiple times and adjusting the value of each result.

    Parameters:
        num_rolls (int): The number of times to roll for treasure.
        monster_damage_die (int): The damage die type for the monster (e.g., 6 for d6).
        monster_traits (list): List of special traits the monster may have.

    Returns:
        list: Descriptions of the treasures found.

    Example usage
    ```python
num_rolls = 4
monster_damage_die = 6
monster_traits = [MONSTER_TRAIT.HOARDER.value]
treasures_found = find_treasure_multiple_rolls(num_rolls, monster_damage_die, monster_traits)
item_details = roll_item_detail()

print("Treasures Found:", treasures_found)
print("Item Details:", item_details)
```
    """
    treasure_results = []
    for _ in range(num_rolls):
        treasure = roll_for_treasure(monster_damage_die, monster_traits)
        # Adjust the value of the treasure if it includes coins
        if "coins" in treasure:
            parts = treasure.split()
            for i, part in enumerate(parts):
                if part.isdigit():
                    new_value = int(int(part) / num_rolls)
                    parts[i] = str(new_value)
            treasure = " ".join(parts)
        treasure_results.append(treasure)

    return treasure_results

import random

def roll_ability():
    abilities = [
        "bless/curse", "entangle/trap/snare", "poison/disease", "paralyze/petrify",
        "mimic/camouflage", "seduce/hypnotize", "dissolve/disintegrate", "Magic Type",
        "drain life/magic", "immunity: Element", "read/control minds"
    ]
    return random.choice(abilities)

def roll_activity():
    activities = [
        "laying trap/ambush", "fighting/at war", "prowling/on patrol", "hunting/foraging",
        "eating/resting", "crafting/praying", "traveling/relocating", "exploring/lost",
        "returning home", "building/excavating", "sleeping", "dying"
    ]
    return random.choice(activities)

def roll_adjective():
    adjectives = [
        "slick/slimy", "rough/hard/sharp", "smooth/soft/dull", "corroded/rusty",
        "rotten/decaying", "broken/brittle", "stinking/smelly", "weak/thin/drained",
        "strong/fat/full", "pale/poor/shallow", "dark/rich/deep", "colorful"
    ]
    return random.choice(adjectives)

def roll_age():
    ages = [
        "being born/built", "young/recent", "young/recent", "young/recent",
        "middle-aged", "middle-aged", "middle-aged", "old", "old",
        "ancient", "ancient", "pre-historic"
    ]
    return random.choice(ages)

def roll_alignment():
    alignments = [
        "Chaotic", "Chaotic", "Evil", "Evil", "Neutral", "Neutral", "Neutral", "Neutral",
        "Good", "Good", "Lawful", "Lawful"
    ]
    return random.choice(alignments)

def roll_aspect():
    aspects = [
        "power/strength", "trickery/dexterity", "time/constitution", "knowledge/intelligence",
        "nature/wisdom", "culture/charisma", "war/lies/discord", "peace/truth/balance",
        "hate/envy", "love/admiration", f"element: {roll_element()}"
    ]
    return random.choice(aspects)

def roll_condition():
    conditions = [
        "being built/born", "intact/healthy/stable", "intact/healthy/stable", "intact/healthy/stable",
        "occupied/active/alert", "occupied/active/alert", "occupied/active/alert", "worn/tired/weak", "worn/tired/weak",
        "vacant/lost", "ruined/defiled/dying", "disappeared/dead"
    ]
    return random.choice(conditions)

def roll_disposition():
    dispositions = [
        "attacking", "hostile/aggressive", "hostile/aggressive", "hostile/aggressive",
        "cautious/doubtful", "cautious/doubtful", "fearful/fleeing", "neutral", "neutral", "neutral",
        "curious/hopeful", "friendly"
    ]
    return random.choice(dispositions)

def roll_element():
    elements = [
        "air", "air", "earth", "earth", "fire", "fire", "water", "water",
        "life", "life", "death", "death"
    ]
    return random.choice(elements)

def roll_feature():
    features = [
        "heavily armored", "winged/flying", "winged/flying", "multiple heads/headless",
        "many eyes/one eye", "many limbs/tails", "tentacles/tendrils", f"aspect: {roll_aspect()}"
        f"element: {roll_element()}", f"magic type: {roll_magic_type}", f"oddity: {roll_oddity()}"
    ]
    return random.choice(features)

def roll_magic_type():
    magic_types = [
        "divination", "divination", "enchantment", "enchantment",
        "evocation", "evocation", "illusion", "illusion",
        "necromancy", "necromancy", "summoning", "summoning"
    ]
    return random.choice(magic_types)

def roll_no_appearing():
    appearances = [
        "Solitary (1)", "Solitary (1)", "Solitary (1)", "Solitary (1)",
        "Group (1d6+2)", "Group (1d6+2)", "Group (1d6+2)", "Group (1d6+2)", "Group (1d6+2)",
        "Horde (4d6 per wave)", "Horde (4d6 per wave)", "Horde (4d6 per wave)"
    ]
    return random.choice(appearances)

def roll_oddity():
    oddities = [
        "weird color/smell/sound", "geometric", "web/network/system", "crystalline/glass-like",
        "fungal", "gaseous/smokey", "mirage/illusion", "volcanic/explosive",
        "magnetic/repellant", "devoid of life", "unexpectedly alive"
    ]
    return random.choice(oddities)

def roll_orientation():
    orientations = [
        "down/earthward", "down/earthward", "north", "northeast", "east", "southeast",
        "south", "southwest", "west", "northwest", "up/skyward", "up/skyward"
    ]
    return random.choice(orientations)

def roll_ruination():
    ruinations = [
        "arcane disaster", "damnation/curse", "earthquake/fire/flood", "earthquake/fire/flood",
        "plague/famine/drought", "plague/famine/drought", "overrun by monsters", "overrun by monsters",
        "war/invasion", "war/invasion", "depleted resources", "better prospects elsewhere"
    ]
    return random.choice(ruinations)

def roll_size():
    sizes = [
        "Tiny", "Small", "Small", "medium-sized", "medium-sized", "medium-sized", 
        "medium-sized", "medium-sized", "medium-sized", "Large", "Large", "Huge"
    ]
    return random.choice(sizes)

def roll_tag():
    tags = [
        "Amorphous", "Cautious", "Construct", "Devious", "Intelligent", "Magical",
        "Organized", "Organized", "Planar", "Stealthy", "Terrifying"
    ]
    return random.choice(tags)

def roll_terrain():
    terrains = [
        "wasteland/desert", "flatland/plain", "flatland/plain", "wetland/marsh/swamp",
        "woodland/forest/jungle", "woodland/forest/jungle", "woodland/forest/jungle",
        "highland/hills", "highland/hills", "mountains", "mountains", f"oddity: {roll_oddity()}"
    ]
    return random.choice(terrains)

def roll_visibility():
    visibilities = [
        "buried/camouflaged/nigh invisible", "buried/camouflaged/nigh invisible",
        "partly covered/overgrown/hidden", "partly covered/overgrown/hidden", 
        "partly covered/overgrown/hidden", "partly covered/overgrown/hidden",
        "obvious/in plain sight", "obvious/in plain sight", "obvious/in plain sight",
        "visible at near distance", "visible at near distance", "visible at great distance/focal point"
    ]
    return random.choice(visibilities)

import random

def generate_creature():
    # Determine the main type of the creature
    creature_type_roll = random.randint(1, 12)
    if creature_type_roll <= 4:
        creature_category = 'Beast'
        subtable = random.randint(1, 12)
        if subtable <= 7:
            creature_specific = ['termite/tick/louse', 'snail/slug/worm', 'ant/centipede/scorpion',
                                 'snake/lizard', 'vole/rat/weasel', 'boar/pig', 'dog/fox/wolf'][subtable - 1]
        elif subtable <= 10:
            creature_specific = ['cat/lion/panther', 'deer/horse/camel', 'ox/rhino'][subtable - 8]
        else:
            creature_specific = ['bear/ape/gorilla', 'mammoth/dinosaur'][subtable - 11]
        additional_details = f"Activity: {roll_activity()}, Disposition: {roll_disposition()}, Number: {roll_no_appearing()}, Size: {roll_size()}"

    elif creature_type_roll <= 6:
        creature_category = 'Human'
        subtable = random.randint(1, 12)
        if subtable <= 7:
            creature_specific = ['halfling', 'goblin/kobold', 'dwarf/gnome', 'orc/hobgoblin/gnoll', 
                                 'half-elf/half-orc, etc.', 'elf'][subtable // 2 - 1]
        elif subtable <= 10:
            creature_specific = ['fey', 'catfolk/dogfolk', 'lizardfolk/merfolk', 'birdfolk', 'ogre/troll', 'cyclops/giant'][subtable - 8]
        else:
            creature_specific = ['centaur', 'werewolf/werebear', 'werecreature (human + Beast)', 
                                 'human + Beast', 'human + 2 Beasts'][subtable - 11]
        additional_details = f"Activity: {roll_activity()}, Alignment: {roll_alignment()}, Disposition: {roll_disposition()}, Number: {roll_no_appearing()}"

    elif creature_type_roll <= 8:
        creature_category = 'Humanoid'
        # Similar handling as 'Human' with potentially different logic or subtables
        creature_specific = "Adapted from fantasy species"
        additional_details = f"Activity: {roll_activity()}, Alignment: {roll_alignment()}, Disposition: {roll_disposition()}, Number: {roll_no_appearing()}"

    else:
        creature_category = 'Monster'
        subtable = random.randint(1, 12)
        if subtable <= 7:
            creature_specific = 'Common type of monster'
        elif subtable <= 10:
            creature_specific = 'Rare type of monster'
        else:
            creature_specific = 'Legendary type of monster'
        additional_details = f"Activity: {roll_activity()}, Alignment: {roll_alignment()}, Disposition: {roll_disposition()}, Number: {roll_no_appearing()}, Size: {roll_size()}"

    return Creature(category=creature_category, specifics=creature_specific, details=additional_details)


def roll_hazard():
    # Roll to determine the type of hazard
    hazard_type_roll = random.randint(1, 12)
    hazard = ""
    details = ""
    
    if hazard_type_roll <= 2:  # Unnatural hazards
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            hazard = "taint/blight/curse"
        elif sub_roll <= 8:
            hazard = "arcane trap/effect"
        elif sub_roll <= 11:
            hazard = "planar trap/effect"
        else:
            hazard = "divine"
            details = f"Aspect: {roll_aspect()}, Visibility: {roll_visibility()}"

    elif hazard_type_roll <= 10:  # Natural hazards
        sub_roll = random.randint(1, 12)
        if sub_roll <= 2:
            hazard = "blinding mist/fog"
        elif sub_roll <= 4:
            hazard = "bog/mire/quicksand"
        elif sub_roll <= 7:
            hazard = "pitfall/sinkhole/chasm"
        elif sub_roll <= 9:
            hazard = "poison/disease"
        elif sub_roll <= 11:
            hazard = "flood/fire/tornado"
        else:
            hazard = "Oddity"
            details = f"Oddity: {roll_oddity()}"

    else:  # Traps
        sub_roll = random.randint(1, 12)
        if sub_roll <= 2:
            hazard = "alarm"
        elif sub_roll <= 5:
            hazard = "ensnaring/paralyzing"
        elif sub_roll <= 8:
            hazard = "injurious (pit, etc.)"
        elif sub_roll <= 9:
            hazard = "gas/fire/poison"
        else:
            hazard = "ambush"
            # Assuming generate_creature returns a string describing the creature
            creature_description = generate_creature()
            details = f"Creature responsible: {creature_description}, Aspect: {roll_aspect()}, Visibility: {roll_visibility()}"

    result = f"Hazard Type: {hazard}"
    if details:
        result += f", Details: {details}"
    return result



def roll_unnatural_entity():
    # Roll to determine the type of unnatural entity
    entity_type_roll = random.randint(1, 12)
    
    if entity_type_roll <= 8:  # Undead entities
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            entity = "haunt/wisp"
        elif sub_roll <= 8:
            entity = "ghost/spectre"
        elif sub_roll == 9:
            entity = "banshee"
        elif sub_roll <= 11:
            entity = "wraith/wight"
        else:
            entity = "spirit lord/master"
        details = f"Ability: {roll_ability()}, Activity: {roll_activity()}, Alignment: {roll_alignment()}, Disposition: {roll_disposition()}"

    elif entity_type_roll <= 11:  # Planar entities
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            entity = "imp (Small)"
        elif sub_roll <= 6:
            entity = "lesser elemental"
        elif sub_roll <= 9:
            entity = "lesser demon/horror"
        elif sub_roll == 10:
            entity = "greater elemental"
        elif sub_roll == 11:
            entity = "greater demon/horror"
        else:
            entity = "devil/elemental lord"
        details = f"Ability: {roll_ability()}, Activity: {roll_activity()}, Alignment: {roll_alignment()}, Disposition: {roll_disposition()}, Element: {roll_element()}, Feature: {roll_feature()}, Tag: {roll_tag()}"

    else:  # Divine entities
        sub_roll = random.randint(1, 12)
        if sub_roll <= 5:
            entity = "agent"
        elif sub_roll <= 9:
            entity = "champion"
        elif sub_roll <= 11:
            entity = "army (Horde)"
        else:
            entity = "avatar"
        details = f"Ability: {roll_ability()}, Activity: {roll_activity()}, Alignment: {roll_alignment()}, Aspect: {roll_aspect()}, Disposition: {roll_disposition()}, Element: {roll_element()}, Feature: {roll_feature()}, Tag: {roll_tag()}"

    result = f"Unnatural Entity Type: {entity}, Details: {details}"
    return result

def roll_danger():
    # Roll to determine which function to call
    danger_roll = random.randint(1, 12)
    
    if danger_roll == 1:
        # Generate an unnatural entity
        result = roll_unnatural_entity()
    elif 2 <= danger_roll <= 6:
        # Generate a hazard
        result = roll_hazard()
    else:
        # Generate a creature
        result = generate_creature()

    return result

def generate_village(ruination: str = None) -> Steading:
    # Basic attributes of the village
    name = "Random Village"
    location = "Generic Location"
    size = SteadingSize.Village
    prosperity = Prosperity.Poor
    population = Population.Steady
    defenses = Defenses.Militia
    tags = []
    relations = {}

    # Optional enhancements based on kingdom or empire involvement
    roll = random.randint(1, 12)
    if roll <= 3:
        tags.append("Safe")
        defenses = Defenses.Defenseless  # Decrease in defenses
    elif roll <= 6:
        prosperity = Prosperity.Moderate  # Increase prosperity
        tags.append("Resource (GM choice)")
        relations["Enmity"] = ["Steading of GM's choice"]
    elif roll <= 8:
        relations["Oath"] = ["Protector Steading"]
        defenses = Defenses.Watch  # Increase in defenses
    elif roll <= 10:
        relations["Trade"] = ["Steading on major road"]
        prosperity = Prosperity.Moderate
    elif roll == 11:
        tags.extend(["Personage (wizard)", "Blight (arcane creatures)"])
    else:
        tags.extend(["Divine", "History (GM choice)"])

    # Choose 1 problem
    roll = random.randint(1, 12)
    if roll <= 2:
        tags.append("Need (food)")
    elif roll <= 4:
        tags.extend(["Religious (deity)", "Enmity (steading of opposing deity)"])
    elif roll <= 6:
        population = Population.Shrinking  # Decrease in population
        prosperity = Prosperity.Dirt  # Decrease in prosperity if fought to the end
        defenses = Defenses.Defenseless  # Decrease in defenses if lost
    elif roll <= 8:
        tags.extend(["Blight (that monster)", "Need (adventurers)"])
    elif roll <= 10:
        population = Population.Growing
        tags.append("Lawless")
    else:
        prosperity = Prosperity.Dirt
        tags.append("Dwarven or Elven or other non-human")

    # Create the Steading instance
    village = Steading(
        name=name,
        location=location,
        size=size,
        prosperity=prosperity,
        population=population,
        defenses=defenses,
        tags=tags,
        relations=relations
    )
    if ruination:
        village.add_tag(f"Ruined: {ruination}")
    return village

def generate_town(ruination: str = None) -> Steading:
    # Basic attributes of the town
    name = "Random Town"
    location = "Generic Region"
    size = SteadingSize.Town
    prosperity = Prosperity.Moderate
    population = Population.Steady
    defenses = Defenses.Watch
    tags = []
    relations = {"Trade": ["Place 1 of GM's choice", "Place 2 of GM's choice"]}

    # Optional enhancements based on Trade involvement
    roll = random.randint(1, 12)
    if roll == 1:
        population = Population.Booming
        tags.append("Lawless")
    elif roll <= 3:
        tags.append("Market")
        prosperity = Prosperity.Wealthy  # Increase prosperity
    elif roll <= 5:
        relations["Oath"] = ["Protector Steading"]
        defenses = Defenses.Garrison  # Increase in defenses
    elif roll <= 7:
        tags.append("Power (divine)")
    elif roll <= 10:
        tags.append(f"Craft (your choice), Resource (required for that craft)")
    else:
        defenses = Defenses.Garrison  # Increase in defenses

    # Choose 1 problem
    roll = random.randint(1, 12)
    if roll <= 2:
        tags.append("Need (vital resource)")
        relations["Trade"].append("Steading with that resource")
    elif roll <= 4:
        relations["Oath"] = ["GM's choice"]
        defenses = Defenses.Militia  # Decrease in defenses
    elif roll <= 6:
        tags.extend(["Personage (the outlaw)", "Enmity (steading preyed upon)"])
    elif roll <= 8:
        tags.append("Exotic (good/service)")
        relations["Enmity"] = ["Steading with ambition"]
    elif roll <= 10:
        population = Population.Shrinking  # Decrease in population
    else:
        population = Population.Growing
        tags.append("Lawless")

    # Create the Steading instance
    town = Steading(
        name=name,
        location=location,
        size=size,
        prosperity=prosperity,
        population=population,
        defenses=defenses,
        tags=tags,
        relations=relations
    )
    if ruination:
        town.add_tag(f"Ruined: {ruination}")
    return town

def generate_keep(ruination: str = None) -> Steading:
    # Basic attributes of the keep
    name = "Random Keep"
    location = "Strategic Position"
    size = SteadingSize.Keep
    prosperity = Prosperity.Poor
    population = Population.Shrinking
    defenses = Defenses.Guard
    tags = ["Need (supplies)"]
    relations = {
        "Trade": ["Place with supplies"],  # GM to specify the place
        "Oath": ["GM's choice"]  # Oath to a higher authority or neighboring steading
    }

    # Optional enhancements based on feudal relationships
    roll = random.randint(1, 12)
    if roll <= 2:
        prosperity = Prosperity.Moderate  # Increase prosperity
        tags.append("Power (political)")
    elif roll <= 4:
        tags.append("Personage (skilled commander)")
        defenses = Defenses.Garrison  # Upgrade in defenses
    elif roll <= 6:
        prosperity = Prosperity.Moderate  # Increase prosperity
        tags.append("Guild (trade)")
    elif roll <= 8:
        tags.append("Arcane")
        population = Population.Exodus  # Decrease in population
    elif roll <= 10:
        tags.remove("Need (supplies)")  # Remove the need for supplies due to fertile land
    else:
        defenses = Defenses.Garrison  # Strengthen defenses
        relations["Enmity"] = ["Steading across the border"]

    # Choose 1 problem
    roll = random.randint(1, 12)
    if roll <= 3:
        tags.append("Safe")
        population = Population.Exodus  # Further decrease in population
    elif roll == 4:
        relations["Enmity"] = ["Former occupiers"]
    elif roll == 5:
        tags.append("Lawless")
    elif roll == 6:
        tags.append("Blight (specific threat)")
    elif roll == 7:
        tags.extend(["History (battle)", "Blight (restless spirits)"])
    elif roll == 8:
        tags.append("Need (skilled recruits)")
    elif roll <= 10:
        population = Population.Exodus  # Disease reduces population
    else:
        population = Population.Growing
        tags.append("Lawless")

    # Create the Steading instance
    keep = Steading(
        name=name,
        location=location,
        size=size,
        prosperity=prosperity,
        population=population,
        defenses=defenses,
        tags=tags,
        relations=relations
    )
    if ruination:
        keep.add_tag(f"Ruined: {ruination}")
    return keep

def generate_city(ruination: str = None):
    # Basic attributes of the city
    name = "Random City"
    location = "Central Region"
    size = SteadingSize.City
    prosperity = Prosperity.Moderate
    population = Population.Steady
    defenses = Defenses.Guard
    tags = ["Market", "Guild (GM's choice)"]
    relations = {"Oath": ["Steading 1 of GM's choice", "Steading 2 of GM's choice"]}  # Multiple oaths to various steadings

    # Optional enhancements based on the city's strategic and political role
    roll = random.randint(1, 12)
    if roll <= 3:
        defenses = Defenses.Watch  # Upgrade in defenses due to permanent structures like walls
        relations["Oath"].append("GM's choice for additional fealty")
    elif roll <= 6:
        tags.append("Personage (the ruler)")
        tags.append("Power (political)")
    elif roll == 7:
        tags.append("Diverse (Dwarven or Elven or both)")
    elif roll <= 10:
        relations["Trade"] = ["Every nearby steading"]
        prosperity = Prosperity.Wealthy  # Increase in prosperity due to trade hub status
    elif roll == 11:
        tags.extend(["History (ancient ruins)", "Divine"])
    else:
        tags.extend(["Arcane", "Craft (your choice)", "Power (arcane)"])

    # Choose 1 problem
    roll = random.randint(1, 12)
    if roll <= 3:
        population = Population.Growing  # Increase in population outgrowing resources
        tags.append("Need (food)")
    elif roll <= 6:
        relations["Enmity"] = ["Nearby steadings"]
        defenses = Defenses.Garrison  # Increase in defenses due to territorial ambitions
    elif roll <= 8:
        defenses = Defenses.Militia  # Decrease in defenses, ruled by a theocracy
        tags.append("Power (divine)")
    elif roll <= 10:
        population = Population.Growing  # Increase in population due to democratic governance
        defenses = Defenses.Militia  # Decrease in defenses, ruled by the people
    elif roll == 11:
        defenses = Defenses.Garrison  # Supernatural defenses increase
        tags.append("Blight (related supernatural creatures)")
    else:
        tags.extend(["Arcane", "Personage (watcher of place of power)", "Blight (arcane creatures)"])

    # Create the Steading instance
    city = Steading(
        name=name,
        location=location,
        size=size,
        prosperity=prosperity,
        population=population,
        defenses=defenses,
        tags=tags,
        relations=relations
    )
    if ruination:
        city.add_tag(f"Ruined: {ruination}")
    return city

# Function to select and run a steading generator based on a dice roll
def generate_steading(ruination: str = None, offset: int = 0):
    roll = random.randint(1+offset, 12)
    if 1 <= roll <= 5 or 9 <= roll <= 11:
        return generate_village(ruination)  # Village is called for rolls 1-5 and 9-11
    elif 6 <= roll <= 8:
        return generate_town(ruination)     # Town is called for rolls 6-8
    elif roll == 12:
        return generate_city(ruination)     # City is called for roll 12
    else:
        return "Invalid roll"      # This line is actually not necessary as all cases are covered

def roll_unnatural_feature():
    roll = random.randint(1, 12)
    if roll <= 9:  # Arcane outcomes
        sub_roll = random.randint(1, 12)
        if sub_roll <= 2:
            result = "Arcane residue"
        elif sub_roll <= 5:
            result = "Arcane blight"
        elif sub_roll <= 7:
            result = "Arcane alteration/mutation"
        elif sub_roll <= 10:
            result = "Arcane enchantment"
        else:
            result = "Arcane source/repository"
        result += f", Alignment: {roll_alignment()}, Magic Type: {roll_magic_type()}"

    elif roll <= 11:  # Planar outcomes
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            result = "Planar distortion/warp"
        elif sub_roll <= 8:
            result = "Planar portal/gate"
        elif sub_roll <= 10:
            result = "Planar rift/tear"
        else:
            result = "Planar outpost"
        result += f", Alignment: {roll_alignment()}, Element: {roll_element()}"

    else:  # Divine outcomes
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            result = "Divine mark/sign"
        elif sub_roll <= 6:
            result = "Divine cursed place"
        elif sub_roll <= 9:
            result = "Divine hallowed place"
        elif sub_roll <= 11:
            result = "Divine watched place"
        else:
            result = "Divine presence"
        result += f", Alignment: {roll_alignment()}, Aspect: {roll_aspect()}"

    return result

def roll_resource():
    sub_roll = random.randint(1, 12)
    if sub_roll <= 4:
        resource = "Game/Fruit/Vegetable"
    elif sub_roll <= 6:
        resource = "Herb/Spice/Dye source"
    elif sub_roll <= 9:
        resource = "Timber/Stone"
    elif sub_roll <= 11:
        resource = "Ore (e.g., copper, iron)"
    else:
        resource = "Precious Metal/Gems"
    return resource

def roll_natural_feature():
    roll = random.randint(1, 12)
    if roll <= 2:  # Lair
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            feature = "Burrow"
        elif sub_roll <= 7:
            feature = "Cave/Tunnels"
        elif sub_roll <= 9:
            feature = "Nest/Aerie"
        elif sub_roll == 10:
            feature = "Hive"
        else:
            feature = "Ruins"
        creature = generate_creature()
        visibility = roll_visibility()
        return f"Lair: {feature}, Responsible Creature: {creature}, Visibility: {visibility}"

    elif roll <= 4:  # Obstacle
        sub_roll = random.randint(1, 12)
        if sub_roll <= 5:
            feature = "Difficult ground"
        elif sub_roll <= 8:
            feature = "Cliff/Crevasse/Chasm"
        elif sub_roll <= 10:
            feature = "Ravine/Gorge"
        else:
            feature = "Oddity"
        return f"Obstacle: {feature}, Visibility: {roll_visibility()}"

    elif roll <= 7:  # Terrain Change
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            feature = "Different terrain type"
        elif sub_roll <= 6:
            feature = "Crevice/Hole/Pit/Cave"
        elif sub_roll <= 8:
            feature = "Altitude Change"
        elif sub_roll <= 10:
            feature = "Canyon/Valley"
        else:
            feature = "Rise/Peak"
        return f"Terrain Change: {feature}"

    elif roll <= 9:  # Water Feature
        sub_roll = random.randint(1, 12)
        if sub_roll == 1:
            feature = "Spring/Hot Spring"
        elif sub_roll == 2:
            feature = "Waterfall/Geyser"
        elif sub_roll <= 6:
            feature = "Creek/Stream/Brook"
        elif sub_roll <= 8:
            feature = "Pond/Lake"
        elif sub_roll <= 10:
            feature = "River"
        else:
            feature = "Sea/Ocean"
        return f"Water Feature: {feature}"

    elif roll <= 11:  # Landmark
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            feature = "Water-based (e.g., waterfall, geyser)"
        elif sub_roll <= 6:
            feature = "Plant-based (e.g., ancient tree, giant flowers)"
        elif sub_roll <= 10:
            feature = "Earth-based (e.g., peak, formation, crater)"
        else:
            feature = f"Oddity: {roll_oddity()}"
        return f"Landmark: {feature}"

    else:  # Resource
        resource = roll_resource()
        size = "Varied size"
        visibility = roll_visibility()
        return f"Resource: {resource}, Size: {size}, Visibility: {visibility}"
    
def roll_evidence():
    roll = random.randint(1, 12)
    if roll <= 6:  # Tracks/Spoor
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            evidence = "faint/unclear tracks"
        elif sub_roll <= 6:
            evidence = "definite/clear tracks"
        elif sub_roll <= 8:
            evidence = "multiple tracks"
        elif sub_roll <= 10:
            evidence = "signs of violence"
        else:
            evidence = "trail of blood/other"
        age = roll_age()
        creature = generate_creature()
        return f"Tracks/Spoor: {evidence}, Age: {age}, Creature Responsible: {creature}"

    elif roll <= 10:  # Remains/Debris
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            evidence = "bones"
        elif sub_roll <= 7:
            evidence = "corpse/carcass"
        elif sub_roll <= 9:
            evidence = "site of violence"
        elif sub_roll == 10:
            evidence = "junk/refuse"
        elif sub_roll == 11:
            evidence = "lost supplies/cargo"
        else:
            evidence = "tools/weapons/armor"
        age = roll_age()
        visibility = roll_visibility()
        return f"Remains/Debris: {evidence}, Age: {age}, Visibility: {visibility}"

    else:  # Stash/Cache
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            evidence = "trinkets/coins"
        elif sub_roll <= 5:
            evidence = "tools/weapons/armor"
        elif sub_roll <= 7:
            evidence = "map"
        elif sub_roll <= 9:
            evidence = "food/supplies"
        else:
            evidence = "treasure"
        return f"Stash/Cache: {evidence}"
    

def roll_structure():
    roll = random.randint(1, 12)
    if roll == 1:  # Enigmatic
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            structure = "Earthworks"
        elif sub_roll <= 8:
            structure = "Megalith"
        elif sub_roll <= 11:
            structure = "Statue/Idol/Totem"
        else:
            structure = f"oddity: {roll_oddity()}"
        age = roll_age()
        size = roll_size()
        visibility = roll_visibility()
        return f"Enigmatic Structure: {structure}, Age: {age}, Size: {size}, Visibility: {visibility}"

    elif roll <= 3:  # Infrastructure
        sub_roll = random.randint(1, 12)
        if sub_roll <= 4:
            structure = "Track/Path"
        elif sub_roll <= 8:
            structure = "Road"
        elif sub_roll <= 10:
            structure = "Bridge/Ford"
        elif sub_roll == 11:
            structure = "Mine/Quarry"
        else:
            structure = "Aqueduct/Canal/Portal"
        creature = generate_creature()
        return f"Infrastructure: {structure}, Responsible Creature: {creature}"

    elif roll == 4:  # Dwelling
        sub_roll = random.randint(1, 12)
        if sub_roll <= 3:
            structure = "Campsite"
        elif sub_roll <= 6:
            structure = "Hovel/Hut"
        elif sub_roll <= 8:
            structure = "Farm"
        elif sub_roll <= 10:
            structure = "Inn/Roadhouse"
        else:
            structure = "Tower/Keep/Estate"
        creature = generate_creature()
        return f"Dwelling: {structure}, Responsible Creature: {creature}"

    elif roll <= 6:  # Burial/Religious
        sub_roll = random.randint(1, 12)
        if sub_roll <= 2:
            structure = "Grave Marker/Barrow"
        elif sub_roll <= 4:
            structure = "Graveyard/Necropolis"
        elif sub_roll <= 6:
            structure = "Tomb/Crypt"
        elif sub_roll <= 9:
            structure = "Shrine"
        elif sub_roll <= 11:
            structure = "Temple/Retreat"
        else:
            structure = "Great Temple"
        creature = generate_creature()
        alignment = roll_alignment()
        aspect = roll_aspect()
        return f"Burial/Religious: {structure}, Responsible Creature: {creature}, Alignment: {alignment}, Aspect: {aspect}"

    elif roll <= 8:  # Steading
        return generate_steading()

    else:  # Ruin
        sub_roll = random.randint(1, 12)
        if sub_roll <= 2:
            # Reroll with new range for Infrastructure
                
            sub_sub_roll = random.randint(7, 12)
            if sub_sub_roll <= 4:
                structure = "Track/Path"
            elif sub_sub_roll <= 8:
                structure = "Road"
            elif sub_sub_roll <= 10:
                structure = "Bridge/Ford"
            elif sub_sub_roll == 11:
                structure = "Mine/Quarry"
            else:
                structure = "Aqueduct/Canal/Portal"
            creature = generate_creature()
            ruination = roll_ruination()
            return f"Infrastructure: {structure}, Responsible Creature: {creature}, Ruination: {ruination}"
        elif sub_roll <= 4:
            sub_roll = random.randint(5, 12)
            if sub_roll <= 3:
                structure = "Campsite"
            elif sub_roll <= 6:
                structure = "Hovel/Hut"
            elif sub_roll <= 8:
                structure = "Farm"
            elif sub_roll <= 10:
                structure = "Inn/Roadhouse"
            else:
                structure = "Tower/Keep/Estate"
            creature = generate_creature()
            ruination = roll_ruination()
            return f"Dwelling: {structure}, Responsible Creature: {creature}, Ruination: {ruination}"
        elif sub_roll <= 6:
            sub_roll = random.randint(5, 12)
            if sub_roll <= 2:
                structure = "Grave Marker/Barrow"
            elif sub_roll <= 4:
                structure = "Graveyard/Necropolis"
            elif sub_roll <= 6:
                structure = "Tomb/Crypt"
            elif sub_roll <= 9:
                structure = "Shrine"
            elif sub_roll <= 11:
                structure = "Temple/Retreat"
            else:
                structure = "Great Temple"
            creature = generate_creature()
            alignment = roll_alignment()
            aspect = roll_aspect()
            ruination = roll_ruination()
            return f"Burial/Religious: {structure}, Responsible Creature: {creature}, Alignment: {alignment}, Aspect: {aspect}, Ruination: {ruination}"
        elif sub_roll <= 8:
            # Call the steading generation
            return generate_steading(ruination=ruination, offset=2)
        else:
            # Generate a dungeon
            return generate_steading()
            # return generate_dungeon()

def generate_place_tags():
    # Climate tags
    climates = ["Frigid", "Temperate", "Temperate", "Torrid"]
    climate_tag = random.choice(climates)
    
    # Terrain type tags
    terrains = ["Forest", "Farmland", "Mountains", "Woods", "Hunting Grounds", "Hills", "Grassland", "Swamp"]
    terrain_tag = random.choice(terrains)
    
    # Danger level tags
    danger_levels = ["Safe", "Unsafe", "Perilous"]
    danger_tag = random.choice(danger_levels)
    
    # Alignment tags
    alignments = ["Neutral", "Lawful", "Chaotic", "Evil"]
    alignment_tag = random.choice(alignments)
    
    # Other specific tags
    other_positive_tags = ["Civilized", "Defensible", "Enchanted", f"Holy (aspect: {roll_aspect()})", "Property (faction of GM's choice)", f"Resource ({roll_resource()})"]
    other_positive_tag = random.choice(other_positive_tags)

    # Other specific tags
    other_negative_tags = ["Barren", "Blighted", "Contested (faction of GMs choice)", "Difficult", "Unholy"]
    other_negative_tag = random.choice(other_negative_tags)
    other_tags = f"{other_positive_tag}, {other_negative_tag}"
    
    # Combining all tags into a single string
    tags = f"Climate: {climate_tag}, Terrain: {terrain_tag}, Danger: {danger_tag}, Alignment: {alignment_tag}, Other: {other_tags}"
    return tags
