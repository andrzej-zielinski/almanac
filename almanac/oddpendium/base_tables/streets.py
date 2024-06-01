import random

def roll_point_of_interest():
    points_of_interest = [
        "Brewery", "Meeting Fountain", "Meeting Fountain", "Meeting Fountain", "Meeting Fountain", 
        "Restaurant", "Restaurant", "Restaurant", "Sunken Pit", "Bar", "Bar", "Bar", "Fighting Den", 
        "Fighting Den", "Castle", "Castle", "City Wall", "City Wall", "Huge Factory", "Huge Factory", 
        "Huge Factory", "Coal Heap", "Coal Heap", "Coal Heap", "Poorhouse", "Poorhouse", "Poorhouse", 
        "Public Baths", "Public Baths", "Public Baths", "Public Baths", "Observatory", "Observatory", 
        "Observatory", "Observatory", "University", "University", "Building Site", "Building Site", 
        "Building Site", "Winding Alleyways", "Winding Alleyways", "Winding Alleyways", "Shop Row", 
        "Shop Row", "Shop Row", "Residential Terrace", "Residential Terrace", "Residential Terrace", 
        "Botanical Garden", "Botanical Garden", "Botanical Garden", "Cult Temple", "Cult Temple", 
        "Docks", "Docks", "Warehouses", "Warehouses", "Underground Shelter", "Underground Shelter", 
        "Underground Shelter", "School", "School", "School", "Ironworks", "Ironworks", "Ironworks", 
        "Ironworks", "Canal Dock", "Canal Dock", "Amusement Complex", "Amusement Complex", 
        "Amusement Complex", "Specialist Shops", "Specialist Shops", "Bridge", "Bridge", "Manor", 
        "Manor", "Guild House", "Guild House", "Guild House", "Army Barracks", "Shopping Arcade", 
        "Shopping Arcade", "Watchtower", "Watchtower", "City Watch Station", "City Watch Station", 
        "Hospital", "Hospital", "Cult Cathedral", "Cult Cathedral", "Shrine"
    ]
    return random.choice(points_of_interest)

def roll_atmosphere():
    atmospheres = [
        "Welcoming", "Dark", "Dark", "Dark", "Smoggy", "Smoggy", "Abandoned", "Abandoned", "Bustling", 
        "Bustling", "Bustling", "Brightly Lit", "Brightly Lit", "Creepy", "Creepy", "Drafty", "Drafty", 
        "Sinister", "Sinister", "Sinister", "Comforting", "Comforting", "Comforting", "Rat-Infested", 
        "Rat-Infested", "Rat-Infested", "Expensive", "Expensive", "Expensive", "Expensive", "In Poverty", 
        "In Poverty", "In Poverty", "In Poverty", "Dusty", "Dusty", "Freshly Built", "Freshly Built", 
        "Freshly Built", "Ruined", "Ruined", "Ruined", "Burnt", "Burnt", "Burnt", "On Fire!", "On Fire!", 
        "On Fire!", "Overrun by Rioters", "Overrun by Rioters", "Overrun by Rioters", "Bird Infested", 
        "Bird Infested", "Falling Down", "Falling Down", "Ancient", "Ancient", "Artistic", "Artistic", 
        "Artistic", "Eccentric", "Eccentric", "Eccentric", "Physics-Defying", "Physics-Defying", 
        "Physics-Defying", "Physics-Defying", "Underground", "Underground", "Overgrown", "Overgrown", 
        "Overgrown", "Hidden", "Hidden", "Criminal", "Criminal", "Council-Sanctioned", "Council-Sanctioned", 
        "Rebellious", "Rebellious", "Rebellious", "Protesting", "Cult-Linked", "Cult-Linked", "Dangerous", 
        "Dangerous", "Filthy", "Filthy", "Overrun by Orphans", "Overrun by Orphans", "Fearful", "Fearful", 
        "Insane"
    ]
    return random.choice(atmospheres)

