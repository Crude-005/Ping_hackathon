import database
import api_functions
import game_functions


def main():
    name , age = game_functions.welcome()
    database.main_character['name'] = name
    database.main_character['age'] = age
    game_functions.main_menu()
    print("Thanks for playing")
    print("Credit: Chirag Sugla")



main()

