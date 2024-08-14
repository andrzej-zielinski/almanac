from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto

from enum import Enum
import random

class SHADOWDARK_BACKGROUND(Enum):
    URCHIN = ("Urchin", "You grew up in the merciless streets of a large city")
    WANTED = ("Wanted", "There's a price on your head, but you have allies")
    CULT_INITIATE = ("Cult Initiate", "You know blasphemous secrets and rituals")
    THIEVES_GUILD = ("Thieves' Guild", "You have connections, contacts, and debts")
    BANISHED = ("Banished", "Your people cast you out for supposed crimes")
    ORPHANED = ("Orphaned", "An unusual guardian rescued and raised you")
    WIZARDS_APPRENTICE = ("Wizard's Apprentice", "You have a knack and eye for magic")
    JEWELER = ("Jeweler", "You can easily appraise value and authenticity")
    HERBALIST = ("Herbalist", "You know plants, medicines, and poisons")
    BARBARIAN = ("Barbarian", "You left the horde, but it never quite left you")
    MERCENARY = ("Mercenary", "You fought friend and foe alike for your coin")
    SAILOR = ("Sailor", "Pirate, privateer, or merchant — the seas are yours")
    ACOLYTE = ("Acolyte", "You're well trained in religious rites and doctrines")
    SOLDIER = ("Soldier", "You served as a fighter in an organized army")
    RANGER = ("Ranger", "The woods and wilds are your true home")
    SCOUT = ("Scout", "You survived on stealth, observation, and speed")
    MINSTREL = ("Minstrel", "You've traveled far with your charm and talent")
    SCHOLAR = ("Scholar", "You know much about ancient history and lore")
    NOBLE = ("Noble", "A famous name has opened many doors for you")
    CHIRURGEON = ("Chirurgeon", "You know anatomy, surgery, and first aid")

    def __init__(self, title, description):
        self.title = title
        self.description = description



class SHADOWDARK_ANCESTRY(Enum):
    DWARF = auto()
    ELF = auto()
    GOBLIN = auto()
    HALF_ORC = auto()
    HALFLING = auto()
    HUMAN = auto()

class SHADOWDARK_CLASS(Enum):
    FIGHTER = auto()
    PRIEST = auto()
    THIEF = auto()
    WIZARD = auto()
    BARD = auto()
    RANGER = auto()

