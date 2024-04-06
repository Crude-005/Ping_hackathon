import database
import api_functions
import random

def get_int():
    num = input(": ")
    if num.isnumeric():
        return num
    print("Invalid input. You have to enter a num")
    return get_int()


def check_level():
    if database.level >=1:
        print("System: You are now officially a Playboy.")
        print("CONRATULATIONS!!!")

def check_tamed_level(name):
    if database.girls[name]['tamed'] >=1:
        database.level+=0.2
        check_level()
        print(f"System: {name} is now fully attracted to you.\nYour level has also incresed")


def ask_her_questions(name):

    while (True):
        print(f"You are asking {name} questions")
        print("What question you want to ask? Enter your choice")
        print(" [1] What is your age?")
        print(" [2] What is your zodiac sign?")
        print(" [3] Who is you favourite celebrity?")
        print(" [4] What is your favourite colour?")
        print(" [0] to return")
        chosen = input(": ")
        if chosen == '0':
            return
        elif chosen == '1':
            print(f"{name}: Though you shouldn't ask a girl her age. Still I will tell you")
            print(f"I am {database.girls[name]['age']} years old")
        elif chosen == '2':
            print(f"{name}: My zodiac sign is {database.girls[name]['zodiac_sign']}")
        elif chosen == '3':
            print(f"{name}: My favourite celebrity is {database.girls[name]['fav_celeb']} ")
        elif chosen == '4':
            print(f"{name}: My favourite colour is {database.girls[name]['fav_colour']}")
        else:
            print("System: Invalid Input. ")

def lets_rhyme(name):
    print()
    print(f"{name}: Hey Let's Rhyme \nWhy don't you start with a sentence")
    sentence = input("Sytem: Write a sentence : ")
    print (f"{name}: " , api_functions.rhyme(sentence))
    sentence = input("Sytem: Write another sentence : ")
    print (f"{name}: " , api_functions.rhyme(sentence))
    sentence = input("Sytem: Write another sentence : ")
    print (f"{name}: " , api_functions.rhyme(sentence))
    print (f"{name}: It was so fun..")
    database.girls[name]['tamed'] += 0.1
    check_tamed_level(name)
    print(f"System: {name} interest in you has been increased ")


def lets_def(name):
    
    ans = '1'
    word = random.choice(database.words_list)
    print(f"{name}: Can you tell me the meaning of {word}")
    print("Enter [1] to use Define Function\n [2] to use Antonym Function\n [3] to use Synonym Function")
    chosen = input(": ")
    if chosen == '1':
        print(f"{database.main_character['name']}: Too easy. It means: ",api_functions.define(word))
    elif chosen == '2':
        print(f"{database.main_character['name']}: Too easy. It opposite is : ",api_functions.antonym(word))
    elif chosen == '3':
        print(f"{database.main_character['name']}: Too easy. It is same as : ",api_functions.synonym(word))
    

    if chosen == ans :
        print(f"{name}:Wow {database.main_character['name']}! You are so intelligent.")
        database.girls[name]['tamed'] += 0.2
        check_tamed_level(name)
        print(f"System: {name} interest in you has been increased. ")
    else:
        print(f"{name}: You are really Dumb.")
        database.girls[name]['tamed'] -= 0.1
        print(f"System: {name} interest in you has been decreased. ")

def lets_astrology(name):
    print(f"{name}: Nothing is going good in my life.")
    print(f"{database.main_character['name']}: Dear {name} Show me your hand. I will tell you your future.")
    print("You decided to use your astrological powers")
    n = input("System: Enter a name")
    a = input("System: Enter age")
    s = input("System: Enter Zodiac sign")
    print(f"{database.main_character['name']}: {api_functions.astrologer(n,a,s)}")
    print(f"{name}:Wow {database.main_character['name']}! You are so amazing.")
    database.girls[name]['tamed'] += 0.1
    check_tamed_level(name)
    print(f"System: {name} interest in you has been increased.")



def lets_celebrity(name):
    print(f"{name}: {database.main_character['name']} Do you know {database.girls[name]['fav_celeb']} is my favourite celebrity.")
    print(f"{database.main_character['name']}: Dear {name} Do you know ")
    n = input("System: You decided to use your celebrity powers. Enter a name: ")
    print(f"{database.main_character['name']}: {api_functions.celebrity(n)}")
    print(f"{name}:Wow {database.main_character['name']}! You are so amazing.")
    database.girls[name]['tamed'] += 0.1
    check_tamed_level(name)
    print(f"System: {name} interest in you has been increased.")


