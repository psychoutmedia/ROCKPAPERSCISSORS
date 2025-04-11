from random import choice

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)    ROCK!
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)    PAPER!
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)    SCISSORS!
"""

moves = ["rock", "paper", "scissors"]

# Score tracking
wins = 0
losses = 0
ties = 0

while True:
    player_move = input("Enter your move (rock, paper, or scissors): ").lower()

    if player_move not in moves:
        print("Invalid move! Try again.")
        continue

    # Computer randomly picks a move
    comp_move = choice(moves)

    # Print player's move
    print("YOUR MOVE:")
    if player_move == "rock":
        print(rock)
    elif player_move == "paper":
        print(paper)
    elif player_move == "scissors":
        print(scissors)

    # Print computer's move
    print("COMPUTER MOVE:")
    if comp_move == "rock":
        print(rock)
    elif comp_move == "paper":
        print(paper)
    elif comp_move == "scissors":
        print(scissors)

    # Determine result
    if comp_move == player_move:
        print("IT'S A TIE!")
        ties += 1
    elif (
        (player_move == "rock" and comp_move == "scissors") or
        (player_move == "paper" and comp_move == "rock") or
        (player_move == "scissors" and comp_move == "paper")
    ):
        print("YOU WIN!!!")
        wins += 1
    else:
        print("YOU LOSE!!!")
        losses += 1

    # Show current score
    print(f"\nScore: {wins} Wins | {losses} Losses | {ties} Ties\n")

    # Ask to play again
    play_again = input("Play again? (y or n): ").lower()
    if play_again != "y":
        print("\nThanks for playing!")
        print(f"FINAL SCORE: {wins} Wins | {losses} Losses | {ties} Ties")
        break