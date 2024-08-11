from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class SHADOWDARK_ARMOR(Enum):
    LEATHER_ARMOR = auto()
    CHAINMAIL = auto()
    PLATE_MAIL = auto()
    SHIELD = auto()
    MITHRAL = auto()

@dataclass
class ArmorEntry:
    name: str
    cost: str
    gear_slots: int
    ac: str
    properties: List[str]

def shadowdark_armor(armor: SHADOWDARK_ARMOR, apply_mithral: bool = False) -> ArmorEntry:
    armors = {
        SHADOWDARK_ARMOR.LEATHER_ARMOR: ArmorEntry("Leather armor", "10 gp", 1, "11 + DEX mod", []),
        SHADOWDARK_ARMOR.CHAINMAIL: ArmorEntry("Chainmail", "60 gp", 2, "13 + DEX mod", ["Disadv on stealth", "swim"]),
        SHADOWDARK_ARMOR.PLATE_MAIL: ArmorEntry("Plate mail", "130 gp", 3, "15", ["No swim", "disadv stealth"]),
        SHADOWDARK_ARMOR.SHIELD: ArmorEntry("Shield", "10 gp", 1, "+2", ["Occupies one hand"]),
        SHADOWDARK_ARMOR.MITHRAL: ArmorEntry("Mithral", "x4", -1, "-", ["No penalty stealth", "swim"])
    }
    if apply_mithral:
        return apply_mithral(armors[armor])
    return armors[armor]

def apply_mithral(armor: ArmorEntry) -> ArmorEntry:
    if armor.name in ["Chainmail", "Plate mail"]:
        mithral = shadowdark_armor(SHADOWDARK_ARMOR.MITHRAL)
        new_cost = f"{mithral.cost} base cost"
        new_gear_slots = max(1, armor.gear_slots + mithral.gear_slots)
        new_properties = [prop for prop in armor.properties if prop not in mithral.properties] + mithral.properties
        return ArmorEntry(
            f"Mithral {armor.name}",
            new_cost,
            new_gear_slots,
            armor.ac,
            new_properties
        )
    else:
        return armor  # Return the original armor if it's not metal armor

# Example usage
if __name__ == "__main__":
    chainmail = shadowdark_armor(SHADOWDARK_ARMOR.CHAINMAIL)
    print("Regular Chainmail:")
    print(f"Name: {chainmail.name}")
    print(f"Cost: {chainmail.cost}")
    print(f"Gear Slots: {chainmail.gear_slots}")
    print(f"AC: {chainmail.ac}")
    print(f"Properties: {', '.join(chainmail.properties)}")

    print("\nMithral Chainmail:")
    mithral_chainmail = apply_mithral(chainmail)
    print(f"Name: {mithral_chainmail.name}")
    print(f"Cost: {mithral_chainmail.cost}")
    print(f"Gear Slots: {mithral_chainmail.gear_slots}")
    print(f"AC: {mithral_chainmail.ac}")
    print(f"Properties: {', '.join(mithral_chainmail.properties)}")