@dataclass
class SHADOWDARK_CHARACTER:
    name: str
    background: SHADOWDARK_BACKGROUND    
    _ancestry: SHADOWDARK_ANCESTRY
    _character_class: SHADOWDARK_CLASS
        
    hp: int
    max_hp: int
    ac: int
    level: int = 0
    xp: int = 0
    alignment: str = "Neutral"
    deity: Optional[str] = None
    title: str = "Novice"
    _strength: int = field(default=10)
    _dexterity: int = field(default=10)
    _constitution: int = field(default=10)
    _intelligence: int = field(default=10)
    _wisdom: int = field(default=10)
    _charisma: int = field(default=10)
    
    hp: int
    max_hp: int
    ac: int
    
    attacks: List[str] = field(default_factory=list)
    talents: List[str] = field(default_factory=list)
    spells: List[str] = field(default_factory=list)
    gear: List[str] = field(default_factory=list)
    
    gear_slots: int = field(init=False)
    spell_slots: Dict[str, int] = field(default_factory=dict)
    languages: List[str] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)
    class_features: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.gear_slots = max(10, self._strength)

    def random_background() -> SHADOWDARK_BACKGROUND:
        return random.choice(list(SHADOWDARK_BACKGROUND))

    @staticmethod
    def calculate_modifier(stat: int) -> int:
        if stat <= 3:
            return -4
        elif stat <= 5:
            return -3
        elif stat <= 7:
            return -2
        elif stat <= 9:
            return -1
        elif stat <= 11:
            return 0
        elif stat <= 13:
            return 1
        elif stat <= 15:
            return 2
        elif stat <= 17:
            return 3
        else:
            return 4

    # Properties for stats and their modifiers
    @property
    def strength(self) -> Dict[str, int]:
        return {"value": self._strength, "modifier": self.calculate_modifier(self._strength)}

    @property
    def dexterity(self) -> Dict[str, int]:
        return {"value": self._dexterity, "modifier": self.calculate_modifier(self._dexterity)}

    @property
    def constitution(self) -> Dict[str, int]:
        return {"value": self._constitution, "modifier": self.calculate_modifier(self._constitution)}

    @property
    def intelligence(self) -> Dict[str, int]:
        return {"value": self._intelligence, "modifier": self.calculate_modifier(self._intelligence)}

    @property
    def wisdom(self) -> Dict[str, int]:
        return {"value": self._wisdom, "modifier": self.calculate_modifier(self._wisdom)}

    @property
    def charisma(self) -> Dict[str, int]:
        return {"value": self._charisma, "modifier": self.calculate_modifier(self._charisma)}

    # Setters for stats
    @strength.setter
    def strength(self, value: int):
        self._strength = value
        self.gear_slots = max(10, self._strength)

    @dexterity.setter
    def dexterity(self, value: int):
        self._dexterity = value

    @constitution.setter
    def constitution(self, value: int):
        self._constitution = value

    @intelligence.setter
    def intelligence(self, value: int):
        self._intelligence = value

    @wisdom.setter
    def wisdom(self, value: int):
        self._wisdom = value

    @charisma.setter
    def charisma(self, value: int):
        self._charisma = value

    def add_gear(self, item: str):
        if len(self.gear) < self.gear_slots:
            self.gear.append(item)
        else:
            print(f"Cannot add {item}. Gear slots full.")
    
    def level_up(self):
        self.level += 1
        # Here you would implement the logic for leveling up
        # This might include increasing HP, updating title, etc.
        
    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)
        
    def heal(self, amount: int):
        self.hp = min(self.max_hp, self.hp + amount)
        self.apply_ancestry_traits()
        self.apply_class_features()
        
    @property
    def ancestry(self) -> SHADOWDARK_ANCESTRY:
        return self._ancestry

    @ancestry.setter
    def ancestry(self, value: SHADOWDARK_ANCESTRY):
        self._ancestry = value
        self.apply_ancestry_traits()

    def apply_ancestry_traits(self):
        # Reset languages and traits
        self.languages = ["Common"]
        self.traits = []

        if self._ancestry == SHADOWDARK_ANCESTRY.DWARF:
            self.languages.append("Dwarvish")
            self.traits.append("Stout: Start with +2 HP. Roll hit points per level with advantage.")
            self.max_hp += 2
            self.hp += 2

        elif self._ancestry == SHADOWDARK_ANCESTRY.ELF:
            self.languages.extend(["Elvish", "Sylvan"])
            self.traits.append("Farsight: +1 bonus to attack rolls with ranged weapons or +1 bonus to spellcasting checks.")

        elif self._ancestry == SHADOWDARK_ANCESTRY.GOBLIN:
            self.languages.append("Goblin")
            self.traits.append("Keen Senses: You can't be surprised.")

        elif self._ancestry == SHADOWDARK_ANCESTRY.HALF_ORC:
            self.languages.append("Orcish")
            self.traits.append("Mighty: +1 bonus to attack and damage rolls with melee weapons.")

        elif self._ancestry == SHADOWDARK_ANCESTRY.HALFLING:
            self.traits.append("Stealthy: Once per day, you can become invisible for 3 rounds.")

        elif self._ancestry == SHADOWDARK_ANCESTRY.HUMAN:
            self.traits.append("Ambitious: You gain one additional talent roll at 1st level.")
            # For simplicity, we'll add a random language here. In a real game, you'd want the player to choose.
            import random
            additional_languages = ["Dwarvish", "Elvish", "Goblin", "Orcish", "Sylvan"]
            self.languages.append(random.choice(additional_languages))

    # ... (rest of the methods from the previous version)

    def roll_stats(self):
        import random
        stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        for stat in stats:
            setattr(self, f"_{stat}", sum(random.randint(1, 6) for _ in range(3)))
        
        if not any(getattr(self, f"_{stat}") >= 14 for stat in stats):
            print("No stat 14 or higher. Rolling again...")
            self.roll_stats()

    @property
    def character_class(self) -> SHADOWDARK_CLASS:
        return self._character_class

    @character_class.setter
    def character_class(self, value: SHADOWDARK_CLASS):
        self._character_class = value
        self.apply_class_features()

    def apply_class_features(self):
        self.class_features = []
        
        if self._character_class == SHADOWDARK_CLASS.FIGHTER:
            self.class_features.extend([
                "Weapons: All weapons",
                "Armor: All armor and shields",
                "Hit Points: 1d8 per level",
                "Hauler: Add Constitution modifier to gear slots if positive",
                "Weapon Mastery: +1 to attack and damage with chosen weapon type",
                "Grit: Advantage on Strength or Dexterity checks to overcome opposing force"
            ])
            self.gear_slots += max(0, self.constitution['modifier'])

        elif self._character_class == SHADOWDARK_CLASS.PRIEST:
            self.class_features.extend([
                "Weapons: Club, crossbow, dagger, mace, longsword, staff, warhammer",
                "Armor: All armor and shields",
                "Hit Points: 1d6 per level",
                "Languages: You know Celestial, Diabolic, or Primordial",
                "Turn Undead: You know the turn undead spell",
                "Deity: Choose a god to serve",
                "Spellcasting: You can cast priest spells"
            ])
            self.languages.append("Celestial")  # Default, could be chosen

        elif self._character_class == SHADOWDARK_CLASS.THIEF:
            self.class_features.extend([
                "Weapons: Club, crossbow, dagger, shortbow, shortsword",
                "Armor: Leather armor, mithral chainmail",
                "Hit Points: 1d4 per level",
                "Backstab: Extra damage on unaware targets",
                "Thievery: Advantage on thieving skills"
            ])

        elif self._character_class == SHADOWDARK_CLASS.WIZARD:
            self.class_features.extend([
                "Weapons: Dagger, staff",
                "Armor: None",
                "Hit Points: 1d4 per level",
                "Languages: You know two additional common languages and two rare languages",
                "Learning Spells: Can learn spells from scrolls",
                "Spellcasting: You can cast wizard spells"
            ])
            self.languages.extend(["Common", "Common", "Rare", "Rare"])  # Placeholder

        elif self._character_class == SHADOWDARK_CLASS.BARD:
            self.class_features.extend([
                "Weapons: Crossbow, dagger, mace, shortbow, shortsword, spear, staff",
                "Armor: Leather armor, chainmail, shields",
                "Hit Points: 1d6 per level",
                "Languages: You know four additional common languages and one rare language",
                "Bardic Arts: Trained in oration, performing arts, lore, and diplomacy",
                "Magical Dabbler: Can activate spell scrolls and wands using Charisma",
                "Presence: Inspire or Fascinate",
                "Prolific: Add 1d6 to learning rolls"
            ])
            self.languages.extend(["Common", "Common", "Common", "Common", "Rare"])

        elif self._character_class == SHADOWDARK_CLASS.RANGER:
            self.class_features.extend([
                "Weapons: Dagger, longbow, longsword, shortbow, shortsword, spear, staff",
                "Armor: Leather armor, chainmail",
                "Hit Points: 1d8 per level",
                "Wayfinder: Advantage on navigation, tracking, bushcraft, stealth, and wild animals",
                "Herbalism: Can prepare herbal remedies"
            ])

    # ... (other methods remain unchanged)

