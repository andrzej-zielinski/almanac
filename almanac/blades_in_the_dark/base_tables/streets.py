import random

def roll_props():
    props = [
        "Nets, Ropes", "Crates, Boxes", "Cables, Chains", "Drain Pipes", "Water Pump", "Oil Drums", "Brick Pile", "Iron Bars", "Wooden Boards", "Cut Stones", "Loose Rocks", "Cement Buckets", "Sewer Grate", "Rotting Refuse", "Mud Puddles", "Discarded Junk", "Carrion & Crows", "Sodden Trash", "Carriages", "Push Carts", "Moored Boats", "Cargo Barge", "Gondolas", "Wagons", "Crane & Pulleys", "Cargo Bales", "Metal Ingots", "Industrial Forge", "Coal / Fuel", "Waste Bins", "Street Lamps", "Electric Wires", "Junction Boxes", "Spotlight Tower", "Clock Tower", "Messenger Post", "Withered Trees", "Monument", "Fountain", "Mossy Ruin", "Collapsed Bldg.", "Flimsy Hovel", "Barricade", "Gate", "Checkpoint", "Piled Rubble", "Canal Lock", "Lightning Barrier", "Food Stall", "Vendor Stall", "Barrels, Casks", "Makeshift Shrine", "News Stand", "Stockade"
    ]
    return random.choice(props)


def roll_mood():
    moods = [
        "Dark or Cold", "Bright or Lively", "Quiet or Refined", "Abandoned or Decrepit", "Cramped or Noisy", "Cozy or Comfortable"
    ]
    return random.choice(moods)


def roll_sights():
    sights = [
        "Rain Slick, Oil Slick", "Dancing Shadows, Flickering Lights", "Mist, Fog, Frost", "Fleeting Shapes, Echoes in the Ghost Field", "Soot, Ash Clouds, Grime", "Crackling Electricity, Wires, Mechanisms"
    ]
    return random.choice(sights)

def roll_sounds():
    sounds = [
        "Machinery, Workers", "Fluttering Cloth, Howling Wind", "Laughter, Song, Music", "Whispers, Echoes, Strange Voices", "Thunder, Driving Rain", "Bells, Clock Chimes, Harbor Horns"
    ]
    return random.choice(sounds)

def roll_smells():
    smells = [
        "Cook Fires, Furnaces", "Damp Wood, Decay, Refuse", "Animals, Hides, Blood", "Chemicals, Distillates, Fumes", "Rain Water, Ocean", "Ozone, Electroplasmic Discharges"
    ]
    return random.choice(smells)


def roll_impressions():
    f = random.choice([roll_smells, roll_sights, roll_sounds])
    return f()

def roll_use():
    uses = [
        "Residential", "Crafts", "Labor", "Shops", "Trade", "Hospitality", "Law, Government", "Public Space", "Power", "Manufacture", "Transportation", "Leisure", "Vice", "Entertainment", "Storage", "Cultivation", "Academic", "Artists"
    ]
    roll = random.randint(1, 6)
    if roll <= 3:
        return random.choice(uses[:6])  # Residential, Crafts, Labor, Shops, Trade, Hospitality
    elif roll in [4, 5]:
        return random.choice(uses[6:12])  # Law, Government, Public Space, Power, Manufacture, Transportation, Leisure
    else:
        return random.choice(uses[12:])  # Vice, Entertainment, Storage, Cultivation, Academic, Artists


def roll_type():
    types = [
        "Narrow Lane", "Tight Alley", "Twisting Street", "Rough Road", "Bridge", "Waterway", "Closed Court", "Open Plaza", "Paved Avenue", "Tunnel", "Wide Boulevard", "Roundabout", "Elevated", "Flooded", "Suspended", "Subterranean", "Floating", "Private, Gated"
    ]
    roll = random.randint(1, 6)
    if roll <= 3:
        return random.choice(types[:6])  # Narrow Lane, Tight Alley, Twisting Street, Rough Road, Bridge, Waterway
    elif roll in [4, 5]:
        return random.choice(types[6:12])  # Closed Court, Open Plaza, Paved Avenue, Tunnel, Wide Boulevard, Roundabout
    else:
        return random.choice(types[12:])  # Elevated, Flooded, Suspended, Subterranean, Floating, Private, Gated

def roll_detail():
    details = [
        "Metal Supports", "Ironwork", "Gates, Fences", "Belching Chimneys", "Metal Grates, Hatches, Doors", "Clockwork Mechanisms", "Rigging, Cables", "Stairs, Ramps, Terraces", "Wooden Scaffolds", "Skyways", "Rooftop Spaces", "Rails, Train Cars", "Hidden Passages", "Banners, Pennants", "Festival Decorations", "Crowd, Parade, Riot", "Street Performers", "Makeshift Stalls, Shelters", "Crisscrossing Routes", "Gang Markings", "Patrol Posts", "Lookouts", "Stocks, Public Punishment", "Street Crier, Visionary", "News Stand, Public Notices", "Stray Animals", "Landscaping", "Muck, Mire", "Construction, Demolition", "Foul Runoff, Fumes, Smoke", "Orphans, Beggars", "Ancient Ruin", "Leering Gargoyles", "Spirit Chimes, Wards", "Eerie Emptiness", "Quarantine, Lockdown", "Shrine Offerings"
    ]
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(details[:6])  # Metal Supports, Ironwork, Gates, Fences, etc.
    elif roll == 2:
        return random.choice(details[6:12])  # Stairs, Ramps, Terraces, etc.
    elif roll == 3:
        return random.choice(details[12:18])  # Banners, Pennants, Festival Decorations, etc.
    elif roll == 4:
        return random.choice(details[18:24])  # Gang Markings, Patrol Posts, Lookouts, etc.
    elif roll == 5:
        return random.choice(details[24:30])  # Stray Animals, Landscaping, Muck, Mire, etc.
    else:
        return random.choice(details[30:])  # Ancient Ruin, Leering Gargoyles, etc.
