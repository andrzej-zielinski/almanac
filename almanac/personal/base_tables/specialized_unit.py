import random

def roll(table):
    return random.choice(table)

# Table 1: Group Focus
group_focuses = [
    "Arcane Research", "Martial Arts", "Beast Mastery", "Alchemy", "Diplomacy",
    "Craftsmanship", "Espionage", "Nature Cultivation", "Planar Studies", "Healing Arts",
    "Prophecy and Divination", "Mechanical Engineering", "Elemental Manipulation",
    "Necromancy", "Illusion and Deception", "Psionics", "Enchantment", "Archaeology",
    "Shapeshifting", "Trade and Commerce"
]

# Table 2: Signature Ability
signature_abilities = [
    "Runic Enchantment", "Celestial Divination", "Wild Shape", "Golem Crafting",
    "Mind Reading", "Elemental Conjuration", "Astral Projection", "Potion Brewing",
    "Soul Binding", "Time Manipulation", "Teleportation", "Weather Control",
    "Dream Walking", "Invisibility", "Transmutation", "Energy Absorption",
    "Dimensional Pocket Creation", "Linguistic Mastery", "Gravity Manipulation",
    "Life Force Manipulation"
]

# Table 3: Cultural Trait
cultural_traits = [
    "Oath-bound Secrecy", "Generational Knowledge", "Ascetic Lifestyle",
    "Collective Consciousness", "Ritualistic Practices", "Technological Integration",
    "Symbiosis with Nature", "Ancestral Worship", "Constant Experimentation",
    "Nomadic Existence", "Hierarchical Structure", "Democratic Decision-making"
]

# Table 4: Societal Role
societal_roles = [
    "Keepers of Ancient Knowledge", "Protectors of the Realm", "Mediators between Worlds",
    "Sustainers of Life", "Enforcers of Justice", "Creators of Wonders",
    "Balancers of Power", "Preservers of Nature", "Predictors of the Future",
    "Healers of Body and Mind", "Shapers of Culture", "Explorers of the Unknown"
]

# Table 5: Limitation or Weakness
limitations = [
    "Reliance on Rare Resource", "Vulnerable to Specific Magic/Technology",
    "Bound by Strict Code of Conduct", "Limited by Planetary Alignment",
    "Susceptible to Corruption", "Slow Reproduction/Recruitment", "Physically Frail",
    "Emotionally Unstable", "Technologically Inept", "Socially Outcast"
]

def generate_specialized_group():
    group = {
        "Group Focus": roll(group_focuses),
        "Signature Ability": roll(signature_abilities),
        "Cultural Trait": roll(cultural_traits),
        "Societal Role": roll(societal_roles),
        "Limitation or Weakness": roll(limitations)
    }
    return group

def display_specialized_group(group):
    print("Specialized Group Profile:")
    print("==========================")
    for key, value in group.items():
        print(f"{key}: {value}")
    print("\nGroup Description:")
    print("==================")
    print(f"This group of {group['Group Focus']} specialists is known for their mastery of {group['Signature Ability']}.")
    print(f"Their culture is characterized by {group['Cultural Trait']}, and they serve society as {group['Societal Role']}.")
    print(f"However, they face challenges due to their {group['Limitation or Weakness']}.")
    print("\nThis unique combination of traits sets them apart in the world and influences their interactions with other factions and individuals.")

# Example usage
if __name__ == "__main__":
    group = generate_specialized_group()
    display_specialized_group(group)