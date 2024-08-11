from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class SHADOWDARK_CHARACTER:
    name: str
    ancestry: str
    character_class: str
    level: int = 0
    xp: int = 0
    alignment: str = "Neutral"
    deity: Optional[str] = None
    title: str = "Novice"
    background: str
    
    # Raw stat values
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

    def __post_init__(self):
        self.gear_slots = max(10, self._strength)

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

    def roll_stats(self):
        import random
        stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        for stat in stats:
            setattr(self, f"_{stat}", sum(random.randint(1, 6) for _ in range(3)))
        
        # Check if any stat is 14 or higher
        if not any(getattr(self, f"_{stat}") >= 14 for stat in stats):
            print("No stat 14 or higher. Rolling again...")
            self.roll_stats()

# Example usage
if __name__ == "__main__":
    character = SHADOWDARK_CHARACTER(
        name="Alric the Bold",
        ancestry="Human",
        character_class="Fighter",
        background="Soldier",
        hp=10,
        max_hp=10,
        ac=15
    )
    
    character.roll_stats()
    
    print(f"Character created: {character.name}")
    print(f"Class: {character.character_class}")
    print(f"HP: {character.hp}/{character.max_hp}")
    print(f"Gear slots: {character.gear_slots}")
    
    for stat in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
        stat_info = getattr(character, stat)
        print(f"{stat.capitalize()}: {stat_info['value']} (Modifier: {stat_info['modifier']})")
    
    character.add_gear("Longsword")
    character.add_gear("Shield")
    print(f"Gear: {', '.join(character.gear)}")