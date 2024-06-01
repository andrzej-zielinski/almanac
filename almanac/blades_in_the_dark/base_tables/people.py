import random

def roll_heritage():
    """
    Remember, each Tycherosi has a demonic trait: cat’s eyes, claws, feathers instead of hair, etc.
    """
    primary_roll = random.randint(1, 6)
    if primary_roll <= 3:
        return "Akorosi"
    else:
        foreigner_roll = random.randint(1, 6)
        if foreigner_roll <= 2:
            return "Skovlander"
        elif foreigner_roll == 3:
            return "Iruvian"
        elif foreigner_roll == 4:
            return "Dagger Islander"
        elif foreigner_roll == 5:
            return "Severosi"
        else:
            return "Tycherosi (each Tycherosi has a demonic trait: cat’s eyes, claws, feathers instead of hair, etc.)"


def roll_style():
    styles = [
        "Tricorn Hat", "Long Coat", "Hood & Veil", "Short Cloak", "Knit Cap", "Slim Jacket", "Hooded Coat", "Tall Boots", "Work Boots", "Mask & Robes", "Suit & Vest", "Collared Shirt", "Suspenders", "Rough Tunic", "Skirt & Blouse", "Wide Belt", "Fitted Dress", "Heavy Cloak", "Thick Greatcoat", "Soft Boots", "Loose Silks", "Sharp Trousers", "Waxed Coat", "Long Scarf", "Leathers", "Eelskin Bodysuit", "Hide & Furs", "Uniform", "Tatters", "Fitted Leggings", "Apron", "Heavy Gloves", "Face Mask", "Tool Belt", "Crutches", "Cane", "Wheelchair"
    ]
    
    return random.choice(styles)


def roll_looks_gender():
    """
    LOOKS
    1/2: man
    3/4: woman
    5: ambiguous, concealed
    """
    roll = random.randint(1, 5)
    if roll <= 2:
        return "man"
    elif roll <= 4:
        return "woman"
    else:
        return "ambiguous, concealed"

import random

def roll_looks_impression():
    looks = [
        ["Large", "Lovely", "Weathered", "Chiseled", "Handsome", "Athletic"], ["Slim", "Dark", "Fair", "Stout", "Delicate", "Scarred"], ["Bony", "Worn", "Rough", "Plump", "Wiry", "Striking"], ["Short", "Tall", "Sexy", "Wild", "Elegant", "Stooped"], ["Cute", "Plain", "Old", "Young", "Stylish", "Strange"], ["Disfigured, Maimed", "Glasses, Monocle", "Prosthetic, Crippled", "Long Hair, Beard, Wig", "Shorn, Bald", "Tattooed"]
    ]
    
    roll = random.randint(1, 6)
    return random.choice(looks[roll - 1])


import random

