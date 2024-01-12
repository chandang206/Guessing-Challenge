
![Logo](https://cdn.firstcry.com/education/2023/02/10130836/Cardinal-Numbers-For-Children-To-Improve-Their-Math-Skills.jpg)


## Demo

Video demo: https://youtu.be/bA8v08v5AIU

# Guessing Challenge

A simple guessing-number challenge with **two game modes** to play either with a computer or versus between actual players.

Files in the project includes:

   - _project.py_
   - _test_project.py_
   - _README.md_
## Libraries

**RANDOM:** to create the random numbers from 1 to 20 for players and computer to guess the correct one. It also was used to make computer generate(guess) the number systematically.

**ART:** to create the welcome banner and make it more interesting.
## Usage

To deploy this project run `python3 project.py`

```python
 ____  _   _  _____  ____   ____   ___  _   _   ____    ____  _   _     _     _      _      _____  _   _   ____  _____  _
 / ___|| | | || ____|/ ___| / ___| |_ _|| \ | | / ___|  / ___|| | | |   / \   | |    | |    | ____|| \ | | / ___|| ____|| |
| |  _ | | | ||  _|  \___ \ \___ \  | | |  \| || |  _  | |    | |_| |  / _ \  | |    | |    |  _|  |  \| || |  _ |  _|  | |
| |_| || |_| || |___  ___) | ___) | | | | |\  || |_| | | |___ |  _  | / ___ \ | |___ | |___ | |___ | |\  || |_| || |___ |_|
 \____| \___/ |_____||____/ |____/ |___||_| \_| \____|  \____||_| |_|/_/   \_\|_____||_____||_____||_| \_| \____||_____|(_)


Guess the correct answer from 1 to 20
Please select your mode
 1-for Solo
 2-for Versus
Select:
```

If select **1**, the game mode will be **player versus computer**:
```python
Select: 1
It's Player turn!
Guess a number: 5
Sorry, too high!
It's Computer turn! Is 6 correct?
Sorry, 6 is too high!
It's Player turn!
Guess a number: 4
Awesome! You guessed the number correctly! Winner!
```
Player will take turns with the computer and guess the number until one get the correct answer. Both get _hints_ after guessing

If select **2**, the game mode will be **player versus player**:
```python
Select: 2
It's Player 1 turn!
Guess a number: 5
Sorry, too low!
It's Player 2 turn!
Guess a number: 7
Awesome! Player 2 guessed the number correctly! Congrat!

```
Player will take turns with each other and guess the number until one get the correct answer. Both get _hints_ after guessing

```python
Continue playing y/n?
```
The game will ask whether player wants to continue playing or not. If they continue, the wellcome banner will re-appear and ask for game mode again, otherwise, the progam will exit.






## Functions
There are 3 basics functions implemented:

- **get_mode()**:
```python
    try:
        t = int(input("Guess the correct answer from 1 to 20 \nPlease select your mode\n 1-for Solo\n 2-for Versus\nSelect: "))
        if not t in [1,2]:
            raise Exception()
    except (ValueError, Exception):
        print("Only two modes available, please reselect")
    else:
        return t
```
The idea is to print the welcome banner with the game modes for selection with options for players whether to continue playing or exit when the game is finished. Also, make sure the program only accept *two values* or it will repromt users.

- **Solo()**:
```python
round_num = 0
    player = ["Player", "Computer"]
    attemps = 0
    ran_num = random.randint(1, 20)

while True:
        round_num += 1
        if round_num % 2:
            try:
                print(f"It's {player[0]} turn!")
                attemps = int(input("Guess a number: "))
                if attemps < ran_num:
                    print("Sorry, too low!")
                elif attemps > ran_num:
                    print("Sorry, too high!")
                else:
                    print(f"Awesome! You guessed the number correctly! Winner!")
                    break
            except ValueError:
                print("Must be a number")
        else:
            try:
                attemps = random.randint(1,20)
                print(f"It's {player[1]} turn! Is {attemps} correct?")
                if attemps < ran_num:
                    print(f"Sorry, {attemps} is too low!")
                    attemps += 1
                elif attemps > ran_num:
                    print(f"Sorry, {attemps} is too high!")
                    attemps -= 1
                else:
                    print(f"Computer guessed the correct number and won this round! Goodluck next time")
                    break
            except ValueError:
                print("Must be a number")
```
Player and computer will take turns to guess the number. Although each computer's "guess" is random, but the program has to make sure computer learn (like if it guess too low or high, the next guess must be higher or number to get the correct answer). The idea is to make it more "competitve" and interesting

- **Vs()**
```python
round_num = 0
    player = ["Player 1", "Player 2"]
    attemps = 0
    ran_num = random.randint(1, 20)

    while True:
        round_num += 1
        if round_num % 2:
            try:
                print(f"It's {player[0]} turn!")
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
                print(f"It's {player[1]} turn!")
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
```
Basically same with Solo but customised for both actual players to take turn and guess the correct answer.
## Authors

- [Chan, Dang Tran Bao](https://github.com/chandang206)