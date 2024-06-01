import random

def roll_eatable():
    """
    I Eat the Stuff - Note: Smelling the Stuff Gives a Clue to Its Effect

    This function randomly selects an effect from a list of possible effects
    when eating something. Smelling the item provides a clue to its effect.
    """
    effects = [
        "Delici…argh! str save or your guts explode.", "Delicious! Fruity. Quite satisfying.", 
        "Delicious! Fruity. Quite satisfying.", "Delicious! Fruity. Quite satisfying.", 
        "Tastes meaty. You regain any lost str.", "Tastes meaty. You regain any lost str.", 
        "Tastes meaty. You regain any lost str.", "Your insides feel cold, and liquid metal coats your bones. You always have Armour 1.", 
        "Tastes pickled. You get real drunk.", "Tastes pickled. You get real drunk.", 
        "Tastes pickled. You get real drunk.", "Woah. Hallucinations for d6 hours.", 
        "Woah. Hallucinations for d6 hours.", "Blech! Vomit now and for d6 hours.", 
        "Blech! Vomit now and for d6 hours.", "Tastes inky. You can read books instantly by waving your hand over them.", 
        "Tastes inky. You can read books instantly by waving your hand over them.", 
        "Urgh… so salty. It's gross.", "Urgh… so salty. It's gross.", "Literally liquid gold. Lose d6 str.", 
        "Literally liquid gold. Lose d6 str.", "Literally liquid gold. Lose d6 str.", 
        "Hot! Breathe Fire (d10) at whoever is right infront of you.", "Hot! Breathe Fire (d10) at whoever is right infront of you.", 
        "Hot! Breathe Fire (d10) at whoever is right infront of you.", "Roll a Mutation.", "Roll a Mutation.", 
        "Roll a Mutation.", "Roll a Mutation.", "Turn Invisible for d6 minutes.", 
        "Turn Invisible for d6 minutes.", "Horrible pain for d6 minutes.", "Horrible pain for d6 minutes.", 
        "Bready. You need never eat or drink again.", "Bready. You need never eat or drink again.", 
        "Like liquid fish. Quite stirring.", "Like liquid fish. Quite stirring.", "Blind for d6 hours!", 
        "Blind for d6 hours!", "Awful poison. Lose 2d6 str.", "Awful poison. Lose 2d6 str.", 
        "Lose 2d6 dex. Turn to stone at dex 0.", "Lose 2d6 dex. Turn to stone at dex 0.", 
        "Lose 2d6 wil. Turn into an insane monster at wil 0.", "Lose 2d6 wil. Turn into an insane monster at wil 0.", 
        "It's okay I guess, for slime.", "It's okay I guess, for slime.", 
        "Gain an evil voice in your head forever.", "Gain an evil voice in your head forever.", 
        "Gain a helpful voice in your head forever.", "Gain a helpful voice in your head forever.", 
        "It's the best! You crave more. Lose 1 wil each day until you eat some more.", 
        "It's the best! You crave more. Lose 1 wil each day until you eat some more.", 
        "Invigorating! Gain 1d6 str for d6 hours.", "Invigorating! Gain 1d6 str for d6 hours.", 
        "Invigorating! Gain 1d6 str for d6 hours.", "Mind-Opening. Gain 1d6 wil for d6 hours.", 
        "Mind-Opening. Gain 1d6 wil for d6 hours.", "Zippy! Move at double pace for d6 hours.", 
        "Zippy! Move at double pace for d6 hours.", "Zippy! Move at double pace for d6 hours.", 
        "First taste is gross. Second is delicious.", "First taste is gross. Second is delicious.", 
        "First taste is gross. Second is delicious.", "Your mouth seals shut for d6 hours.", 
        "Your mouth seals shut for d6 hours.", "Your mouth seals shut for d6 hours.", 
        "Go on a rampage for d6 turns.", "Go on a rampage for d6 turns.", "Your voice now echos.", 
        "Your voice now echos.", "Your voice is permanently higher pitched.", 
        "Your voice is permanently higher pitched.", "Rapid hair growth, permanently.", 
        "Rapid hair growth, permanently.", "Like Honey! Heals any ailment."
    ]
    return random.choice(effects)

# Example usage
print("Eatable Effect:", roll_eatable())
