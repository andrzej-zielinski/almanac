import random

def roll_forename_male():
    forenames_male = [
        "Augost", "Benedict", "Brin", "Chuman", "Calhed", "Dorren", "Emmett", "Felix", "Fred", 
        "Grobin", "Gizard", "Herion", "Istan", "Ilmer", "Junas", "Katsun", "Lurpat", "Litton", 
        "Munfud", "Narmun", "Orren", "Podder", "Peta", "Picklow", "Pipp", "Quinn", "Rashin", 
        "Stellan", "Samford", "Tucker", "Teevan", "Untin", "Varran", "Vanis", "Volta", "Webster", 
        "Yunak", "Zam"
    ]
    return random.choice(forenames_male)

def roll_forename_female():
    forenames_female = [
        "Augosta", "Benedicta", "Breen", "Chuwel", "Calit", "Dorret", "Emma", "Felora", "Freda", 
        "Gill", "Giza", "Heriael", "Isti", "Ilda", "Julia", "Katsin", "Lunda", "Litta", 
        "Muni", "Nadya", "Orra", "Poddin", "Ooze", "Pickelle", "Pippita", "Quigley", "Rashel", 
        "Stella", "Samay", "Tuckis", "Teva", "Una", "Varin", "Vanissa", "Voltel", "Webin", 
        "Yuna", "Zarrack"
    ]
    return random.choice(forenames_female)

def roll_surname():
    surnames = [
        "Allane", "Bargroll", "Brunfield", "Chop", "Creed", "Dunbell", "Eggler", "Fox", "Farsee", 
        "Gill", "Gullwin", "Huckle", "Horrican", "Ingle", "Jongler", "Kross", "Lix", "Lowbile", 
        "Montane", "Nutbush", "Olifant", "Offenpot", "Ooze", "Phile", "Parfait", "Quigley", 
        "Regal", "Stagger", "Shark", "Tumble", "Terrine", "Underhog", "Upperill", "Volfhole", 
        "Vinifera", "Wickerspin", "Yarn", "Zarrack"
    ]   
    return random.choice(surnames)

def roll_occupation():
    occupations = [
        "Actor", "Barge Pilot", "Butler", "Coffee House Host", "Coal Miner", "Dog Breeder", 
        "Escort", "Fist Fighter", "Fishmonger", "Gull-Catcher", "Glue Maker", "Gunsmith", 
        "Gin-Maker", "Hog Slaughterer", "Ivory Worker", "Jeweler", "Lower Politician", 
        "Life Servant", "Lamp Lighter", "Lesser Noble", "Mercenary", "Newspaper Vendor", 
        "Octopus Catcher", "Oyster Seller", "Perfumer", "Professor", "Prison Guard", 
        "Pie-Smith", "Road Sweeper", "Salt Farmer", "Sweet-Maker", "Trinket Merchant", 
        "Tax Collector", "Tunnel Digger", "Whaler", "Watchmaker", "Watchman", "Writer", 
        "Wigmaker"
    ]
    return random.choice(occupations)

def roll_capability():
    capabilities = [
        "Anal-Retentive", "Boringly Dependable", "Best in the City", "Cheap and Dirty", 
        "Charming and Oily", "Dabbler", "Expensive and Flashy", "Fair and Down to Earth", 
        "Filthy but Very Cheap", "Great, but Hated for It", "Good but Annoying", 
        "Highly Artistic", "Hardly Trained", "Inherited Family Trade", "Interested in New Career", 
        "Imposter", "Jealous of Better Rival", "Learning, Still", "Loves the Job", 
        "Lazy and Greedy", "Money-Grabbing", "Moral, but Not That Good", "Only Serves Friends", 
        "Old-Master Trained", "Perfectionist", "Paragon of the Job", "Poor from Bad Business", 
        "Retired from Injury", "Ruthless", "Sworn into Profession", "Silently Dutiful", 
        "Trained from Birth", "Trapped in Job", "Uncaring", "Unreliable Genius", 
        "Wedded into Career", "Wasted Talent", "Warm and Friendly", "Wealthy with Success"
    ]
    return random.choice(capabilities)

def roll_manner():
    manners = [
        "Attractive", "Big Fat Glutton", "Beaky Bore", "Creaky Elder", "Childlike", "Dashing Young Gun", 
        "Ethereal Beauty", "Fails at Flirtatious", "Flamboyant Charmer", "Great Speaker", "Greasy Toad", 
        "Gentle Giant", "Hulking Brute", "Hunchback", "Harmless Dope", "Intensely Creepy", 
        "Ill-Coloured and Thin", "Jolly Fatty", "Loads of Jewellery", "Lots of Scars", "No Nose", 
        "Nice but Dim", "Naive Teenager", "Old Sleaze", "Pig-Faced", "Plucky Little Thing", 
        "Powdered Wig", "Quite Ugly", "Rough as a Dog", "Stocky Grunter", "Stunted Growth", 
        "Straight-Laced", "Towering Clutz", "Unwashed Hippy", "Vapid Fashionista", "Very Long Hair", 
        "Well-Bred Snob", "Waif", "Weird Head"
    ]
    return random.choice(manners)

