import random

def roll_nature():
    natures = [
        "Solid-Smoke", "Skeletal", "Skeletal", "Skeletal", "Decaying", "Decaying", "Luxurious", 
        "Luxurious", "Bio-Machine", "Bio-Machine", "Living Construct", "Living Construct", 
        "Reptilian", "Reptilian", "Slime Covered", "Slime Covered", "Glassy", "Glassy", 
        "Liquid Metal", "Liquid Metal", "Liquid Metal", "Ceramic", "Ceramic", "Ceramic", 
        "Living Rock", "Living Rock", "Living Rock", "Scabs and Sores", "Scabs and Sores", 
        "Hyper-Robotic", "Hyper-Robotic", "Spiny", "Spiny", "Spiny", "Stinking Filth", 
        "Stinking Filth", "Shadow-Cloaked", "Shadow-Cloaked", "Eerily Beautiful", 
        "Eerily Beautiful", "Mechanical", "Mechanical", "Sapient and Armoured", 
        "Sapient and Armoured", "Baroque Excess", "Leathery", "Leathery", "Feathered", 
        "Feathered", "Pale and Bald", "Pale and Bald", "Ghostly", "Ghostly", "Ghostly", 
        "Holographic", "Holographic", "Hardlight", "Hardlight", "Acid Dripping", 
        "Acid Dripping", "Shaggy Hair", "Shaggy Hair", "Mirrored Metal", "Mirrored Metal", 
        "Damp Clay", "Damp Clay", "Colossal", "Bare Musculature", "Bare Musculature", 
        "All-Brain", "Plasmic", "Plasmic", "Chitin", "Chitin", "Rusted", "Rusted", "Bionic Parts"
    ]
    return random.choice(natures)

def roll_form():
    forms = [
        "Cube", "Tripod", "Tripod", "Tripod", "Swarm", "Swarm", "Hand", "Hand", "Worm", 
        "Worm", "Sphere", "Sphere", "Hound", "Hound", "Great Cat", "Great Cat", "Snake", 
        "Snake", "Crustacean", "Crustacean", "Crustacean", "Squat Biped", "Squat Biped", 
        "Squat Biped", "Slender Biped", "Slender Biped", "Slender Biped", "Insect", "Insect", 
        "Obese Biped", "Obese Biped", "Towering Biped", "Towering Biped", "Towering Biped", 
        "Baby Bird", "Baby Bird", "Slug", "Slug", "Snail", "Snail", "Suit", "Suit", "Terror-Bird", 
        "Terror-Bird", "Bull", "Shark", "Shark", "Spider", "Spider", "Blob", "Blob", "Spiral", 
        "Spiral", "Spiral", "Pyramid", "Pyramid", "Sheet", "Sheet", "Wasp", "Wasp", "Maggot", 
        "Maggot", "Tadpole", "Tadpole", "Jellyfish", "Jellyfish", "Bat", "Octopus", "Octopus", 
        "Pike", "Sea Urchin", "Sea Urchin", "Cannon", "Cannon", "Fly", "Fly", "Fetal"
    ]
    return random.choice(forms)

def roll_twist():
    twists = [
        "Mastery of Magnetism", "Grasps with Extra Limbs", "Grasps with Extra Limbs", "Grasps with Extra Limbs", "Phases Through Matter", "Phases Through Matter", "Phases Through Matter", "Chimera (roll additional Form)", "Reads Minds", "Reads Minds", "Reads Minds", "Colossal Size", "Colossal Size", "Drains Life", "Drains Life", "Sprays Acid", "Sprays Acid", "Creates Black-Holes", "Creates Black-Holes", "Creates Black-Holes", "Teleports Self", "Teleports Self", "Teleports Self", "Teleports Others", "Teleports Others", "Teleports Others", "Shifts Shape", "Shifts Shape", "Shifts Shape", "Shifts Shape", "Breathes Smoke", "Breathes Smoke", "Creates Electric Charge", "Creates Electric Charge", "Sees Future", "Sees Future", "Controls Others", "Controls Others", "Cloaking Device", "Cloaking Device", "Cloaking Device", "Conjures Illusions", "Conjures Illusions", "Conjures Illusions", "Infects with Disease", "Infects with Disease", "Infects with Disease", "Kills with Venom", "Kills with Venom", "Kills with Venom", "Hunts Arcana", "Fires Bullets", "Fires Bullets", "Freeze Matter", "Freeze Matter", "Heat/Melt Matter", "Heat/Melt Matter", "Heat/Melt Matter", "Implants with Egg/Parasite", "Implants with Egg/Parasite", "Paralyzes with Touch", "Paralyzes with Touch", "Fires Death Rays", "Fires Death Rays", "Manipulates Living Tissue Telekenetically", "Manipulates Living Tissue Telekenetically", "Manipulates Objects Telekenetically", "Manipulates Objects Telekenetically", "Sees Distant Places", "Sees Distant Places", "Regenerates from Any Harm", "Regenerates from Any Harm", "Reflects Harm onto Attacker", "Absorbs Victims into Body", "Absorbs Victims into Body", "Turns Victims into Non-Living Matter", "Turns Victims into Non-Living Matter", "Launch Explosives", "Launch Explosives", "Cause Intense Pain at Touch", "Cause Intense Pain at Touch", "Heal Any Harm with a Touch", "Heal Any Harm with a Touch", "Sense Distant Objects"
    ]
    return random.choice(twists)

