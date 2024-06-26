import random

def roll_names():
    demon_names = [
        "Korvaeth", "Sevraxis", "Argaz", "Zalvroxos", "Kethtera", "Arkeveron", "Ixis", "Kyronax", "Voldranai", "Esketra", "Ardranax", "Kylastra", "Oryxus", "Ahazu", "Tyraxis", "Azarax", "Vaskari"
    ]
    
    return random.choice(demon_names)

def roll_features():
    demon_features = [
        "Black shark eyes", "Scales (onyx, iridescent, crystalline, metallic, etc.)", "Razor-sharp claws", "Bony protrusions", "Multiple eyes", "Lashing tail", "Leathery wings", "Spines", "Dripping ichor", "Glowing eyes or markings", "Hair or fur (drifting as if underwater, burning with a cool fire, etc.)", "Feathers", "Multiple arms", "Tentacles", "Hard shell, metallic plates", "Lights dim or flare", "Plants wither or grow wildly", "Mechanisms grind to a halt", "Liquid freezes, boils, turns to blood or ashes"
    ]
    
    return random.choice(demon_features)

import random

def roll_aspects():
    aspects = [
        "Humanoid with Bestial or Elemental Features", "Animal", 
        "Monstrous", "Amorphous"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 3:
        return aspects[0]  # Humanoid with Bestial or Elemental Features
    elif roll == 4:
        return aspects[1]  # Animal
    elif roll == 5:
        return aspects[2]  # Monstrous
    else:
        return aspects[3]  # Amorphous

def roll_affinities():
    affinities = [
        "Sea, Water", "Darkness", "Earth, Metal", 
        "Fire, Smoke", "Sky, Stars", "Storm, Wind"
    ]
    
    return random.choice(affinities)

def roll_desires():
    desired = [
        "Mayhem", "Murder", "Justice", "Corruption", "Power", "Control", "Knowledge", "Pleasure", "Suffering", "War", "Revenge", "Chaos", "Freedom", "Savagery", "Manipulation", "Deception", "Fear", "Achievement"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(desired[:6])  # Mayhem, Murder, Justice, Corruption, Power, Control
    elif roll <= 4:
        return random.choice(desired[6:12])  # Knowledge, Pleasure, Suffering, War, Revenge, Chaos
    else:
        return random.choice(desired[12:])  # Freedom, Savagery, Manipulation, Deception, Fear, Achievement

def roll_forgotten_gods():
    forgotten_gods = [
        "The One Within Many", "The Silver Fire", "The Rapturous Chord", "The Fallen Star", "The Lord of the Depths", "The Silent Song", "The Lady of Thorns", "Our Blood Spilled in Glory", "The Ram", "The Empty Vessel", "The Closed Eye", "The Hand of Sorrow", "That Which Hungers", "The Thousand Faces", "The Web of Pain", "The Pillars of Night", "The Burned King", "The Father of the Abyss", "The Forsaken Legion", "The Unbroken Sun", "The Revelation", "The Radiant Word", "The Shrouded Queen", "The Reconciler", "The Cloud of Woe", "The Broken Circle", "The Conqueror", "She Who Slays in Darkness", "The Dream Beyond Death", "The Blood Dimmed Tide", "The Guardian of the Gates", "The Maw of the Void", "The Keeper of the Flame", "The Throne of Judgment", "The Lost Crown", "The Golden Stag"
    ]
    
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return forgotten_gods[roll - 11]

def roll_cult_practices():
    cult_practices = [
        "Sacrifice: Fed to specially consecrated beasts / Savaged (eaten?) by frenzied cult mob.", "Sacrifice: Pitted against an anointed champion in death arena.", "Sacrifice: Ritually bled upon the sacred altar.", "Sacrifice: Progressively overdosed with mind-expanding drugs.", "Sacrifice: Ritually killed and claimed as anointed spirit-champion.", "Sacrifice: Slain by arcane means (electrocuted, spirit shattered, death-cursed).", "Congregation: An orgy of pleasure (sex, food, dance, music) and/or pain.", "Congregation: Sacred hymns or prayers for days without ceasing.", "Congregation: Occupying a sacred nexus point during an astrological confluence.", "Congregation: A pilgrimage to a sacred place or being in the deathlands / at sea.", "Congregation: A group vision / dream-quest via essences, drugs, or meditation.", "Congregation: A reenactment / dumb-show of a sacred event.", "Acquisition: A collection of eyes / hearts / blood from mystics or demons.", "Acquisition: The shards of a shattered sacred object (jewel, sword, skull, stone).", "Acquisition: The original holy writings of the prophet / master / saint.", "Acquisition: The severed body parts (heads, hands, tongues) of heretics or apostates.", "Acquisition: Properties aligned with sacred geometry or attuned by mystical events.", "Acquisition: The ghosts of prophets / mystics / founders / enemies of the order.", "Destruction: Ritual burning of sacred objects (rune-papers, effigies, flesh, hair).", "Destruction: Ritual eradication of a spirit or demon.", "Destruction: The breaking of the seals that keep the god from this world.", "Destruction: Shattering of ritual objects / altars / temples sacred to an enemy order.", "Destruction: Eradication of weapons / objects / sites / rituals that can harm the god.", "Destruction: Eradication of social / legal / cultural elements that threaten the order.", "Consecration: Purification by bathing in sacred fluid (blood, wine, milk, oil, etc.).", "Consecration: Purification of the gates that give passage to the god into this world.", "Consecration: Baptism / blessing of an acolyte or object by immersion in spirit well.", "Consecration: Purify / bless cult followers with tattoos / scarification / mutilation.", "Consecration: Creation of blessed idols / artwork / ritual spaces / artifacts.", "Consecration: Wards / runes / spirits bound to shun enemies of the order.", "Desecration: Debasement or defilement of one sworn to an enemy order.", "Desecration: Corruption of place / object / ritual / tradition to appropriate its power.", "Desecration: Defilement of place / object / ritual to humiliate another order.", "Desecration: Manipulation of authorities / institutions to appropriate their power.", "Desecration: Corruption of acolytes to prepare them for transformation.", "Desecration: Mindless, pointless chaos; sewing the seeds of anarchy."
    ]
    
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return cult_practices[roll - 11]

