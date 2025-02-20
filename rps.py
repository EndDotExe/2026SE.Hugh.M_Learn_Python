import random

username = input("Name? ")


rps = input("Rock Paper Scissors? ")
print("Shoot!")

rps = rps.lower()


result = random.randint(1, 3)
match result:
    case 1:
        print("Rock!")
    case 2:
        print("Paper!")
    case 3:
        print("Scissors!")


if result == 1 and rps == "scissors":
    print("Game Wins!")
elif result == 2 and rps == "scissors":
    print(f"{username} Wins!")
elif result == 3 and rps == "scissors":
    print("Tie!")
elif result == 1 and rps == "rock":
    print("Tie!")
elif result == 2 and rps == "rock":
    print("Game Wins!")
elif result == 3 and rps == "rock":
    print(f"{username} Wins!")
elif result == 1 and rps == "paper":
    print(f"{username} Wins!")
elif result == 2 and rps == "paper":
    print("Tie!")
elif result == 3 and rps == "paper":
    print("Game Wins!")