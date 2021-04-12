import time
import random


# created a global list variable, so that it can be assessed..
# inside or outside the function
weapon = []


def print_and_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

# introduces the game


def introduction(monster, weapon):
    print_and_pause("You find yourself standing in an open field,"
                    "filled with grass and yellow wildflowers.")
    print_and_pause("Rumor has it that a " + monster +
                    " is somewhere around here,"
                    "and has been terrifying the nearby village.")
    print_and_pause("In front of you is a house.")
    print_and_pause("To your right is a dark cave.")
    print_and_pause("In your hand you hold your a"
                    "trusty (but not very effective) dagger.\n")

# combact that leads to lose against the enemy


def the_lost_fight_scenario(monster, weapon):
    print_and_pause("Seems the " + monster + " has been waiting for you,"
                    "the " + monster + " charges at you"
                    "with a shocking speed.")
    print_and_pause("You fall on your face into the dirt, gasping for air.")
    print_and_pause("You are done.")

# combact that leads to victory against the enemy


def the_victories_fight_scenario(monster, weapon):
    print_and_pause("You are face to face with the " + monster + ".")
    print_and_pause("The " + monster + " tries to hit you in the face,"
                    "but you were lucky to dodge the attack."
                    "You started running from the " + monster + ".")
    print_and_pause("The " + monster + " starts chasing you,"
                    "giving you no time to set yourself up for a reprisal.")
    print_and_pause("You missed your footing and fell to the ground,"
                    "and the sword fell off your hand.")
    print_and_pause("The " + monster + " starts walking slowly towards you,"
                    "as you crawl on your knees"
                    "trying to reach for the sword.")
    print_and_pause("The " + monster + " attacks you again,"
                    "you block the attack with the ancient"
                    "Greek shield you took from the cave.")
    print_and_pause("You finally get hold of the sword.")

# function that ensures that the game accepts no invalid input


def repeat_fight_or_run_question(monster):
    fight_or_run_away(monster, weapon)

# fight or run away function


def fight_or_run_away(monster, weapon):
    fight_run = input("Would you like to (1) fight or (2) run away?")
    if fight_run == '1' and "sword" not in weapon:
        print_and_pause("You do your best...")
        print_and_pause("but your dagger is no match for the " + monster + ".")
        the_lost_fight_scenario(monster, weapon)
        print_and_pause("You have been defeated!")
        print_and_pause("YOU HAVE LOST THE GAME!")
        print_and_pause("GAME OVER")
        play_game_again()
    elif fight_run == "1" and "sword" in weapon:
        print_and_pause("As the troll moves to attack you,"
                        "you unsheath your new sword.")
        print_and_pause("The sword of Ogoroth shines brightly in your hand"
                        "as you brace yourself for the attack")
        the_victories_fight_scenario(monster, weapon)
        print_and_pause("The " + monster + " takes one look at"
                        "your new toy and runs away!")
        print_and_pause("You have rid the town of the " + monster + ","
                        "you are victorious!")
        print_and_pause("YOU HAVE WON THE GAME!")
        play_game_again()
    elif fight_run == '2':
        print_and_pause("You run back to the field."
                        " Luckily, you don't seem to have been followed.\n")
        entering_the_door()
        making_a_decision(monster, weapon)
    else:
        repeat_fight_or_run_question(monster)


def knock_on_the_door(monster, weapon):
    print_and_pause("You approach the door of the house.")
    print_and_pause("You are about to knock when the door"
                    "opens and out steps a " + monster + ".")
    print_and_pause("Eep! This is the " + monster + "'s house!")
    print_and_pause("The " + monster + " attacks you!")
    if "sword" not in weapon:
        print_and_pause("You feel a bit under-prepared for this,"
                        "what will only having a tiny dagger.")
    fight_or_run_away(monster, weapon)


def peering_into_the_cave(monster, weapon):
    if "sword" not in weapon:
        weapon.append("sword")
        print_and_pause("You peer cautiously into the cave.")
        print_and_pause("It turns out to be only a very small cave.")
        print_and_pause("Your eye catches a glint of metal behind a rock.")
        print_and_pause("You have found the magical Sword of Ogoroth!")
        print_and_pause("You discard your silly old dagger"
                        "and take the sword with you.")
        print_and_pause("You also found an ancient greek shield in the cave."
                        "You carried it with you.")
        print_and_pause("You walk back out to the field.\n")
        entering_the_door()
        making_a_decision(monster, weapon)
    else:
        print_and_pause("You peer cautiously into the cave.")
        print_and_pause("You've been here before,"
                        "and gotten all the good stuff")
        print_and_pause("You walk back to the field.")
        entering_the_door()
        making_a_decision(monster, weapon)


def repeating_play_game_again():
    play_game_again()

# starts the game again


def play_game_again():
    play_game_again_question = input("Would you like to play again? (y/n)")
    if play_game_again_question == 'n':
        print_and_pause("Thanks for playing! See you next time.")
    elif play_game_again_question == 'y':
        print_and_pause("Excellent! Restarting the game ...")
        start_the_game()
    else:
        repeating_play_game_again()


def entering_the_door():
    print_and_pause("Enter 1 to knock on the door of the house.")
    print_and_pause("Enter 2 to peer into the cave.")
    print_and_pause("What would you like to do?")


def choose_between_1_and_2(decision, monster, weapon):
    making_a_decision(monster, weapon)


def making_a_decision(monster, weapon):
    decision = input("(Please enter 1 or 2.)\n")
    if decision == '1':
        knock_on_the_door(monster, weapon)
    elif decision == '2':
        peering_into_the_cave(monster, weapon)
    else:
        choose_between_1_and_2(decision, monster, weapon)


def start_the_game():
    # selects a random monster every time the game starts
    monster = random.choice(['Beast', 'Vampire', 'Goblin', 'Dragon', 'Bugbear',
                            'White walker', 'Giant Skull'])
    introduction(monster, weapon)
    entering_the_door()
    making_a_decision(monster, weapon)


start_the_game()