def roll_goals():
    goals = [
        "Wealth", "Power", "Authority", "Prestige, Fame", "Control", "Knowledge", "Pleasure", "Revenge", "Freedom", "Achievement", "Happiness", "Infamy, Fear", "Respect", "Love", "Change", "Chaos, Destruction", "Justice", "Cooperation"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(goals[:6])  # Wealth, Power, Authority, Prestige, Fame, Control, Knowledge
    elif roll <= 4:
        return random.choice(goals[6:12])  # Pleasure, Revenge, Freedom, Achievement, Happiness, Infamy, Fear
    else:
        return random.choice(goals[12:])  # Respect, Love, Change, Chaos, Destruction, Justice, Cooperation

def roll_preferred_methods():
    methods = [
        "Violence", "Threats", "Negotiation", "Study", "Manipulation", "Strategy", "Theft", "Arcane", "Commerce", "Hard Work", "Law, Politics", "Sabotage", "Subterfuge", "Alchemy", "Blackmail", "Teamwork", "Espionage", "Chaos"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(methods[:6])  # Violence, Threats, Negotiation, Study, Manipulation, Strategy
    elif roll <= 4:
        return random.choice(methods[6:12])  # Theft, Arcane, Commerce, Hard Work, Law, Politics, Sabotage
    else:
        return random.choice(methods[12:])  # Subterfuge, Alchemy, Blackmail, Teamwork, Espionage, Chaos

def roll_profession_common():
    professions = [
        "Baker", "Barber", "Blacksmith", "Brewer", "Butcher", "Carpenter", "Cartwright", "Chandler", "Clerk", "Cobbler", "Cooper", "Cultivator", "Driver", "Dyer", "Embroiderer", "Fishmonger", "Gondolier", "Guard", "Leatherworker", "Mason", "Merchant", "Roofer", "Ropemaker", "Rug Maker", "Servant", "Shipwright", "Criminal", "Tailor", "Tanner", "Tinkerer", "Vendor", "Weaver", "Woodworker", "Goat Herd", "Messenger", "Sailor"
    ]
    
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(professions[:6])  # Baker, Barber, Blacksmith, Brewer, Butcher, Carpenter
    elif roll == 2:
        return random.choice(professions[6:12])  # Cartwright, Chandler, Clerk, Cobbler, Cooper, Cultivator
    elif roll == 3:
        return random.choice(professions[12:18])  # Driver, Dyer, Embroiderer, Fishmonger, Gondolier, Guard
    elif roll == 4:
        return random.choice(professions[18:24])  # Leatherworker, Mason, Merchant, Roofer, Ropemaker, Rug Maker
    elif roll == 5:
        return random.choice(professions[24:30])  # Servant, Shipwright, Criminal, Tailor, Tanner, Tinkerer
    else:
        return random.choice(professions[30:])  # Vendor, Weaver, Woodworker, Goat Herd, Messenger, Sailor

def roll_profession_rare():
    professions = [
        "Advocate", "Architect", "Artist", "Author", "Bailiff", "Apiarist", "Banker", "Bounty Hunter", "Clockmaker", "Courtesan", "Furrier", "Glass Blower", "Diplomat", "Jailer", "Jeweler", "Leech", "Locksmith", "Magistrate", "Musician", "Physicker", "Plumber", "Printer", "Scholar", "Scribe", "Sparkwright", "Tax Collector", "Treasurer", "Whisper", "Composer", "Steward", "Captain", "Spirit Warden", "Journalist", "Explorer", "Rail Jack", "Soldier"
    ]
    
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(professions[:6])  # Advocate, Architect, Artist, Author, Bailiff, Apiarist
    elif roll == 2:
        return random.choice(professions[6:12])  # Banker, Bounty Hunter, Clockmaker, Courtesan, Furrier, Glass Blower
    elif roll == 3:
        return random.choice(professions[12:18])  # Diplomat, Jailer, Jeweler, Leech, Locksmith, Magistrate
    elif roll == 4:
        return random.choice(professions[18:24])  # Musician, Physicker, Plumber, Printer, Scholar, Scribe
    elif roll == 5:
        return random.choice(professions[24:30])  # Sparkwright, Tax Collector, Treasurer, Whisper, Composer, Steward
    else:
        return random.choice(professions[30:])  # Captain, Spirit Warden, Journalist, Explorer, Rail Jack, Soldier


def roll_names():
    names = [
        "Adric", "Aldo", "Amosen", "Andrel", "Arden", "Arlyn", "Arquo", "Arvus", "Ashlyn", "Branon", "Brace", "Brance", "Brena", "Bricks", "Candra", "Carissa", "Carro", "Casslyn", "Cavelle", "Clave", "Corille", "Cross", "Crowl", "Cyrene", "Daphnia", "Drav", "Edlun", "Emeline", "Grine", "Helles", "Hix", "Holtz", "Kamelin", "Kelyr", "Kobb", "Kristov", "Laudius", "Lauria", "Lenia", "Lizete", "Lorette", "Lucella", "Lynthia", "Mara", "Milos", "Morlan", "Myre", "Narcus", "Naria", "Noggs", "Odrienne", "Orlan", "Phin", "Polonia", "Quess", "Remira", "Ring", "Roethe", "Sesereth", "Sethla", "Skannon", "Stavrul", "Stev", "Syra", "Talitha", "Tesslyn", "Thena", "Timoth", "Tocker", "Una", "Vaurin", "Veleris", "Veretta", "Vestine", "Vey", "Volette", "Vond", "Weaver", "Wester", "Zamira"
    ]
    
    return random.choice(names)


def roll_family_names():
    family_names = [
        "Ankhayat", "Arran", "Athanoch", "Basran", "Boden", "Booker", "Bowman", "Breakiron", "Brogan", "Clelland", "Clermont", "Coleburn", "Comber", "Daava", "Dalmore", "Danfield", "Dunvil", "Farros", "Grine", "Haig", "Helker", "Helles", "Hellyers", "Jayan", "Jeduin", "Kardera", "Karstas", "Keel", "Kessarin", "Kinclaith", "Lomond", "Maroden", "Michter", "Morriston", "Penderyn", "Prichard", "Rowan", "Sevoy", "Skelkallan", "Skora", "Slane", "Strangford", "Strathmill", "Templeton", "Tyrconnell", "Vale", "Walund", "Welker"
    ]
    
    return random.choice(family_names)

def roll_aliases():
    aliases = [
        "Bell", "Birch", "Bricks", "Bug", "Chime", "Coil", "Cricket", "Cross", "Crow", "Echo", "Flint", "Frog", "Frost", "Grip", "Gunner", "Hammer", "Hook", "Junker", "Mist", "Moon", "Nail", "Needle", "Ogre", "Pool", "Ring", "Ruby", "Silver", "Skinner", "Song", "Spur", "Tackle", "Thistle", "Thorn", "Tick-Tock", "Twelves", "Vixen", "Whip", "Wicker"
    ]
    
    return random.choice(aliases)

import random

def roll_traits():
    traits = {
        11: "Charming", 12: "Cold", 13: "Cavalier", 14: "Brash", 15: "Suspicious", 16: "Obsessive", 21: "Shrewd", 22: "Quiet", 23: "Moody", 24: "Fierce", 25: "Careless", 26: "Secretive", 31: "Ruthless", 32: "Calculating", 33: "Defiant", 34: "Gracious", 35: "Insightful", 36: "Dishonest", 41: "Patient", 42: "Vicious", 43: "Sophisticated", 44: "Paranoid", 45: "Enthusiastic", 46: "Elitist", 51: "Savage", 52: "Cooperative", 53: "Arrogant", 54: "Confident", 55: "Vain", 56: "Daring", 61: "Volatile", 62: "Candid", 63: "Subtle", 64: "Melancholy", 65: "Enigmatic", 66: "Calm"
    }
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return traits[roll]

def roll_interests():
    interests = {
        11: "Fine whiskey, wine, beer", 12: "Fine food, restaurants", 13: "Fine clothes, jewelry, furs", 14: "Fine arts, opera, theater", 15: "Painting, drawing, sculpture", 16: "History, legends", 21: "Architecture, furnishings", 22: "Poetry, novels, writing", 23: "Pit-fighting, duels", 24: "Forgotten gods", 25: "Church of Ecstasy", 26: "Path of Echoes", 31: "Weeping Lady, charity", 32: "Antiques, artifacts, curios", 33: "Horses, riding", 34: "Gadgets, new technology", 35: "Weapons collector", 36: "Music, instruments, dance", 41: "Hunting, shooting", 42: "Cooking, gardening", 43: "Gambling, cards, dice", 44: "Natural philosophy", 45: "Drugs, essences, tobacco", 46: "Lovers, romance, trysts", 51: "Parties, social events", 52: "Exploration, adventure", 53: "Pets (birds, dogs, cats)", 54: "Craft (leatherwork, etc.)", 55: "Ships, boating", 56: "Politics, journalism", 61: "Arcane books, rituals", 62: "Spectrology, electroplasm", 63: "Alchemy, medicine", 64: "Essences, alchemy", 65: "Demon lore, legends", 66: "Pre-cataclysm legends"
    }
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return interests[roll]

def roll_quirks():
    quirks = {
        11: "Superstitious. Believes in signs, magic numbers.", 12: "Devoted to their family.", 
        13: "Married into important / powerful family.", 14: "Holds their position to spy for another faction.", 15: "Reclusive. Prefers to interact via messengers.", 16: "Massive debts (to banks / criminals / family)", 21: "Blind to flaws in friends, allies, family, etc.", 22: "Once hollowed, then restored. Immune to spirits.", 23: "Has chronic illness that requires frequent care.", 24: "Secretly (openly?) controlled by possessing spirit.", 25: "Serves a demon’s agenda (knowingly or not).", 26: "Proud of heritage, traditions, native language.", 31: "Concerned with appearances, gossip, peers.", 32: "Drug / alcohol abuser. Often impaired by their vice.", 33: "Holds their position due to blackmail.", 34: "Relies on council to make decisions.", 35: "Involved with war crimes from the Unity War.", 36: "Leads a double life using cover identity.", 41: "Black sheep / outcast from family or organization.", 42: "In prison or under noble’s house arrest.", 43: "Well-traveled. Connections outside Doskvol.", 44: "Revolutionary. Plots against the Imperium.", 45: "Inherited their position. May not deserve / want it.", 46: "Celebrity. Popularized in print / song / theater.", 51: "Scandalous reputation (deserved or not).", 52: "Surrounded by sycophants, supplicants, toadies.", 53: "Spotless reputation. Highly regarded.", 54: "Bigoted against culture / belief / social class.", 55: "Visionary. Holds radical views for future.", 56: "Cursed, haunted, harassed by spirits or demon.", 61: "Intense, unreasonable phobia or loathing.", 62: "Extensive education on every scholarly subject.", 63: "Keeps detailed journals, notes, records, ledgers.", 64: "Is blindly faithful to an ideal, group, or tradition.", 65: "Deeply traditional. Opposed to new ideas.", 66: "A fraud. Some important aspect is fabricated."
    }
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return quirks[roll]
