def mad_lib():
    nouns = []
    adjectives = []
    verbs = []
    adverbs = []
    
    print("Let's create a Mad Lib! Follow the prompts below.")
    
    # Collect nouns with conditions
    for i in range(4):
        noun = input(f"Enter a noun ({i+1}/4): ")
        if noun.endswith("s") and i == 0:  # Require plural noun for the first
            print("Nice! A plural noun to start.")
        elif not noun:
            noun = "default_noun"  # Default if empty
            print("No input detected, using default noun.")
        nouns.append(noun)
    
    # Collect adjectives with conditions
    for i in range(4):
        adjective = input(f"Enter an adjective ({i+1}/4): ")
        if "dark" in adjective.lower() and i == 0:
            print("Spooky choice!")
        elif not adjective:
            adjective = "mysterious"  # Default if empty
            print("No input detected, using 'mysterious'.")
        adjectives.append(adjective)
    
    # Collect verbs with conditions
    for i in range(4):
        verb = input(f"Enter a verb ({i+1}/4): ")
        if verb.lower() == "hack" and i == 0:
            print("Perfect choice for a tech heist!")
        elif not verb:
            verb = "run"  # Default if empty
            print("No input detected, using 'run'.")
        verbs.append(verb)
    
    # Collect adverbs with conditions
    for i in range(4):
        adverb = input(f"Enter an adverb ({i+1}/4): ")
        if "ly" not in adverb:
            print("Hint: Adverbs often end in 'ly'.")
            adverb += "ly"  # Add "ly" suffix for fun
        elif not adverb:
            adverb = "stealthily"  # Default if empty
            print("No input detected, using 'stealthily'.")
        adverbs.append(adverb)
    
    # The mad lib story with placeholders for inputs
    story = f"""
    In the middle of a {adjectives[0]} night, a team of {nouns[0]} hackers gathered in their secret {nouns[1]}, ready to execute the most {adjectives[1]} heist in tech history. 
    Their mission: to steal the {adjectives[2]} source code of the world's most secure {nouns[2]}.

    As the lead hacker typed {adverbs[0]} on their mechanical {nouns[3]}, the screen flickered and the {adjectives[3]} firewall appeared. 
    "We've hit the first {nouns[1]}," said the rookie, sweating {adverbs[1]}.

    "Relax," the leader replied, grinning {adverbs[2]}. "It's just a simple buffer overflow exploit. I’ll handle it." With a few {verbs[0]}, the firewall was bypassed.

    They were in. Rows of {nouns[0]} danced across the screen as they {verbs[1]} deeper into the system. 
    "We’ve got {nouns[2]} access!" one of the team members shouted {adverbs[3]}.

    "Perfect," the leader said. "Now let's {verbs[2]} this baby and vanish like a {adjectives[3]} ninja."

    With a final {verbs[3]}, the {nouns[3]} was theirs. They closed their laptops and disappeared {adverbs[2]} into the digital ether, leaving only a trail of {adjectives[1]} memes behind.
    """

    # Printing the mad lib story
    print(story)

# Run the Mad Lib
mad_lib()
