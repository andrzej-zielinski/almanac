import random 

def roll_score_person():
    categories = ["civilian", "criminal", "political", "strange"]
    return random.choice(categories)

# Example usage:
print(roll_score_person())



def roll_score_person_civilian():
    civilians = [
        "Academic or Scholar", "Laborer or Tradesman", "Courier or Sailor", "Merchant or Shopkeeper", "Artist or Writer", "Doctor or Alchemist"
    ]
    roll = random.randint(1, 6)
    return civilians[roll - 1]

def roll_score_person_criminal():
    criminals = [
        "Drug Dealer or Supplier", "Mercenary or Thug", "Fence or Gambler", "Spy or Informant", "Smuggler or Thief", "Crime Boss"
    ]
    roll = random.randint(1, 6)
    return criminals[roll - 1]

def roll_score_person_political():
    politicals = [
        "Noble or Official", "Banker or Captain", "Revolutionary or Refugee", "Clergy or Cultist", "Constable or Inspector", "Magistrate or Ward Boss"
    ]
    roll = random.randint(1, 6)
    return politicals[roll - 1]

def roll_score_person_strange():
    strange = [
        "Ghost of (roll again)", "Occult Collector", "Vampire or Other Undead", "Demon (disguised)", "Possessed or Hollow", "Whisper or Cultist"
    ]
    roll = random.randint(1, 6)
    return strange[roll - 1]

def roll_score_client():
    person_type = roll_score_person()
    if person_type == "civilian":
        return roll_score_person_civilian()
    elif person_type == "criminal":
        return roll_score_person_criminal()
    elif person_type == "political":
        return roll_score_person_political()
    else:  # "strange"
        return roll_score_person_strange()
    
def roll_score_work_type():
    work_types = ["skullduggery", "violence", "underworld", "unnatural"]
    return random.choice(work_types)

def roll_score_work_skullduggery():
    skullduggery = [
        "Stalking or Surveillance", "Sabotage or Arson", "Lift or Plant", "Poison or Arrange Accident", "Burglary or Heist", "Impersonate or Misdirect"
    ]
    roll = random.randint(1, 6)
    return skullduggery[roll - 1]

def roll_score_work_violence():
    violence = [
        "Assassinate", "Disappear or Ransom", "Terrorize or Extort", "Destroy or Deface", "Raid or Defend", "Rob or Strong-arm"
    ]
    roll = random.randint(1, 6)
    return violence[roll - 1]

def roll_score_work_underworld():
    underworld = [
        "Escort or Security", "Smuggle or Courier", "Blackmail or Discredit", "Con or Espionage", "Locate or Hide", "Negotiate or Threaten"
    ]
    roll = random.randint(1, 6)
    return underworld[roll - 1]

def roll_score_work_unnatural():
    unnatural = [
        "Curse or Sanctify", "Banish or Summon", "Extract Essence", "Place or Remove Runes", "Perform / Stop Ritual", "Hollow or Revivify"
    ]
    roll = random.randint(1, 6)
    return unnatural[roll - 1]

def roll_score_work():
    work_type = roll_score_work_type()
    if work_type == "skullduggery":
        return roll_score_work_skullduggery()
    elif work_type == "violence":
        return roll_score_work_violence()
    elif work_type == "underworld":
        return roll_score_work_underworld()
    else:  # "unnatural"
        return roll_score_work_unnatural()


import random

