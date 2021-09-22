"""Roll the dice...How many times can you guess correctly?!"""

__author__ = "730225468"

player: str
points: int = 1
DICE = "\U0001F3B2"
HEART = "\U0001F49A"


def main() -> None:
    """The entrypoint to the program."""
    greet()
    global points
    game: int = int(input("Do you want to play the game? Enter 1 for YES or 2 for NO: "))
    while game == 1:
        option1: int = int(input("Do you want to guess if the dice will land on an even or odd number? Enter 1 for YES or 2 for NO: "))
        game = game - 1
        if option1 == 1:
            points = points + 1
            print(even_odd(1))
        else:
            option2: int = int(input("Do you want to guess the exact number the dice will land on? Enter 1 for YES or 2 for NO: "))
            if option2 == 1:
                points = points + 1
                print(guess_the_number(1))
            else:
                option3: int = int(input("Do you want to end the game? Enter 1 for YES or 2 for NO: "))
                if option3 == 1:
                    print("Thank you for playing! You have earned 1 adventure point. Goodbye.")
                else: 
                    print(even_odd(1))
    return None


def greet() -> None:
    """The introduction to the game."""
    global player
    print("Welcome to 'Roll the Dice!' This will be a game to test your guessing skills using a dice!" + DICE)
    player = input("Enter your name: ")
    return None


def even_odd(number: int) -> int:
    """Guess if the number will be even or odd when the dice is rolled. You will earn 1 point for each correct guess."""
    global player
    global points
    guess: int = int(input("Do you think the number will be even or odd? Enter 1 for EVEN or 2 for ODD: "))
    number = 2
    if number == guess:
        print("Nice guess " + player + "! The dice landed on an odd number!")
        points = points + 1   
    else: 
        print("Nice try " + player + ", but the dice landed on an odd number.")
    print("Thanks for guessing! Here is your total number of adventure points: ")
    return (points)


def guess_the_number(points: int) -> int:
    """Guess the correct number that the dice lands on to earn points. You will earn 2 points for each correct guess."""
    global player
    points = points 
    x: int = int(input("Give me a number 1 through 6 that you think the dice will land on: "))
    from random import randint
    y = randint(1, 6)
    if x == y:
        print("Nice roll " + player + "!" "The dice landed on... " + str(y))
        print("Congrats " + player + "!! You guessed correctly and have earned 2 points.")
        points = points + 2
    else:
        print("Sorry, you guessed incorrectly. You have earned 0 points.")
        points = points
    print("Thanks for guessing! Here is your total number of adventure points: ")
    return (points)


if __name__ == "__main__":
    main()
print(f"Thank you for playing!{DICE}{HEART} You ended with " + str(points) + " point(s)!")