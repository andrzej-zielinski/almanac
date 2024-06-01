import random

def roll_traits():
    traits = [
        "Jealous", "Desperate", "Violent", "Hysterical", "Skittish", "Fleeting", "Curious", "Deceptive", "Clever", "Probing", "Knowledgeable", "Charming", "Prophetic", "Insightful", "True", "Revelatory", "Guiding", "Instructive", "Reactive", "Territorial", "Dominant", "Insistent", "Bold", "Demanding", "Angry", "Volatile", "Aggressive", "Wild", "Savage", "Vengeful", "Mad", "Chaotic", "Bizarre", "Destructive", "Insane", "Vile"
    ]
    
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(traits[:6])  # Jealous, Desperate, Violent, Hysterical, Skittish, Fleeting
    elif roll == 2:
        return random.choice(traits[6:12])  # Curious, Deceptive, Clever, Probing, Knowledgeable, Charming
    elif roll == 3:
        return random.choice(traits[12:18])  # Prophetic, Insightful, True, Revelatory, Guiding, Instructive
    elif roll == 4:
        return random.choice(traits[18:24])  # Reactive, Territorial, Dominant, Insistent, Bold, Demanding
    elif roll == 5:
        return random.choice(traits[24:30])  # Angry, Volatile, Aggressive, Wild, Savage, Vengeful
    else:
        return random.choice(traits[30:])  # Mad, Chaotic, Bizarre, Destructive, Insane, Vile


def roll_effects():
    effects = [
        "Frost, Chill", "Cold wind", "Faint visions of the local past", "Electrical discharge", "Weird shadows", "Faint echoes", "Mist, Fog", "Rushing wind", "Intense visual echoes", "Intense magnetism", "Disturbing shadows", "Thunderous sounds", "Freezing fog", "Storm winds", "Pitch darkness", "Lightning", "Clutching shadows", "Voices in your head"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 3:
        return random.choice(effects[:6])  # Frost, Chill, Cold wind, Faint visions of the local past, Electrical discharge, Weird shadows, Faint echoes
    elif roll in [4, 5]:
        return random.choice(effects[6:12])  # Mist, Fog, Rushing wind, Intense visual echoes, Intense magnetism, Disturbing shadows, Thunderous sounds
    else:
        return random.choice(effects[12:])  # Freezing fog, Storm winds, Pitch darkness, Lightning, Clutching shadows, Voices in your head
