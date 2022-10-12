#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 11, 2022
# programs that lets you guess the randomly generated number


import random


def main():
    # variables
    user_num = int(input("Guess a number between 0 and 9: "))
    rand_num = random.randint(0, 9)

    # checks if user's number is the same as the random number
    if user_num == rand_num:
        print("You guessed the right number!")
    else:
        print(f"You guessed the wrong number. The right number was {rand_num}")


if __name__ == "__main__":
    main()