def lets_joke(name):
    print(f"{name}: {database.main_character['name']} , I am feeling down today. Do you have something to lighten me up?")
    print(f"{database.main_character['name']}: Dear {name} Why dont i lighten your mood by a joke.")
    n = input("System: You decided to use your joking powers. Enter a topic: ")
    print(f"{database.main_character['name']}: {api_functions.joke(n)}")
    print(f"{name}:Wow {database.main_character['name']}! You are so funny.")
    database.girls[name]['tamed'] += 0.2
    check_tamed_level(name)
    print(f"System: {name} interest in you has been increased.")

def lets_flatter(name):
    print(f"{name}: {database.main_character['name']} , Why don't you try hitting on me")
    print(f"{database.main_character['name']}: Why not I would love to.")
    n = input("System: You decided to use your charming powers. Enter a topic: ")
    print(f"{database.main_character['name']}: {api_functions.pickup_line(n)}")
    print(f"{name}:{database.main_character['name']}. Don't flatter me like that.")
    database.girls[name]['tamed'] += 0.2
    check_tamed_level(name)
    print(f"System: {name} interest in you has been increased.")



def answer_her_questions(name):
    while(True):
        options = ['intelligence','astrologer', 'celebrity' , 'joke' , 'pickup_line']
        chosen = random.choice(options)
        if chosen == 'intelligence':
            chosen = random.choice(options)
            options = ['Def','syn','ant','celeb']
            if chosen == 'Def':
                lets_def(name,'1')
            elif chosen == 'syn':
                lets_def(name,'3')
            elif chosen == 'ant':
                lets_def(name,'2')
        elif chosen == 'astrologer':
            lets_astrology(name)
        elif chosen == 'celbrity':
            lets_celebrity(name)
        elif chosen == 'joke':
            lets_joke(name)
        elif chosen == 'pickup_line':
            lets_flatter(name)
        
        print("System: Do you want to continue\n [1] yes \n [2] no")
        chosen = input(": ")
        if chosen == '2':
            return
    

def talk_to_girl(name):
    while(True):
        print("You are currently talking to", name)
        print("Enter\n [0] to talk to another girl\n [1] to check her interest in you\n [2] to ask questions \n [3] to answer her questions\n [4] to rhyme with her")
        chosen = input(": ")
        if chosen == '0':
            return
        elif chosen == '1':
            x = database.girls[name]['tamed'] * 100
            print(f"{name} is {x}% interested in you.")
        elif chosen == '2':
            ask_her_questions(name)
        elif chosen == '3':
            answer_her_questions(name)
        elif chosen == '4':
            lets_rhyme(name)
        else:
            print("Invalid Input")

        return








def change_info_main_character():
    print("Change your information")
    while(True):
        print("Enter\n [0] to retrun to Main Menu\n [1] to change name \n [2] to change age")
        chosen = input(': ' )
        if chosen == '0':
            return
        elif chosen == '1':
            name = input("Enter new name: ")
            database.main_character['name'] = name
            print("Name changed successfully.")
        elif chosen == '2':
            age = input("Enter new age: ")
            database.main_character['age'] = age
            print("Age changed successfully.")
        else:
            print("Invalid Input. Try Again")

def start_adventure():
    while( True):
        print("\nLet's start the adventure:\n")
        print("Enter \n [0] to return to Main Menu \n [1] to approach a girl")
        chosen = input(": ")
        if chosen == '0':
            print("\n\n returning to main menu...")
            return
        print("Here's the list of girls you can approach.Choose one.")
        for i,name in enumerate(database.girls['list']):
            print(f" [{i+1}] {name}")
        chosen = get_int()
        if int(chosen) in range(1,6):
            talk_to_girl(database.girls['list'][chosen-1])
        else:
            print("Number is out of range.Please choose a valid number")
            continue


def main_menu():
    while(True):
        print("Main Menu\n")
        print("Enter\n [0] to quit\n [1] to start your adventure \n [2] to change your info")
        chosen = input(': ' )
        if chosen == '0':
            print("""If you chose to quit all your progress will be nullified.
You wont be able to continue.
                  
Are you sure you want to quit
Enter\n [1] Yes \n [2] NO""")
            chosen = input(': ')
            if chosen == '1':
                return
            else:
                continue
        elif chosen == '1':
            start_adventure()
        elif chosen == '2':
           change_info_main_character()
        else:
            print("Invalid Input. Try Again")






def welcome():
    print('''Playboy in the Room.

Welcome to 'Playboy in the Room'.
You aim in this game is to make all the gilrs fall in love with you.
          
Are you ready to dive into fun?
[1] Yes
[2] No
''')
    chosen_to_play = input(": ")
    if chosen_to_play == '2':
        print("Too late. You are alreaady trapped in this game.")
    else:
        print("OK! So lets begin.")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

