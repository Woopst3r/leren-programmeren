import random
import time

def name_input():
    name = input("What is your name?: ")
    return name

def welcome_input(name):
    while True:
        user_input = input(f"W̵e̵l̸o̸m̴e̶  {name} t̴o̶ ̴T̶r̷a̴p̵R̷o̵o̷m̸. Type 'Escape' if you wish to continue: ").lower()
        if user_input == "escape":
            return
        else:
            response = input("Are you too scared to play? Type 'yes' to end the game, or 'no' to try again: ").lower()
            if response == "yes":
                print("Game over.")
                return
def play_game():
    print("Masked individual: I respect you for your courage. But you need more than courage to escape this place.\n")
    print("Masked individual: You have 10 fingers, right? Let's play a game. If you win rock-paper-scissors 3 times, you will get the key to the next room. If you lose 3 times, I will take 2 fingers from you.\n")
    options = ["rock", "paper", "scissors"]
    dealer_score = 0
    player_score = 0
    while True:
        if dealer_score == 3:
            print("Dealer wins. You lose three fingers.")
            return False
        if player_score == 3:
            print("You win! Dealer gives you the key.")
            return True
        dealer_choice = random.choice(options)
        player_choice = input("Pick rock, paper, or scissors: ").lower()
        if player_choice == dealer_choice:
            print("Tie.")
        elif player_choice == "rock" and dealer_choice == "paper":
            print("Dealer wins!")
            dealer_score += 1
        elif player_choice == "paper" and dealer_choice == "scissors":
            print("Dealer wins!")
            dealer_score += 1
        elif player_choice == "scissors" and dealer_choice == "rock":
            print("Dealer wins!")
            dealer_score += 1
        else:
            print("You win!")
            player_score += 1
            time.sleep(1)
    return False

def finger_chop(fingers_left):
    fingers_left -= 2
    if fingers_left <= 0:
        print("You have no fingers left. Game over.")
    else:
        print(f"You have {fingers_left} fingers left.")
    return fingers_left
def main():
    name = name_input()
    welcome_input(name)
    fingers_left = 10
    while True:
        win = play_game()
        if not win:
            fingers_left = finger_chop(fingers_left)
            if fingers_left <= 0:
                break
        else:
            print(f"You still have {fingers_left} fingers left.")
            play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if play_again == "no":
                break
            else:
                fingers_left = 10

    print(f"Game over. You have {fingers_left} fingers left.")

if __name__ == "__main__":
    main()