def roll_link_to_underground():
    links_to_underground = [
        "No.", "Probably in the next road down.", "Probably in the next road down.", "Probably in the next road down.", "Probably in the next road down.", "No, and why are you so interested?", "No, and why are you so interested?", "No, and why are you so interested?", "No, we don't want Weirdos coming up.", "No, it's too dangerous to leave them open.", "No, it's too dangerous to leave them open.", "No, it's too dangerous to leave them open.", "Sure! Oh, wait, it's gone.", "Sure! Oh, wait, it's gone.", "Yes, but the tunnels are too hot to survive.", "Yes, but the tunnels are too hot to survive.", "No, soldiers came and sealed it up.", "No, soldiers came and sealed it up.", "Yes, but it leads straight into an acid pool.", "Yes, but it leads straight into an acid pool.", "Yes, but it leads straight into an acid pool.", "Nobody wants to talk about the Underground.", "Nobody wants to talk about the Underground.", "We dug this one quite recently.", "We dug this one quite recently.", "An escape tunnel out of town.", "An escape tunnel out of town.", "An escape tunnel out of town.", "Yeah, an old trapdoor.", "Yeah, an old trapdoor.", "Yeah, an old trapdoor.", "A wine cellar leads into somewhere horrible.", "A wine cellar leads into somewhere horrible.", "A wine cellar leads into somewhere horrible.", "A wine cellar leads into somewhere horrible.", "This tunnel goes right across town.", "This tunnel goes right across town.", "A particularly disgusting sewer.", "A particularly disgusting sewer.", "An old bank vault.", "An old bank vault.", "Smugglers have set up tunnels around here.", "Smugglers have set up tunnels around here.", "Smugglers have set up tunnels around here.", "They all got sealed up years ago.", "They all got sealed up years ago.", "They all got sealed up years ago.", "There's a tunnel in plain sight.", "There's a tunnel in plain sight.", "There's a tunnel in plain sight.", "Hidden stairway indoors.", "Hidden stairway indoors.", "Hidden stairway indoors.", "A hole opened up last week.", "A hole opened up last week.", "A hole opened up last week.", "Nasty things burst from the ground here.", "Nasty things burst from the ground here.", "An old vault entrance.", "An old vault entrance.", "Emergency shelter nearby.", "Emergency shelter nearby.", "Just a chute straight down.", "Just a chute straight down.", "Just a chute straight down.", "Spiral staircase ornately decorated.", "Spiral staircase ornately decorated.", "Spiral staircase ornately decorated.", "Spiral staircase ornately decorated.", "An overgrown natural cave.", "An overgrown natural cave.", "An overgrown natural cave.", "Tunnel at the bottom of a pond.", "Tunnel at the bottom of a pond.", "Open sewer.", "Open sewer.", "An old well.", "An old well.", "Rusty ladder down a chute.", "Rusty ladder down a chute.", "Rusty ladder down a chute.", "It caved in recently.", "It caved in recently.", "An old elevator.", "A newly fitted elevator.", "A newly fitted elevator.", "A newly fitted elevator.", "The hole where they throw their rubbish.", "The hole where they throw their rubbish.", "Huge pit into the darkness.", "Huge pit into the darkness.", "Tunnel at the bottom of the river.", "Tunnel at the bottom of the river.", "Natural cave in somebody's cellar."
    ]
    return random.choice(links_to_underground)

def roll_quickest_route_across_town():
    routes = [
        "Crawl-Tunnel", "Funicular", "Funicular", "Funicular", "Funicular", "Horse Carriage", "Horse Carriage", "Horse Carriage", "Underground Carriageway", "Canal Boat", "Canal Boat", "Canal Boat", "Underground Canal", "Underground Canal", "Shadey Alleyways", "Shadey Alleyways", "Straight Through the Park", "Straight Through the Park", "Along the Docks", "Along the Docks", "Along the Docks", "Rooftop Walkway", "Rooftop Walkway", "Down the High Street", "Down the High Street", "Through a Riot", "Through a Riot", "Through a Riot", "Underground Tramway", "Underground Tramway", "Underground Tramway", "Underground Tramway", "Tunnel with Toll Booth", "Tunnel with Toll Booth", "Tunnel with Toll Booth", "Tunnel with Toll Booth", "Hired Carriage", "Hired Carriage", "Through an Abandoned Warehouse", "Through an Abandoned Warehouse", "Through a Working Factory", "Through a Working Factory", "Through the Slums", "Through the Slums", "Through the Slums", "Through the Rich Neighbourhoods", "Through the Rich Neighbourhoods", "Along the City Walls", "Along the City Walls", "Along the City Walls", "Steamboat Down the River", "Steamboat Down the River", "Steamboat Down the River", "Rickshaw", "Rickshaw", "Rickshaw", "Underground Tunnels", "Underground Tunnels", "Through the Market", "Through the Market", "The Wine Cellar Network", "The Wine Cellar Network", "Catacombs", "Catacombs", "Catacombs", "Through the Old Town", "Through the Old Town", "Through the Old Town", "Through the Old Town", "Urgh, Sewers", "Urgh, Sewers", "Urgh, Sewers", "Urgh, Sewers", "Through the Bad End of Town", "Through the Bad End of Town", "Across University Campus", "Across University Campus", "Through the Botanical Gardens", "Through the Botanical Gardens", "Along the Canals", "Along the Canals", "Along the Canals", "Over a Ruined Castle", "Over a Ruined Castle", "Through the Graveyard Quarter", "Through the Graveyard Quarter", "Up the Hill, then Back Down", "Up the Hill, then Back Down", "Up the Hill, then Back Down", "Right Through the Crazy Part of Town", "Right Through the Crazy Part of Town", "Through a Cult Temple", "Through a Cult Temple", "Past the Army Barracks", "Past the Army Barracks", "Through the Smuggler Tunnels"
    ]
    return random.choice(routes)

