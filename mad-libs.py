def mad_lib():
    # Collecting inputs from the user for the Mad Lib
    nouns = [input(f"Enter a noun ({i+1}/4): ") for i in range(4)]
    adjectives = [input(f"Enter an adjective ({i+1}/4): ") for i in range(4)]
    verbs = [input(f"Enter a verb ({i+1}/4): ") for i in range(4)]
    adverbs = [input(f"Enter an adverb ({i+1}/4): ") for i in range(4)]
    
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
    print(story)

# Run the Mad Lib
mad_lib()