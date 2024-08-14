from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict

class SteadingSize(Enum):
    Village = 1
    Town = 2
    Keep = 3
    City = 4

class Prosperity(Enum):
    Dirt = 1
    Poor = 2
    Moderate = 3
    Wealthy = 4
    Rich = 5

class Population(Enum):
    Exodus = 1
    Shrinking = 2
    Steady = 3
    Growing = 4
    Booming = 5

class Defenses(Enum):
    Defenseless = 1
    Militia = 2
    Watch = 3
    Guard = 4
    Garrison = 5
    Battalion = 6
    Legion = 7

@dataclass
class Steading:
    name: str
    location: str
    size: SteadingSize
    prosperity: Prosperity
    population: Population
    defenses: Defenses
    tags: List[str] = field(default_factory=list)
    relations: Dict[str, List[str]] = field(default_factory=dict)
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def set_relation(self, relation_type: str, steadings: List[str]):
        self.relations[relation_type] = steadings

    def __str__(self):
        return f"""**Steading - {self.name}** - {self.size.name} ({self.size.value})
*{self.prosperity.name} ({self.prosperity.value})*, *{self.population.name} ({self.population.value})*, *{self.defenses.name} ({self.defenses.value})*, {", ".join([f"*{t}*" for t in self.tags])}, {(", ".join(f"*{k}({', '.join([r for r in v])})*" for k, v in self.relations.items()))
}
"""
