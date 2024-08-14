from almanac.perilous_wilds.base_tables import roll_unnatural_entity, generate_creature, roll_hazard, generate_place_tags, generate_steading, generate_place_name, generate_region_name

from almanac.shadowdark.base_tables.character import SHADOWDARK_ANCESTRY, SHADOWDARK_CHARACTER, SHADOWDARK_CLASS

# Example usage
# print(f"Region - {generate_region_name()}")
# print(generate_place_tags())

# print(f"Area - {generate_place_name()}")
# print(generate_place_tags())
# print(generate_steading())
# print(generate_steading())
# print(generate_steading())

# print(f"Area - {generate_place_name()}")
# print(generate_place_tags())
# print(generate_steading())
# print(generate_steading())
# print(generate_steading())

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
    character.apply_ancestry_traits()
    character.apply_class_features()
    
    print(f"Character created: {character.name}")
    print(f"Ancestry: {character.ancestry.name}")
    print(f"Class: {character.character_class.name}")
    print(f"HP: {character.hp}/{character.max_hp}")
    print(f"Languages: {', '.join(character.languages)}")
    print(f"Ancestry Traits: {', '.join(character.traits)}")
    print(f"Class Features: {', '.join(character.class_features)}")
    print(f"Gear slots: {character.gear_slots}")