# Example usage
if __name__ == "__main__":
    character = SHADOWDARK_CHARACTER(
        name="Alric the Bold",
        _ancestry=SHADOWDARK_ANCESTRY.HUMAN,
        _character_class=SHADOWDARK_CLASS.FIGHTER,
        background="Soldier",
        hp=10,
        max_hp=10,
        ac=15
    )
    
    character.roll_stats()
    
    print(f"Character created: {character.name}")
    print(f"Ancestry: {character.ancestry.name}")
    print(f"Class: {character.character_class.name}")
    print(f"HP: {character.hp}/{character.max_hp}")
    print(f"Languages: {', '.join(character.languages)}")
    print(f"Ancestry Traits: {', '.join(character.traits)}")
    print(f"Class Features: {', '.join(character.class_features)}")
    print(f"Gear slots: {character.gear_slots}")
    
    for stat in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
        stat_info = getattr(character, stat)
        print(f"{stat.capitalize()}: {stat_info['value']} (Modifier: {stat_info['modifier']})")
    
    # Changing class to demonstrate the setter
    print("\nChanging class to Bard:")
    character.character_class = SHADOWDARK_CLASS.BARD
    print(f"New Class: {character.character_class.name}")
    print(f"Class Features: {', '.join(character.class_features)}")
    print(f"Languages: {', '.join(character.languages)}")

    for _ in range(5):  # Generate 5 random backgrounds
        background = SHADOWDARK_CHARACTER.random_background()
        print(f"Background: {background.title}")
        print(f"Description: {background.description}")
        print()

    # You can also access a specific background
    specific_background = SHADOWDARK_BACKGROUND.NOBLE
    print(f"Specific Background: {specific_background.title}")
    print(f"Description: {specific_background.description}")