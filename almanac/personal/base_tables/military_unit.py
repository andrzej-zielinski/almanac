import random

def roll_unit_type():
    types = [
        "Arcane Archers (Magical ranged combat)",
        "Battleragers (Berserker melee fighters)",
        "Beastmasters (Animal control and coordination)",
        "Chronomancers (Time manipulation specialists)",
        "Dragonriders (Aerial cavalry)",
        "Elemental Shamans (Elemental magic users)",
        "Golem Engineers (Construct creators and controllers)",
        "Illusionists (Deception and misdirection experts)",
        "Inquisitors (Anti-magic and heretic hunters)",
        "Necromancers (Undead summoners and controllers)",
        "Planar Binders (Extraplanar entity summoners)",
        "Psionic Knights (Mind-powered warriors)",
        "Runesmiths (Magical item crafters and enhancers)",
        "Shadow Assassins (Stealth and assassination experts)",
        "Siege Mages (Fortification attackers/defenders)",
        "Spellblades (Magic and melee combat hybrids)",
        "Storm Callers (Weather manipulation specialists)",
        "Swarmkeepers (Insect or small creature controllers)",
        "Technomancers (Magical technology specialists)",
        "Voidwalkers (Teleportation and spatial manipulation experts)"
    ]
    return random.choice(types)

def roll_main_ability():
    abilities = [
        "Arcane Bombardment (Area-of-effect magical damage)",
        "Blink Strike (Teleportation attack)",
        "Chaos Orb (Unpredictable magical effect)",
        "Doppelganger Cloak (Creates illusory duplicates)",
        "Elemental Fusion (Combines elemental powers)",
        "Enchanted Weaponry (Magically enhanced arms)",
        "Energy Siphon (Drains and redirects magical energy)",
        "Farsight Scope (Extreme long-range targeting)",
        "Golem Armor (Living construct armor)",
        "Gravity Well (Manipulates local gravity)",
        "Mind Shatter (Psychic attack)",
        "Phantasmal Terror (Fear-inducing illusions)",
        "Planar Anchor (Creates/closes planar portals)",
        "Runic Augmentation (Enhances allies' abilities)",
        "Soulbound Weapon (Weapon linked to user's life force)",
        "Temporal Shift (Brief time manipulation)",
        "Venom Burst (Area-of-effect poison attack)",
        "Void Shield (Absorbs and nullifies attacks)",
        "Weather Control Device (Localized climate manipulation)",
        "Wild Shape Mastery (Advanced shapeshifting)"
    ]
    return random.choice(abilities)

def roll_psychological_trait():
    traits = [
        "Fanatical Devotion (Unwavering loyalty to their cause)",
        "Hive Mind (Linked consciousness within the unit)",
        "Emotionless Efficiency (Coldly logical approach to combat)",
        "Battle Frenzy (Enter a state of controlled rage)",
        "Tactical Genius (Exceptional strategic thinking)",
        "Mystic Serenity (Calm focus even in chaos)",
        "Adaptive Mindset (Quick to change tactics)",
        "Psychic Resilience (Strong mental defenses)",
        "Berserker Rage (Uncontrolled fury in battle)",
        "Eldritch Madness (Insanity granting unpredictable power)",
        "Collective Courage (Draw bravery from unity)",
        "Predatory Instinct (Animalistic hunting behavior)"
    ]
    return random.choice(traits)

def roll_secondary_ability():
    abilities = [
        "Accelerated Healing (Fast recovery from wounds)",
        "Arcane Sight (Can see magical auras)",
        "Chameleon Skin (Natural camouflage)",
        "Corrosive Blood (Acid blood damages attackers)",
        "Dreamwalking (Can enter and manipulate dreams)",
        "Elemental Affinity (Resistant to a type of elemental damage)",
        "Empathic Link (Can sense allies' emotions and status)",
        "Energy Absorption (Can absorb and redirect energy attacks)",
        "Featherfall (Immune to falling damage)",
        "Linguistic Genius (Can quickly learn and speak any language)",
        "Mage Bane (Disrupts enemy spellcasting)",
        "Phasing (Can become intangible briefly)",
        "Photosynthetic Skin (Can survive without food in sunlight)",
        "Psionic Projection (Can create solid thought constructs)",
        "Regenerative Nanites (Microscopic healing machines in bloodstream)",
        "Shared Pain (Distributes damage among nearby allies)",
        "Sonic Scream (Powerful sound-based attack)",
        "Spirit Sight (Can see invisible and ethereal beings)",
        "Technopathy (Can communicate with and control machines)",
        "Vampiric Touch (Heals by dealing damage)"
    ]
    return random.choice(abilities)

def roll_narrative_purpose():
    purposes = [
        "Knowledge Seekers: Collect and preserve arcane lore, often venturing into dangerous areas for rare tomes or artifacts.",
        "Relic Hunters: Search for powerful magical items, either to use or to keep out of the wrong hands.",
        "Elemental Balancers: Maintain equilibrium between elemental forces, preventing natural disasters.",
        "Planar Guardians: Protect the material plane from extraplanar threats, closing dangerous portals.",
        "Beast Whisperers: Communicate with and calm dangerous creatures, acting as mediators between civilization and wildlife.",
        "Curse Breakers: Specialize in removing ancient curses and cleansing corrupted lands.",
        "Mindscape Explorers: Enter and navigate the realms of dreams and thoughts, battling psychic threats.",
        "Time Wardens: Prevent temporal anomalies and protect the flow of history.",
        "Soul Shepherds: Guide and protect spirits, preventing them from becoming vengeful ghosts.",
        "Living Archives: Each member memorizes vast amounts of information, preserving knowledge even if physical records are lost.",
        "Ley Line Maintainers: Monitor and repair the world's magical energy grid, preventing catastrophic magical events.",
        "Oath Enforcers: Magically bind and enforce contracts between powerful entities, maintaining cosmic balance.",
        "Harmony Resonators: Their mere presence bolsters allies' morale and weakens enemy resolve through supernatural auras.",
        "Fate Weavers: Manipulate strands of destiny, subtly influencing future events.",
        "Golem Crafters: Create and maintain magical constructs used for labor and defense in civilian areas.",
        "Planeshift Diplomats: Negotiate with extraplanar entities, maintaining peace between realms.",
        "Mage Hunters: Track down and neutralize rogue magic users, preventing arcane disasters.",
        "Bloodline Guardians: Protect and nurture specific magical bloodlines crucial to the world's future.",
        "Reality Anchors: Their presence stabilizes areas of wild magic, allowing safer magic use for allies.",
        "Veil Keepers: Maintain the separation between the magical and mundane worlds, preserving the balance of power."
    ]
    return random.choice(purposes)

