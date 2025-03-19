#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""

# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Supper_Cheater
still_playing = True

def main():
    """run-time code"""
    while still_playing == True:
        # create two cheater objects
        cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
        cheater2 = Supper_Cheater() # increase all rolls by +1 provided they are < 6
        cheat_roll = True
        # both players take turns
        cheater1.roll()
        cheater2.roll()

        # both players use their cheat methods
        cheater1.cheat()
        cheater2.cheat()

        print(f"Cheater 1 rolled {cheater1.get_dice()}")
        print(f"Cheater 2 rolled {cheater2.get_dice()}")

        if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
            print("Draw!")

        elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
            print("Cheater 1 wins!")

        else:
            print("Cheater 2 wins!")
        
        for roll in cheater1.dice:
            print(roll)
            print(cheat_roll)
            input()
            if roll  < 6:
                cheat_roll = False
        if cheat_roll == True:
            print("cheater1 as cheated!")
        cheat_roll  = True
        for roll in cheater2.dice:
            print(roll)
            print(cheat_roll)
            input()
            if roll < 6:
                cheat_roll = False
        if cheat_roll == True:
            print("cheater2 as cheated!")
        if input("would you like to play again(y/n): ") == "n":
            break
if __name__ == "__main__":
    main()
