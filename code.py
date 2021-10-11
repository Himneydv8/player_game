# made by himneydv8
from random import *
from os import *
from time import *
need_to_sign_up = False
need_to_log_in = False
logged_in = False
wanted_pass = ""
wanted_pass_check = " "

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.score = 0
    def get_name(self):
        return self.name
    def add_score(self, counts):
        self.score = counts + self.score
    def tell_score(self):
        return self.score
    def get_id(self):
        return self.id

#get all accs
def give_accounts():
    return accounts
#get random id for player
def get_r_ip():
    return randint(1000000, 9999999)
#clearer
def clear():
        _ = system('cls')
#menu 
def menu():
    print("MENU")
    what_to_do = input("What do you want to do? play, ip, score, logout")
    if what_to_do == "play":
        points = game()
        Playerr.add_score(points)
        score = Playerr.tell_score()
        print(f"Score: {score}")
    elif what_to_do == "ip":
        print(ips[player_name_real])
    elif what_to_do == "score":
        print(Playerr.tell_score())
    elif what_to_do == "logout":
        print("Logging Out!")
        return "loggy"

        
#game
def game():
    diffi = input("Choose difficulty: Hard: 1 Medium: 2 Easy: 3 ")
    guesses = 1
    if int(diffi) == 1:
        random_num = randint(1, 10000)
        while guesses <= 21:
            print(f"Guess: {guesses}")
            guess = int(input("Put a number between 1, 10000"))
            if guess == int(guess):
                if guess == random_num:
                    print("You won")
                    sleep(5)
                    return 31 - guesses
                elif guess > random_num:
                    print("Lower")
                    guesses = guesses + 1
                elif guess < random_num:
                    print("Higher")
                    guesses = guesses + 1
            else:
                print("You didnt put number")
        print("You didnt win. You get it next time")
        return 0
        
    elif int(diffi) == 2:
        random_num = randint(1, 1000)
        while guesses <= 21:
            print(f"Guess: {guesses}")
            guess = int(input("Put a number between 1, 1000"))
            if guess == int(guess):
                if guess == random_num:
                    print("You won")
                    sleep(5)
                    return 21 - guesses
                elif guess > random_num:
                    print("Lower")
                    guesses = guesses + 1
                elif guess < random_num:
                    print("Higher")
                    guesses = guesses + 1
            else:
                print("You didnt put number")
        print("You didnt win. You get it next time")
        return 10

    elif int(diffi) == 3:
        random_num = randint(1, 100)
        while guesses <= 10:
            print(f"Guess: {guesses}")
            guess = int(input("Put a number between 1, 100"))
            if guess == int(guess):
                if guess == random_num:
                    print("You won")
                    sleep(5)
                    return 10 - guesses
                elif guess > random_num:
                    print("Lower")
                    guesses = guesses + 1
                elif guess < random_num:
                    print("Higher")
                    guesses = guesses + 1
            else:
                print("You didnt put number")
        print("You didnt win. You get it next time")
        return 0
    

                


#account list
accounts = {
    "himney": "869475409"
}
#ip list
ips = {
    
}

#ask if they have account
while True:
    ask_if_acc = input("Do you already have an account? yes or no // ")
    if ask_if_acc == "yes":
        need_to_log_in = True
        break
    elif ask_if_acc == "no":
        need_to_sign_up = True
        break
    else:
        print("yes or no")

#log in
if need_to_log_in == True:
    while True:
        print("Name:")
        player_name_dk = input("")
        if player_name_dk not in accounts:
            print("Your Username is wrong")
        else:
            print("Password:")
            player_pass_dk = input("")
            if accounts[player_name_dk] == player_pass_dk:
                print("You logged in!")
                logged_in = True
                player_name_real = player_name_dk
                break
            else:
                print("Your Username or Password is wrong")
                print("Try again")
#sign up
if need_to_sign_up == True:
    while True:
        print("Name:")
        wanted_name = input("")
        if wanted_name not in accounts:
            print("Pass:")
            wanted_pass = input("")
            print("Pass again:")
            wanted_pass_check = input("")
            if wanted_pass == wanted_pass_check:
                print("You signed up!")
                accounts[wanted_name] = wanted_pass
                logged_in = True
                player_name_real = wanted_name
                break
            else:
                print("Password is not the same")
        else:
            print("Name not avaible")

#only come here if logged in
print("You're in game!")
ips[player_name_real] = get_r_ip()

Playerr = Player(player_name_real, ips[player_name_real])
while True:
    sleep(3)
    clear()
    loggy = menu()
    if loggy == "loggy":
        break

print("Logging out")
for i in range(randint(4, 8)):
    print("...")
    sleep(0.5)
    clear()
print("bye bye ")
