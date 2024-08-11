from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Union

class SHADOWDARK_WEAPON(Enum):
    BASTARD_SWORD = auto()
    CLUB = auto()
    CROSSBOW = auto()
    DAGGER = auto()
    GREATAXE = auto()
    GREATSWORD = auto()
    JAVELIN = auto()
    LONGBOW = auto()
    LONGSWORD = auto()
    MACE = auto()
    SHORTBOW = auto()
    SHORTSWORD = auto()
    SPEAR = auto()
    STAFF = auto()
    WARHAMMER = auto()

@dataclass
class WeaponEntry:
    name: str
    cost: str
    type: str
    range: str
    damage: str
    properties: List[str]

def shadowdark_weapon(weapon: SHADOWDARK_WEAPON) -> WeaponEntry:
    weapons = {
        SHADOWDARK_WEAPON.BASTARD_SWORD: WeaponEntry("Bastard sword", "10 gp", "M", "C", "1d8/1d10", ["V", "2 slots"]),
        SHADOWDARK_WEAPON.CLUB: WeaponEntry("Club", "5 cp", "M", "C", "1d4", []),
        SHADOWDARK_WEAPON.CROSSBOW: WeaponEntry("Crossbow", "8 gp", "R", "F", "1d6", ["2H", "L"]),
        SHADOWDARK_WEAPON.DAGGER: WeaponEntry("Dagger", "1 gp", "M/R", "C/N", "1d4", ["F", "Th"]),
        SHADOWDARK_WEAPON.GREATAXE: WeaponEntry("Greataxe", "10 gp", "M", "C", "1d8/1d10", ["V", "2 slots"]),
        SHADOWDARK_WEAPON.GREATSWORD: WeaponEntry("Greatsword", "12 gp", "M", "C", "1d12", ["2H", "2 slots"]),
        SHADOWDARK_WEAPON.JAVELIN: WeaponEntry("Javelin", "5 sp", "M/R", "C/F", "1d4", ["Th"]),
        SHADOWDARK_WEAPON.LONGBOW: WeaponEntry("Longbow", "8 gp", "R", "F", "1d8", ["2H"]),
        SHADOWDARK_WEAPON.LONGSWORD: WeaponEntry("Longsword", "9 gp", "M", "C", "1d8", []),
        SHADOWDARK_WEAPON.MACE: WeaponEntry("Mace", "5 gp", "M", "C", "1d6", []),
        SHADOWDARK_WEAPON.SHORTBOW: WeaponEntry("Shortbow", "6 gp", "R", "F", "1d4", ["2H"]),
        SHADOWDARK_WEAPON.SHORTSWORD: WeaponEntry("Shortsword", "7 gp", "M", "C", "1d6", []),
        SHADOWDARK_WEAPON.SPEAR: WeaponEntry("Spear", "5 sp", "M/R", "C/N", "1d6", ["Th"]),
        SHADOWDARK_WEAPON.STAFF: WeaponEntry("Staff", "5 sp", "M", "C", "1d4", ["2H"]),
        SHADOWDARK_WEAPON.WARHAMMER: WeaponEntry("Warhammer", "10 gp", "M", "C", "1d10", ["2H"]),
    }
    return weapons[weapon]

# Example usage
# if __name__ == "__main__":
#     longsword = shadowdark_weapon(SHADOWDARK_WEAPON.LONGSWORD)
#     print(f"Weapon: {longsword.name}")
#     print(f"Cost: {longsword.cost}")
#     print(f"Type: {longsword.type}")
#     print(f"Range: {longsword.range}")
#     print(f"Damage: {longsword.damage}")
#     print(f"Properties: {', '.join(longsword.properties) if longsword.properties else 'None'}")