from dataclasses import dataclass

@dataclass
class Creature():
    category: str
    specifics: str
    details: str

    def __init__(self, category, specifics, details):
        self.category = category
        self.specifics = specifics
        self.details = details

    def __str__(self):
        return f"""
Creature Category: {self.category}
Creature Specific: {self.specifics}
Additional Details: {self.category}
"""
