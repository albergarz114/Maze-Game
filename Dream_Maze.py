## THE Dream Maze ##
# Current Situation
print("""
Alberto is a regular guy who works as a developer. On his free time he enjoys the outdoors, traveling, playing table tennis, and a foodie.
Unfortunately, it was those days where work got overwhelming for him and his team. Random ideas from work 
kept racing in his mind. Finally, Alberto lied down in bed and fell into a deep sleep. In the dream he was stuck in a 
corn maze. Alberto was panicking because he was stuck in the maze and couldn't get out. He looked at his hands and his 
palms were cold, clammy, and full of sweat. He felt he was going to suffocate, but quickly reminded himself that nervousness
will not get him nowhere. He needed to be brave and learn how to get out of the corn maze. Next to one of the corn fields on the floor
was a paper. He picked up the paper and read it. The paper stated there is a golden key somewhere to escape from the corn maze.
The only advice Alberto got from the paper was to follow his instincts and trust himself. At the end of the instructions 
there was a warning not to eat the red berries growing from some of the bushes. There are poisonous and can either kill you or give you hallucinations.
Alberto was ready and told himself LETS FREAKING DO THIS AND FIND THE GOLDEN KEY!!
""")
# OPTIONS FOR DECISIONS
print("(TAKE LEFT/TAKE RIGHT/TAKE MIDDLE)")
choice = input ("What do you do? ")

if "TAKE LEFT" == choice:
    print("""Unfortunately, he did not find the golden key. Alberto ended up in a dead end with a lot of poisonous berries scattered 
    all over the floor. Now what? 
    """)
    # OPTIONS FOR MORE DECISIONS
    print("(ABORT/SEARCH)")
    choice = input("What does he do now?")
    if "ABORT" == choice:
        print("Alberto gives up, is starving, and decides to eat the berries. Next thing you know he starts seeing colors, vomits, and passes out. Then he wakes up in the middle of the night and yells because he had a horrible dream! ")
    elif "SEARCH" == choice:
        print("He does NOT give up because he is a fighter! He analyzes the situation and executes it. Alberto tells himself I AM HE WHO NEVERS GIVES UP!!!")
    else:
        print("Alberto cheated by taking short cuts in the corn maze. ")
if "TAKE RIGHT" == choice:
    print("Alberto was UPSET AND FRUSTRATED! Puzzled! Puzzled! Puzzled! The golden key was not there. He had to rethink the process and accept his mistakes.")
    # OPTIONS OPTIONS
    print("(TAKE ANOTHER LEFT/TAKE ANOTHER RIGHT/TAKE MIDDLE)")
    choice = input("What is the plan Captain? ")
    if "TAKE ANOTHER LEFT" == choice:
        print("Albert will get more confused and lose his mind. However, he has a lot of options to keep searching for the golden key.")
    elif "TAKE ANOTHER RIGHT" == choice:
        print("He ended up in a loop and is going in circles. No way around it! ")
    else:
        print("He keeps looking for the key, but is exhausted. ")
if "TAKE MIDDLE" == choice:
        print("After walking five blocks Alberto sees some object shining in the far distance. ")
        # OPTIONS 3
        print("(KEEP STRAIGHT/LEFT TURN/DOUBLE RIGHT)")
        choice = input("Where to now? ")
if "KEEP STRAIGHT" == choice:
        print("He FOUND THE GOLDEN KEY!! HOORAY")
elif "LEFT TURN" == choice:
        print("Damn brother....close but no CIGAR ")
elif "DOUBLE RIGHT" == choice:
        print("YOU ARE and WILL BE IN A LIMBO FOREVER MY FRIEND. ")

else:
        print("GAME OVER!!")
    