def roll_connection():
    connections = [
        "Dullard Aunt/Uncle", "Sibling", "Best Friend", "Owes Money", "Old Friend", "Common Ancestry", 
        "Platonic Love", "Flirtatious Admiration", "Parent", "Owed Money", "Acquaintance", 
        "Common Benefactor", "Hatred", "Irritation", "Twin", "Spouse", "Guardian", "Lover", "Mentor", 
        "Abuser", "Lust", "Distaste", "House-Share", "Former Colleagues", "School Friends", 
        "Adopted Parent", "Unrequited Love", "Planning Murder", "Knows Secret", "One Night Stand", 
        "Rivals", "Backhand Deal", "Criminal Enterprise", "Shared Trauma", "Jealousy", "Violent Hate", 
        "Engaged", "Protector", "Playful Rivalry"
    ]
    return random.choice(connections)

def roll_event():
    events = [
        "Arrested Wrongfully for Minor Crime", "Arrested Rightfully for Major Crime", 
        "Arrested Rightfully for Major Crime", "Arrested Rightfully for Major Crime", 
        "Arrested Rightfully for Major Crime", "Became Addicted to an Exotic Drug", 
        "Became Addicted to an Exotic Drug", "Contracted a Terrible Disease", 
        "Contracted a Terrible Disease", "Debt Collectors are Applying Pressure", 
        "Debt Collectors are Applying Pressure", "Died in an Uprising", "Died in an Uprising", 
        "Died in Industrial Accident", "Died in Industrial Accident", "Found Long-Lost Relative", 
        "Found Long-Lost Relative", "Found (New) Love", "Found (New) Love", 
        "Found a Major Arcanum", "Found a Major Arcanum", "Found a Major Arcanum", 
        "Found a Lesser Arcanum", "Found a Lesser Arcanum", "Getting (Re)Married", 
        "Getting (Re)Married", "Getting (Re)Married", "Joined a Star Cult", "Joined a Star Cult", 
        "Joined a Star Cult", "Joined a (New) Revolutionary Group", "Joined a (New) Revolutionary Group", 
        "Joined a (New) Revolutionary Group", "Joined a (New) Revolutionary Group", 
        "House Collapsed", "House Collapsed", "House Collapsed", "House Collapsed", "Lost at Sea", 
        "Lost at Sea", "Lost Everything", "Lost Everything", "Lamp-Lighter Burnt Down House", 
        "Lamp-Lighter Burnt Down House", "Lamp-Lighter Burnt Down House", 
        "Left Bastion for the Deep Country", "Left Bastion for the Deep Country", 
        "Left Bastion for the Deep Country", "Left Bastion for a Lesser City", 
        "Left Bastion for a Lesser City", "Left Bastion for a Lesser City", "Murdered in the Street", 
        "Murdered in the Street", "Murdered in the Street", "Murdered in Their Bed", 
        "Murdered in Their Bed", "Murdered in Their Bed", "Nice Person Has Given Them Some Juicy Work", 
        "Nice Person Has Given Them Some Juicy Work", "Nice Person Has Given Them Some Juicy Work", 
        "Press-Ganged into Military", "Press-Ganged into Military", "Press-Ganged into Military", 
        "Rumours of Criminal Activity", "Rumours of Criminal Activity", "Rumours of Criminal Activity", 
        "Rumours of Sexual Depravity", "Rumours of Sexual Depravity", "Rumours of Sexual Depravity", 
        "Saw Weird Things in the Sky", "Saw Weird Things in the Sky", "Saw Weird Things in the Sky", 
        "Saw Weird Things in the Sky", "Saw Horrible Beasts in the Street", "Saw Horrible Beasts in the Street", 
        "Saw Horrible Beasts in the Street", "Saw Horrible Beasts in the Street", "Saw a Murder Nearby", 
        "Saw a Murder Nearby", "Taken up Military Service", "Taken up Military Service", "Taken up Military Service", 
        "Taken in an Orphan", "Taken in an Orphan", "The Watch are Harassing Them", 
        "The Watch are Harassing Them", "The Watch are Harassing Them", "Underground Weirdos Abducted Them", 
        "Underground Weirdos Abducted Them", "Underground Weirdos Abducted Them", "Vanished in a Burst of Light", 
        "Wandered into Underground, Now Missing", "Wandered into Underground, Now Missing", 
        "Wandered into Underground, Now Missing", "Won a Fortune by Gambling", "Won a Fortune by Gambling", 
        "Witnessed an Abduction into the Night Sky", "Witnessed an Abduction into the Night Sky", 
        "Went on a Drinking Binge", "Went on a Drinking Binge", "Recklessly Leapt into a Doomed Romance"
    ]
    return random.choice(events)
