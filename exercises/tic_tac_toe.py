'''
    This is the Tic Tac Toe game played from the console
'''


player1 = {
    "name": "Player 1",
    "symbol": "X",
    "moves": set()
}

player2 = {
    "name": "Player 2",
    "symbol": "O",
    "moves": set()
}

player_list = [player1, player2]

locations = {}

replay_game = "yes"
player_won = False


def set_replay(play_again):
    '''
    Function doc-string
    '''

    global replay_game
    replay_game = play_again.lower()


def replay():
    '''
    Function doc-string
    '''

    return replay_game == "yes"


def set_player_win(player_win):
    '''
    Function doc-string
    '''

    global player_won
    player_won = player_win


def win():
    '''
    Function doc-string
    '''

    global player_won
    return player_won


def is_move_valid(player_move):
    '''
    Function doc-string
    '''

    return player_move not in player_list[0]["moves"] and player_move not in player_list[1]["moves"]


def is_symbol_valid(symbol):
    '''
    Function doc-string
    '''

    return symbol in ("X", "O")


def initialise_game():
    '''
    Function doc-string
    '''

    global replay_game
    replay_game = "Yes"

    global player_won
    player_won = False

    global player_list
    for player in player_list:
        player["moves"] = set()


# SET NUMBERS FOR SYMBOL LOCATIONS
def initialise_locations():
    '''
    Function doc-string
    '''

    global locations

    locations = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }


def print_grid():
    '''
    Function doc-string
    '''

    global locations

    grid_lines = {
        "horizontal": "   |   |   \n",
        "vertical": "-----------\n",
        "level_one": " {} | {} | {}\n".format(locations["1"], locations["2"], locations["3"]),
        "level_two": " {} | {} | {}\n".format(locations["4"], locations["5"], locations["6"]),
        "level_three": " {} | {} | {}\n".format(locations["7"], locations["8"], locations["9"])
    }

    print(grid_lines["horizontal"] + grid_lines["level_one"] + grid_lines["horizontal"]
          + grid_lines["vertical"] + grid_lines["horizontal"] + grid_lines["level_two"]
          + grid_lines["horizontal"] + grid_lines["vertical"] + grid_lines["horizontal"]
          + grid_lines["level_three"] + grid_lines["horizontal"])


def congratulate_replay(string):
    '''
    Function doc-string
    '''

    set_player_win(True)
    print_grid()
    set_replay(input("{}\nDo you want to play again? Enter Yes or No: \n".format(string)))


def check_if_win(player):
    '''
    Function doc-string
    '''

    if (set(["1", "2", "3"]) == player["moves"] or set(["4", "5", "6"]) == player["moves"]
            or set(["7", "8", "9"]) == player["moves"] or set(["1", "5", "9"]) ==
            player["moves"] or set(["3", "5", "7"]) == player["moves"]):

        congratulate_replay("Congratulations! {}, you have won the game!".format(player["name"]))

    if len(player["moves"]) == 5:

        congratulate_replay("It's a tie!")


def play():
    '''
    Function doc-string
    '''

    global locations

    while not win():

        for player in player_list:

            print_grid()

            player_move = input("Choose your next position: (1-9)\n")

            # CHECK IF POSITION ALREADY TAKEN
            while not is_move_valid(player_move):

                player_move = input("Position already marked, please choose another position:\n")

            player["moves"].add(player_move)
            locations[player_move] = player["symbol"]

            check_if_win(player)

            if win():
                return

    print("while not win loop exit")


# GAME START
def start():
    '''
    Function doc-string
    '''

    print("Welcome to Tic Tac Toe!")

    player1["symbol"] = input("{}: Do you want to be X or O?\n".format(player1["name"])).upper()

    while not is_symbol_valid(player1["symbol"]):
        player1["symbol"] = input("Invalid character introduced. Please enter X or O:\n").upper()

    if player1["symbol"] == "O":
        player2["symbol"] = "X"

    print("{0} will go first.".format(player1["name"]))

    while replay():

        initialise_game()

        initialise_locations()

        play()

    print("Hope you had a good time!")


# START THE APPLICATION
#start()

    