def roll_business_name():
    business_names = [
        "Cage-Brand Steam Generators", "Pickem's Enterprise Loans", "Pickem's Enterprise Loans", "Pickem's Enterprise Loans", "Pickem's Enterprise Loans", "Anise Sisters Security Wire", "Anise Sisters Security Wire", "Anise Sisters Security Wire", "Gasman Spice & Soap", "Prospective Telecoms", "Prospective Telecoms", "Prospective Telecoms", "The Lady's Sugar and Coffeehouse", "The Lady's Sugar and Coffeehouse", "Yesser's Wool and Meat", "Yesser's Wool and Meat", "Secure Properties and Jails", "Secure Properties and Jails", "Consolidated Bookmakers", "Consolidated Bookmakers", "Consolidated Bookmakers", "Commercial Voice Printed Press", "Commercial Voice Printed Press", "Commercial Voice Printed Press", "Commercial Voice Printed Press", "Gallow, Sniff, & Pine Medical Research", "Gallow, Sniff, & Pine Medical Research", "Gallow, Sniff, & Pine Medical Research", "Claymore Bank & Private Military", "Claymore Bank & Private Military", "Claymore Bank & Private Military", "Claymore Bank & Private Military", "Broken Compass Offshore Acquisitions", "Broken Compass Offshore Acquisitions", "Broken Compass Offshore Acquisitions", "Broken Compass Offshore Acquisitions", "Baker Arms & Munitions", "Baker Arms & Munitions", "Cohen Mass Nutrition Solutions", "Cohen Mass Nutrition Solutions", "Cohen Mass Nutrition Solutions", "Footman Stills Spirits & Tonics", "Footman Stills Spirits & Tonics", "Footman Stills Spirits & Tonics", "Braker's Streetlamp and Halberd", "Braker's Streetlamp and Halberd", "Braker's Streetlamp and Halberd", "Black Horse Hospitals and Asylums", "Black Horse Hospitals and Asylums", "Black Horse Hospitals and Asylums", "Bastio-Goldish Coal, Oil, and Ore", "Bastio-Goldish Coal, Oil, and Ore", "Bastio-Goldish Coal, Oil, and Ore", "Confectioner's Village Foods & Homes", "Confectioner's Village Foods & Homes", "Confectioner's Village Foods & Homes", "Red Ghost Roads & Carriages", "Red Ghost Roads & Carriages", "Freeman Brewers & Bakers", "Freeman Brewers & Bakers", "Drake Ships & Sails", "Drake Ships & Sails", "Drake Ships & Sails", "Shooman Boots & Tonics", "Shooman Boots & Tonics", "Shooman Boots & Tonics", "Bates' Smoke Farms", "Bates' Smoke Farms", "Bates' Smoke Farms", "Bates' Smoke Farms", "Great Underground Disposal Company", "Clock's Shippage & Canals", "Clock's Shippage & Canals", "Clock's Shippage & Canals", "Hightower Hats & Canes", "Hightower Hats & Canes", "Territorial Tea & Wine", "Territorial Tea & Wine", "Outlander's Exotic Down & Fur", "Outlander's Exotic Down & Fur", "Furrupp's Brick & Mortar", "Furrupp's Brick & Mortar", "Furrupp's Brick & Mortar", "Bitter & Snatch Jewellery", "Werner's Industrial Machinery", "Werner's Industrial Machinery", "Silvermountain Private Security", "Silvermountain Private Security", "Aria Mines", "Aria Mines", "Miracle Factory Ice & Salt", "Miracle Factory Ice & Salt", "Metropolitan Tramway", "Metropolitan Tramway", "Sunfair Gold Holdings"
    ]
    return random.choice(business_names)

def roll_council_decision():
    council_decisions = [
        "All Arcana must be registered", "War with all other cities!", "Major cult is outlawed", 
        "Entire quarter to be flattened", "Army conscription", "New council-sanctioned cult", 
        "Same-sex marriage to be outlawed", "All prisoners to be executed", "All prisoners to be released", 
        "Launching a Cosmic Rocket!", "Double taxes!", "Mass eviction!", "Close the gates! Total lockdown", 
        "Inquisition into possible rebellion", "Entire council executed and replaced", 
        "Colonising the Golden Lands!", "Underground Crusade!", "Guns outlawed", "Alcohol prohibited", "Martial Law"
    ]
    return random.choice(council_decisions)

def roll_public_reaction():
    public_reactions = [
        "Riots!", "Tomorrow we launch an uprising!", "Someone should do something!", 
        "Don't care.", "They probably have a good reason!", "Well it's about time!"
    ]
    return random.choice(public_reactions)

