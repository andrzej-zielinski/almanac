import random

def roll_exterior_material():
    materials = [
        "Gray Brick", "Stone & Timbers", "Cut Stone Blocks", "Wooden Boards", "Plaster Board & Timbers", "Metal Sheeting"
    ]
    roll = random.randint(1, 6)
    return materials[roll - 1]

def roll_exterior_details():
    details = [
        "Tile Work", "Iron Work", "Glass Work", "Stone Work", "Wood Work", "Landscaping"
    ]
    roll = random.randint(1, 6)
    return details[roll - 1]


def roll_use_common():
    common_uses = [
        "Bunk House", "Inn", "Tavern", "Gambling Hall", "Drug Den", "Brothel", "Market", "Workshop", "Bakery", "Butchery", "Forge", "Tailory", "Work House", "Goat Stables", "Brewery", "Watch Post", "Court, Jail", "Dock", "Ruin", "Row Houses", "Tenements", "Apartment Building", "Small House", "Bath House", "Shrine", "Tattooist", "Physicker", "Fighting Pits", "Square, Fountain", "Grotto", "Warehouse", "Stockyard", "Factory", "Refinery", "Eelery", "Mushroom Garden"
    ]
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(common_uses[:6])  # Bunk House, Inn, Tavern, Gambling Hall, Drug Den, Brothel
    elif roll == 2:
        return random.choice(common_uses[6:12])  # Market, Workshop, Bakery, Butchery, Forge, Tailory
    elif roll == 3:
        return random.choice(common_uses[12:18])  # Work House, Goat Stables, Brewery, Watch Post, Court, Jail, Dock
    elif roll == 4:
        return random.choice(common_uses[18:24])  # Ruin, Row Houses, Tenements, Apartment Building, Small House, Bath House
    elif roll == 5:
        return random.choice(common_uses[24:30])  # Shrine, Tattooist, Physicker, Fighting Pits, Square, Fountain, Grotto
    else:
        return random.choice(common_uses[30:])  # Warehouse, Stockyard, Factory, Refinery, Eelery, Mushroom Garden


def roll_use_rare():
    rare_uses = [
        "Market House", "Restaurant", "Bar, Lounge", "Academy", "Salon", "Cafe", "Floristry", "Tobacconist", "Book Shop", "Jeweler", "Clothier", "Gallery", "Apothecary", "Horse Stables", "Distillery", "Vintner", "Master Artisan", "Boat House", "Theater", "Opera House", "Apartment Building", "Townhouse", "Manor House", "Villa", "Clinic", "Temple", "Cistern", "Watch Post", "Park", "Monument", "Archive", "Spiritualist", "Bank", "Alchemist", "Power Plant", "Radiant Energy Garden"
    ]
    roll = random.randint(1, 6)
    if roll == 1:
        return random.choice(rare_uses[:6])  # Market House, Restaurant, Bar, Lounge, Academy, Salon, Cafe
    elif roll == 2:
        return random.choice(rare_uses[6:12])  # Floristry, Tobacconist, Book Shop, Jeweler, Clothier, Gallery
    elif roll == 3:
        return random.choice(rare_uses[12:18])  # Apothecary, Horse Stables, Distillery, Vintner, Master Artisan, Boat House
    elif roll == 4:
        return random.choice(rare_uses[18:24])  # Theater, Opera House, Apartment Building, Townhouse, Manor House, Villa
    elif roll == 5:
        return random.choice(rare_uses[24:30])  # Clinic, Temple, Cistern, Watch Post, Park, Monument
    else:
        return random.choice(rare_uses[30:])  # Archive, Spiritualist, Bank, Alchemist, Power Plant, Radiant Energy Garden


def roll_details():
    details = [
        ["Dripping Water", "Creaking Floorboards", "Roaring Fires", "Smoky Lamps", "Buzzing Electric Lights", "Ticking Clockworks"], ["Plants, Flowers", "Wall Hangings, Artwork", "Shuttered Windows", "Heavy Curtains, Thick Carpet", "Dust, Detritus", "Wear, Damage"], ["Threadbare, Tattered", "Utilitarian Furnishings", "Elegant Finery", "Lush, Comfortable", "Rough-Spun Simplicity", "Spartan Austerity"], ["Circular Stairs, Ladders", "Secret Doors", "Catwalks", "Skylights", "Balcony", "Cellar"], ["Drafty, Cold", "Stout, Quiet", "Cozy, Warm", "Vaulted, Spacious", "Low, Cramped", "Rickety, Ramshackle"], ["Strange Devices", "Weird Artifacts", "Spirit Wards, Old Runes", "Piled Jumble of Curios", "Antique Appointments", "Shrine, Altar"]
    ]
    
    roll = random.randint(1, 6)
    return random.choice(details[roll - 1])


def roll_items():
    items = [
        "Chalkboard, Desks, Papers", "Maps, Charts, Diagrams", "Books, Scrolls, Bookcases", "Lamp, Inkwell, Writing Desk", "Clock, Cabinet, Shelves", "Table, Chairs, Notebooks", "Bed, Bureau, Vanity", "Bunks, Stools, Trunks", "Basin, Pitcher, Mirror", "Sofa, Divan, Music Box", "Couches, Table, Lamps", "Drapery, Pillows, Cushions", "Counter, Sink, Cabinets", "Cookfire, Pots, Pans, Utensils", "Dining Table, Chairs, Cutlery", "Game Board, Cards, Dice", "Larder, Spices, Meat Hooks", "Wine, Beer, Whiskey", "Pedestal, Statue, Paintings", "Bird Cage, Quill, Diary", "Bell, Book, Candle", "Fireplace, Rug, Armchair", "Curtains, Vases, Flowers", "Instruments, Music Sheets", "Exam Chair, Medical Tools", "Burner, Vials, Beakers", "Workbench, Tools, Rags", "Weapons, Ammunition"
    ]
    
    return random.choice(items)


