from base_tables.military_unit import *
from base_tables.nation import *

def generate_military_unit():
    unit = {
        "Unit Type": roll_unit_type(),
        "Main Ability": roll_main_ability(),
        "Psychological Trait": roll_psychological_trait(),
        "Secondary Ability": roll_secondary_ability(),
        "Narrative Purpose": roll_narrative_purpose()
    }
    return unit

def display_military_unit(unit):
    print("Specialized Military Unit:")
    print("==========================")
    for key, value in unit.items():
        print(f"{key}: {value}")
    print("\nUnit Description:")
    print("=================")
    print(f"The {unit['Unit Type'].split('(')[0].strip()} are a specialized military unit known for their {unit['Main Ability'].split('(')[0].strip()}.")
    print(f"In battle, they exhibit {unit['Psychological Trait'].split('(')[0].strip()}, making them formidable opponents.")
    print(f"They also possess the ability of {unit['Secondary Ability'].split('(')[0].strip()}, adding to their combat effectiveness.")
    print(f"\nBeyond their military role, they serve as {unit['Narrative Purpose'].split(':')[0]}.")
    print(f"{unit['Narrative Purpose'].split(':')[1].strip()}")
    print("\nThis dual nature as both a military force and {0} makes them a unique and valuable asset to their society.".format(unit['Narrative Purpose'].split(':')[0].lower()))



def generate_culture():
    culture = {
        "Military Paradigm": roll(military_paradigms),
        "Historical Events": [roll(historical_events), roll(historical_events)],
        "Cultural Evolution": roll(cultural_evolutions),
        "Government": roll(governments),
        "Economy": roll(economies),
        "Religion/Philosophy": roll(religions),
        "Social Norms": roll(social_norms),
        "Aesthetics": roll(aesthetics),
        "Unique Cultural Elements": [roll(unique_elements), roll(unique_elements)],
        "Potential Plot Hook": roll(plot_hooks)
    }
    return culture

def print_culture(culture):
    print("Generated Culture Profile:")
    print("==========================")
    for key, value in culture.items():
        print(f"\n{key}:")
        if isinstance(value, list):
            for item in value:
                print(f"- {item}")
        else:
            print(f"- {value}")

# Example usage
if __name__ == "__main__":
    generated_culture = generate_culture()
    print_culture(generated_culture)

if __name__ == "__main__":
    unit = generate_military_unit()
    display_military_unit(unit)
