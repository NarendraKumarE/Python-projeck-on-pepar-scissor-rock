import random 

user_wins = 0
computer_wins = 0 
option =["rock","pepar", "scissors"]
while True:
    user_input = input("Type Rock/Pepar/Scissors or q to quit: ").lower()
    if user_input == "q" :
        break
    if user_input not in option :
        continue
    random_number = random.randint(0,2)
    # Rcok = 0,Paper =1,scissors =2
    computer_pick = option[random_number]
    print("Computer picked ",computer_pick)

    if random_number=="rock"and computer_pick == "scissors":
        print("You won !")
        user_wins+=1
    elif random_number=="pepar"and computer_pick == "rock":
        print("You won !")
        user_wins+=1
    elif random_number=="scissors"and computer_pick == "pepar":
        print("You won !")
        user_wins+=1
    else:
        print("You lost!")
        computer_wins+=1
print("You won",user_wins,"times" )
print("Computer won",computer_wins,"times")
print("Good bye!")

