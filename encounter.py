import random,sys,time

typing_speed = 50 #wpm
#Slow Input to be immersive.
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print ('')

def slow_type_EXTRA(t): 
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*7.0/typing_speed)
    print ('')

#Step Counter
player_steps = 0

#Dialogues
dialogue1 = ["I want to escape.", "When will this end?", "I want to give up.", "Please let all end.", "I don't want to continue this anymore",
            "I want to see my family again", "I don't want to die.", "I have a knife and it is not for my enemies."]
dialogue2 = ["Is a grave better than being tortured?", "What time of the day is it?", "I want to sleep.", "My bones are still intact. But my brain is not",
             "Will I ever see the light of day again?", "Maybe an eternal sleep will benefit me more."]
dialogue3 = ["Why did it not attack me?", "I'm a coward...", "Thank you God.", "I survived..?"]

if player_moves:
    player_steps += 1

if player_steps == 5:
    encounter = random.randint(0, 100)
    if encounter <= 50:
        print("An enemy found you.")
        player_steps == 0 #Reset to 0

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Higher enemy encounter
if player_steps == 6:
    encounter = random.randint(0, 80)
    if encounter <= 40:
        print("An enemy has found you.")
        player_steps == 0 #Reset again

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Safe reset.
if player_steps == 7:
    encounter <= random.randint(0, 50)
    if encounter <= random.randint <= 25:
        print("An enemy found you.")
        player_steps == 0 #reset

    else:
        slow_type(random.choice(dialogue2))
        slow_type(random.choice(dialogue3))
        player_steps == 0 #safe reset.