import random
import art

def main():
# print the welcome banner with the game modes for selection
    while True:
        print(art.text2art("GUESSING CHALLENGE!"))
        mode = get_mode()
        if mode == 1:
            Solo(mode)
        elif mode == 2:
            Vs(mode)
        else:
            continue
    # options for players whether to continue playing or exit when the game is finished
        confirmation = input("Continue playing y/n?").upper()
        if confirmation in ["N", "NO"]:
            break

def get_mode():
    # get the game mode for player to select
    try:
        t = int(input("Guess the correct answer from 1 to 20 \nPlease select your mode\n 1-for Solo\n 2-for Versus\nSelect: "))
        # make sure theres only two available options
        if not t in [1,2]:
            raise Exception()
    except (ValueError, Exception):
        print("Only two modes available, please reselect")
    else:
        return t

# mode for player versus computer
def Solo(mode):
#layout the rules
    round_num = 0
    player = ["Player", "Computer"]
    attemps = 0
    ran_num = random.randint(1, 20)

#create the loop for player and computer to take turns to guess the number
    while True:
        round_num += 1
        if round_num % 2:
            try:
                print(f"It's {player[0]}'s turn!")
                attemps = int(input("Guess a number: "))
            # give the hints whether the guessed number is close or not
                if attemps < ran_num:
                    print("Sorry, too low!")
                elif attemps > ran_num:
                    print("Sorry, too high!")
                else:
                # if the player guess the correct number, print out the winner
                    print(f"Awesome! You guessed the number correctly! Winner!")
                    break
            # make sure its a number
            except ValueError:
                print("Must be a number")
        else:
            try:
                attemps = random.randint(1,20)
                print(f"It's {player[1]}'s turn! Is {attemps} correct?")
            #give hints to computer to get the answer even it is random
                if attemps < ran_num:
                    print(f"Sorry, {attemps} is too low!")
                    attemps += 1
                elif attemps > ran_num:
                    print(f"Sorry, {attemps} is too high!")
                    attemps -= 1
                else:
                    # if the computer guess the correct answer, declare winner
                    print(f"Computer guessed the correct number and won this round! Goodluck next time")
                    break
            except ValueError:
                print("Must be a number")

# mode for player versus player
def Vs(mode):
    round_num = 0
    player = ["Player 1", "Player 2"]
    attemps = 0
    ran_num = random.randint(1, 20)

    # same with solo, but each player take turn to guess the number
    # and whoever guess the correct number will be declared winner
    # also, only numbers are allowed
    while True:
        round_num += 1
        if round_num % 2:
            try:
                print(f"It's {player[0]}'s turn!")
                attemps = int(input("Guess a number: "))
                if attemps < ran_num:
                    print("Sorry, too low!")
                elif attemps > ran_num:
                    print("Sorry, too high!")
                else:
                    print(f"Awesome! Player 1 guessed the number correctly! Congrat!")
                    break
            except ValueError:
                print("Must be a number")
        else:
            try:
                print(f"It's {player[1]}'s turn!")
                attemps = int(input("Guess a number: "))
                if attemps < ran_num:
                    print("Sorry, too low!")
                elif attemps > ran_num:
                    print("Sorry, too high!")
                else:
                    print(f"Awesome! Player 2 guessed the number correctly! Congrat!")
                    break
            except ValueError:
                print("Must be a number")

if __name__ == "__main__":
    main()