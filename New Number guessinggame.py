import random
from art import pattern
attempts=0
is_running=True
number_of_attempts=0
def play_game():
    global number_of_attempts
    
    computer_number=random.randint(1,100)
    def generate_attempts(user):
        if user=="easy".lower():
           return attempts +10
        elif user=="hard".lower():
           return attempts +5

    def check_guess(guess):
        global number_of_attempts
        number_of_attempts-=1
        if guess==computer_number:
            return"You guess right,kudos!💖😊"
        elif guess > computer_number:
            return"Too high 🤦‍♂️."
        elif guess<computer_number:
            return "Too Low 🤦‍♂️"
    while is_running:
        print(pattern)
        print("Welcome to the number guessing game!".title())
        print("I am thinking of a number between 1 and 100")
        difficulty=input("Choose a difficulty. Type 'easy' or 'hard' ")
        number_of_attempts=generate_attempts(difficulty)
        
        print(f"You have {number_of_attempts} attempts to guess the number")
        guess=int(input("Make a Guess > "))
        print(check_guess(guess))
        print(f"You have {number_of_attempts} attempts left")
        while number_of_attempts>0:
            guess=int(input("Guess again > "))
            result=check_guess(guess)
            print(result)
            if result=="You guess right,kudos!💖😊":
                break
            print(f"You have {number_of_attempts} attempts left")
        else:
            print("You have used all the attempts 😜,Try again")
            print(f"The correct number is {computer_number}")

        replay=input("Do you wish to play the game?(y or n) ").lower()
        if replay !="y":
           break
        
play_game()


    
    
    
    