def roll_twist_or_complication():
    twists_and_complications = [
        "An element is a cover for heretic spirit cult practices", "An occultist has foreseen this job and warned the parties involved", "Rogue spirits possess some/most/all of the people involved", "Rogue spirits haunt the location", "The job furthers a demon’s secret agenda", "The job furthers a vampire’s secret agenda", "An element is a front for a criminal enterprise", "A dangerous gang uses the location", "The job is a trap laid by your enemies", "The job is a test for another job", "The job furthers a merchant lord’s secret agenda", "The job furthers a crime boss’s secret agenda", "The job requires travel by electrorail", "Must visit the deathlands to do the job", "The job requires sea travel", "The location moves around (site changes, it’s on a vehicle, etc.)", "The job furthers a revolutionary’s secret agenda", "The job furthers a city official’s secret agenda"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(twists_and_complications[:6])  # Spiritual or heretic elements
    elif roll <= 4:
        return random.choice(twists_and_complications[6:12])  # Criminal elements
    else:
        return random.choice(twists_and_complications[12:])  # Travel or other elements

# Example usage:
print(roll_twist_or_complication())


import random

def roll_connections_person():
    connections = [
        "PC Friend", "PC Rival", "PC Vice purveyor", "Crew Contact", "City Doskvol notable", "Weird Ghost, Demon, God"
    ]
    
    roll = random.randint(1, 6)
    return connections[roll - 1]


import random

def roll_connections_faction():
    factions = [
        "The Unseen", "Lord Scurlock", "The Circle of Flame", "The Lampblacks", "The Dimmer Sisters", "The Billhooks", "The Gray Cloaks", "The Fog Hounds", "City Council or The Foundation", "Spirit Wardens", "Imperial Military", "Sparkwrights", "A Consulate", "Leviathan Hunters", "Gondoliers or Cabbies", "The Church of Ecstasy", "The Forgotten Gods", "Skovlander Refugees", "The Silver Nails", "The Hive", "The Crows", "The Red Sashes", "The Grinders", "The Wraiths", "Ulf Ironborn", "The Lost", "Ironhook Prison", "Bluecoats or Inspectors", "Laborers or Servants", "Cyphers or Ink Rakes", "Ministry of Preservation", "Sailors or Dockers", "Rail Jacks or The Brigade", "The Weeping Lady", "Path of Echoes or Reconciled", "Deathlands Scavengers"
    ]
    
    roll = random.randint(1, 6) * 10 + random.randint(1, 6)
    return factions[roll - 11]



def roll_opportunity_assassins():
    opportunities = [
        "Two feuding noble houses put out the call for hired killers.", "A fading noble house wants to exact revenge on their enemies list.", "A grieving noble lord or lady wants revenge for a child killed in a legal duel.", "A noble wants to eliminate their rival leviathan hunter captain before the next hunt.", "A noble wants to clear the way for a lucrative marriage—kill the rival suitor.", "A noble has been targeted by an underworld faction and will pay a hefty price to eliminate the gang leader—with little understanding of the consequences.", "A crime boss is facing serious charges and the inspector can’t be bought—kill the witnesses.", "The new city official is extorting extreme bribes for looking the other way. It’s just cheaper to kill them. You get several offers from different gangs.", "Three warring street gangs put out the call for hired killers.", "A powerful crime boss is enjoying safety in the prison ward they control. Their rival wants you to get in there and take them out.", "The last survivor of a destroyed underworld faction wants revenge.", "An underworld faction member has vanished with the treasury. Find them and kill them—and make it a good example for others.", "Two competing merchant houses put out a call for the assassination of their rival.", "An intelligence agent has identified a key Doskvol official whose death will serve a particular foreign interest.", "A cult requires a series of specific and bizarre killings to serve their dark rituals.", "A scorned lover wants their former partner (and their new paramour) dead.", "Several poor families offer you their combined savings to kill a cruel workhouse boss.", "A strangely lucid ghost will lead you to their killer for revenge—and then to a hidden treasure for your payment."
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Noble-related opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Crime-related opportunities
    else:
        return random.choice(opportunities[12:])  # Various other opportunities

import random

def roll_opportunity_bravos():
    opportunities = [
        "A jeweler has set up shop nearby. Lots of tempting pieces for the grabbing.", "A local merchant is telling everyone that they “never capitulate to brutes” and urges others to follow suit. People are listening.", "A channel fisherman wants his competitor’s boats destroyed.", "A tavern owner is plagued by rowdy brawls every night. They want an end to it.", "A distillery fires all their Skovlander workers and refuses to pay their wages for time already worked. The Skovs are camped outside, demanding justice.", "A group of merchants are seeking mercenary muscle to defy the local gang payoffs.", "The Bluecoats have set up watchtowers and checkpoints to search people for weapons and pad their arrest quotas.", "The city council wants leg-breakers to put an end to unionizing among the dockers.", "A noble has hired a small private army to guard their estate for some reason. Must be something worth defending in there...", "The sparkwrights are building a loud, clanking machine in a tower across from an apartment building. The tenants are outraged by the noise and smoke.", "Ironhook is hiring toughs to provide security for a special expedition into the deathlands. The scavengers are all death-row convicts.", "Skovlander soldiers have stolen an armed naval ship, and are assaulting craft in the channel.", "A rival gang keeps treasures from their crimes out in the open in their lair, expecting their fearsome reputation to dissuade any potential robbery.", "A group of vigilantes has appeared, crippling anyone they deem to be “criminal scum.”", "A vicious gang stalks the district, robbing with impunity and daring anyone to challenge them.", "A horde of hollows is loose in the underground canals, dragging people to watery deaths and terrorizing the area, shutting down commerce and vice.", "A gambling den operator needs a crew to make an example of a high-roller who skipped out on a huge debt.", "A vampire-hunter has come to Doskvol and needs assistance."
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Local and merchant-related opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Bluecoat and council-related opportunities
    else:
        return random.choice(opportunities[12:])  # Gang and other criminal-related opportunities


def roll_opportunity_cult():
    opportunities = [
        "A student at Doskvol Academy publishes a treatise claiming your god is a corrupted translation of an even more ancient god.", "It has become trendy for young people of high society to pretend to swoon and have visions, but not all of them are pretense.", "Construction work has accidentally unearthed an ancient spirit well, and awakened the entities trapped there since the cataclysm.", "A rival cult’s secret regalia have some connection with the Immortal Emperor: are they his agents or is it mere coincidence?", "A noble performed a desperate ritual seeking assistance from your god. You have been chosen as the instrument of its aid.", "A prominent collector of artifacts chokes to death in the streets, vomiting blackened blood and gasping the name of your god.", "A rival cult is destroying any and all artifacts and sites sacred to other gods. They seem to have some arcane means of discovery. You may be next.", "The murder of a noble has signs and sigils of your god left at the crime scene.", "Local citizens in the area around your lair have started working together at odd times, in a trance, constructing something alien out of strange debris.", "A trio of formidable ghosts arrive at your lair and announce themselves as the true ancient masters of your cult.", "The anointed champion of a rival cult challenges your chosen one to deadly combat.", "The Spirit Wardens intend to revive an ancient barbarism and burn a “witch” in the public square. Your god forbids this to occur, now or ever.", "A moldy tome has been recovered from the bag of a Tycherosi vagrant: it contradicts some vital tenet of your cult’s doctrine.", "A wealthy cult offers you riches (coin, claim, cohort, etc.) to abandon your faith and enter into their congregation.", "A leviathan hunter ship returns to port, devoid of crew or any items save one thing: a huge pyramid of alien metal, thrumming with the secret name of your god.", "A gang of thugs is having serious mystical problems from a rival group. They hire you to put an end to it.", "Blessed coins placed in the mouths of the faithful dead allow ghosts to return even after the Spirit Wardens have seen to them. Who is doing this? How?", "Your altars crumble, your artifacts crack. Demonstrate your true faith, or despair."
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Scholarly or societal opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Rival cult or ghost-related opportunities
    else:
        return random.choice(opportunities[12:])  # Mystical or faith-testing opportunities



def roll_opportunity_hawkers():
    opportunities = [
        "A taste-making dilettante noble is slumming in your area with their coterie of sycophants, looking for 'the next exciting thing.'", "A knock-off product shows up on the streets and undercuts your price. Is your supplier cutting you out?", "Your upscale clients are tired of coming to your territory for their fix. Set up a distribution front in a nicer part of town. (Or the same for low-class clients.)", "Students at Doskvol Academy have shown an interest in your supply, but they need it delivered to them, past the crisp Bluecoat security.", "A solo operator is providing a much more popular version of your product.", "A masked figure will pay you well for the opportunity to discreetly kill one of your regulars while they’re... distracted.", "A city council member is considering a total ban on an illicit product—they might be persuaded to make it yours, driving demand sky-high.", "The gang who operated your territory years ago is back from the Dagger Isles and expects to get back to business as usual.", "A Bluecoat killed their last dealer for 'pushing their relationship too far,' and comes to the crew for an alternate source.", "The smugglers in your supply chain want to cut out all intermediaries and deal with you directly.", "A legendary rip-off man and their crew are hitting stash houses. Now a bounty has been put on their head—can you claim it?", "A brutal gang of savage killers has wiped out a rival’s vice den. Now they want you to step in and run it for them.", "The cult of a forgotten god approaches you with an offer of partnership: they can make your product much more appealing in exchange for... special considerations.", "A fiery street-crier rails against your product and drives down demand. But you think you recognize them as a customer...", "A new vice gang is making really smart, savvy moves. Rumor is, they’re guided by the ghost of a legendary street operator.", "Ghosts of former customers are suddenly drawn back to you, demanding their fix.", "An arcane killer is targeting vice-users and dealers, leaving their hollowed shells wandering the streets.", "An infamous leviathan hunter has tastes that... you probably don’t usually provide for. But she’s willing to pay very well."
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Product and client-related opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Gang and smuggler-related opportunities
    else:
        return random.choice(opportunities[12:])  # Cult, ghost, and other unique opportunities




def roll_opportunity_shadows():
    opportunities = [
        "A local art dealer announces an exhibition of rare ancient Iruvian jewelry.", "The Path of Echoes needs a specific body purloined from the crematorium before it’s dissolved tonight.", "A collector wants to steal an original work of art or industry and replace it with a forgery.", "A client wants to extract a loved one from their servitude in an indentured work house.", "A ghost wants you to secure the rest of their precious collection of worldly things.", "A master assassin has come out of retirement for one more job. Many would pay well to know who their target is.", "The black sheep of a noble family wants their revenge, and the deed to the ancestral estate is the key.", "A drug gang wants to obtain the secret formula for their rival’s popular new product.", "Strange artifacts were recovered from the Void Sea. They’re held at Bellweather for analysis by the Spirit Wardens.", "Rumors of war, aren’t there always? Plant a damning paper trail in the office of the ambassador.", "Anti-Imperial agents are passing information while on the trains. Intercept their communiques.", "A professor in Sparkwright Tower wants their rival’s research notes. Make it look like a common burglary.", "A Bluecoat squad doesn’t want to make a very dangerous arrest. Steal the evidence from the Inspector’s safe.", "A damning piece of evidence against a vulnerable crime lord is held in a bank vault until trial.", "A client seeks the source of altered texts sold to academy students that are driving them to madness and murder.", "A desperate Inspector needs you to plant evidence to bring down a demon-corrupted Spirit Warden.", "A circus is in town, featuring strange creatures and mysterious animals. A client would pay well for a new pet.", "Only one gang member survived their botched job. Can you clean the bloody scene before the authorities arrive?"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Art, body, and personal extraction-related opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Revenge, drugs, and artifact-related opportunities
    else:
        return random.choice(opportunities[12:])  # Evidence, texts, and other unique opportunities



def roll_opportunity_smugglers():
    opportunities = [
        "Skovlander insurrectionists need supplies for their campaign of terror attacks against city institutions.", "Union organizers want to arm factory workers in advance of a strike.", "A massive gang war creates high demand for restricted military weapons and heavy ordnance.", "Exiled nobility slumming it in Doskvol has a sudden and urgent need to go home that they won’t explain.", "Leviathan hunter made undocumented stops. Meet them outside the city and bring some things in uninspected.", "Heiress needs to leave the city to meet her forbidden love. If you make it look like a kidnapping she’ll split the ransom.", "The city council outlaws a formerly legal product.", "A jailbreak at Ironhook means many escaped prisoners seek flight from the city.", "For a nominal fee, a Bluecoat will help you acquire a vehicle seized from another gang.", "A new spice has been “discovered” in Tycheros but it’s officially banned. Naturally, everyone wants it.", "A route is closed to traffic (and Bluecoat inspection) due to: imminent collapse—weird events—toxic gas—fires.", "A criminal organization needs weapons smuggled into Ironhook to seize control of a cell-block.", "A cult wants to smuggle their demon-tainted “chosen one” past the Spirit Wardens and out into the deathlands.", "An ancient artifact has been spotted outside the barrier and academics need it in the city yesterday. For study, of course.", "A district is quarantined due to ghost infestation or plague. They need basic supplies, and spirit wards even more.", "A client wants you to move a strange package around the city for two days straight. Don’t stop moving! That would be bad.", "A derailed train in the deathlands has a lot of salvageable cargo. Possibly (wealthy and grateful) survivors, too.", "A noble’s crimes leave their assets frozen. Their leviathan hunter, full from an expedition, is forbidden to dock."
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(opportunities[:6])  # Supplies, weapons, and urgent travel-related opportunities
    elif roll <= 4:
        return random.choice(opportunities[6:12])  # Legal changes, jailbreaks, and new products
    else:
        return random.choice(opportunities[12:])  # Cult, artifact, and quarantine-related opportunities


def roll_contraband():
    contraband = [
        "Escaped Prisoners, Spies (forbidden)", "Workers Fleeing Contracts (forbidden)", "A Devil or Dangerous Artifact (forbidden)", "Insurrectionists or Anarchists (forbidden)", "Refugees or Immigrants (restricted access)", "A Noble or Official Seeking Secret Travel", "Fine Tobacco, Whiskey, Wine, etc. (high tax)", "Luxuries—Perfumes, Silks, Spices (high tax)", "Livestock or Dangerous Animals (restricted ownership)", "Medicine, Alchemicals (restricted ownership)", "Military Arms (restricted ownership)", "Drugs (high tax)", "Confidential Documents (restricted ownership)", "Banned Art, Seditious Materials (restricted ownership)", "Arcane Implements or Documents (forbidden)", "Electroplasmic Tech (restricted ownership)", "Volatile Alchemicals or Explosives (forbidden)", "Spirit Essences (restricted ownership)"
    ]
    
    roll = random.randint(1, 6)
    if roll <= 2:
        return random.choice(contraband[:6])  # Forbidden and restricted people
    elif roll <= 4:
        return random.choice(contraband[6:12])  # High tax and restricted goods
    else:
        return random.choice(contraband[12:])  # Restricted and forbidden documents and items


def roll_opportunity():
    opportunity_type = random.choice([
        "assassins", "bravos", "cult", "hawkers", "shadows", "smugglers"
    ])
    
    if opportunity_type == "assassins":
        return roll_opportunity_assassins()
    elif opportunity_type == "bravos":
        return roll_opportunity_bravos()
    elif opportunity_type == "cult":
        return roll_opportunity_cult()
    elif opportunity_type == "hawkers":
        return roll_opportunity_hawkers()
    elif opportunity_type == "shadows":
        return roll_opportunity_shadows()
    else:  # smugglers
        contraband = roll_contraband()
        return f"{roll_opportunity_smugglers()} ({contraband})"

# Example usage:
print(roll_opportunity())

