import random
mylist = ["R", "P", "S"]
print("welcome to rock, paper, scissors game...")
def play_game():
    sel = random.choice(mylist)
    user_input = input("pick one of R, P, S: ")
    user_input = user_input.upper()
    while user_input not in mylist:
        user_input = input("pick one of R, P, S: ").upper()
    if sel == user_input:
        print("There's a tie...")
        play_game()
    else:
        if sel == "R" and user_input == "S":
            print("Computer wins")
        elif sel == "S" and user_input == "R":
            print("Computer wins")
        elif sel == "P" and user_input == "S":
            print("User wins")
        elif sel == "S" and user_input == "P":
            print("Computer wins")
        elif sel == "P" and user_input == "R":
            print("Computer wins")
        elif sel == "R" and user_input == "P":
            print("User wins")

play_game()
