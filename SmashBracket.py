# Smash Bracket v1
# CalvinHacks 2019
# Created by:

#from num2words import num2words
from random import shuffle
import math


class Bracket:

    def __init__(self, bracket_size, player_list):
        """
        Initialize bracket
        :param bracket_size: number of players
        :param player_list: list of players sorted by seed
        """
        self.size = bracket_size
        self.player_list = player_list
        self.current_matches = []

    def __repr__(self):
        """
        Bracket shown in the terminal.
        :return: string representation of bracket
        """
        pass

    __str__ = __repr__


class Player:
    """
    Creates player profile with Name, Character, Seeding, Status
    Seeding defaults to None
    Status defaults to Active = 1 (inactive = 0)"""

    def __init__(self, name, character, seed=None, status=1):
        self.name = name
        self.character = character
        self.seed = seed
        self.status = status

    def __repr__(self):
        return str(self.name) + ' as ' + str(self.character)

    __str__ = __repr__


def sort_players(player_list):
    """
    Sorts player_list
    :param player_list: unsorted list of players
    :return: sorted list of players
    """
    sorted_list = []
    i = 1
    while len(sorted_list) != len(player_list):
        for player in player_list:
            if player.seed == i:
                sorted_list.append(player)
                i += 1
    return sorted_list


def bracket_setup():
    """
    Setup bracket with players and player characters.
    Give option for manual seeding.
    :return: List of tuples (Name, Character, Seeding, Status)"""
    player_list = []
    bracket_size = 0
    key_in = input('Enter first player name: \n')
    while key_in != "next":
        name = key_in
        character = input("Character name: \n")
        player = Player(name, character)
        player_list.append(player)
        print("Added", player)
        bracket_size += 1
        key_in = input('Enter another player name or type "next" to continue: \n')
    seed = input("Would you like random seeding?\n(y/n)\n")
    if seed == "y":
        player_list = random_seed(player_list, bracket_size)
    else:
        for player in player_list:
            my_seed = int(input("What seed is " + str(player) + "?\n"))
            player.seed = my_seed
    player_list = sort_players(player_list)

    print(len(player_list))
    # playersNum = checkPlayers(17,17)
    playersNum = checkPlayers(len(player_list), len(player_list))
    print(playersNum)

    if playersNum - len(player_list) > 0:
        for x in range(playersNum - len(player_list)):
            name = "Person 0: Free Win"
            character = "p0"
            player = Player(name, character)
            player_list.append(player)

    bracket = Bracket(playersNum, player_list)
    match_list = []
    single_match = [None, None]
    print("--------Tournament Bracket------------")
    for y in range(0, math.ceil(bracket_size / 2)):
        if y + 1 != playersNum and y != 0:
            y = y + 1
        print("--------Bracket:------------")
#       print(y)
        print("Player 1:" + player_list[y].name)
        single_match[0] = player_list[y]

        # cmd=num2words(player_list[y].name) #To convert the Numbers to Text
        # #Calls the Espeak TTS Engine to read aloud the Numbers
        # call([cmd_beg+cmd+cmd_end], shell=True)
        # num2words("Versus")

        if y + 1 != playersNum:
            y = y + 1
        print("Player 2: " + player_list[y].name)
        single_match[1] = player_list[y]

        # cmd=num2words(player_list[y].name) #To convert the Numbers to Text
        # #Calls the Espeak TTS Engine to read aloud the Numbers
        # call([cmd_beg+cmd+cmd_end], shell=True)

        match_list.append(single_match)

#       print(y)
    print("-----------------------------")
    bracket.current_matches = match_list
    return bracket


def checkPlayers(players, playersDecrement):
#    print("Fixed Length: " + str(players))
#    print("Players Decrement: " + str(playersDecrement))
    if playersDecrement == 1.0:
        return players

    if playersDecrement % 2 == 0:
        return checkPlayers(players, playersDecrement / 2)
    elif playersDecrement % 2 == 1:
        players = players + 1
#        print("Fixed Length After: " + str(players))
        if players % 2 == 0:
            return checkPlayers(players, players)
        if players % 2 == 1:
            return checkPlayers(players + 1, players + 1)


def bracket_progression(bracket):
    """Progresses bracket through each round until the end.
    :param match_list: list of strings that contain the matches from the previous round
    :return: New bracket for new round"""
    winning_players = []
    out_matches = []
    i = 1
    for match in bracket.current_matches:
        winner = input("Who won round " + str(i) + " between " + str(match[0]) + " and " + str(match[1]) + "?\n")
        i += 1
        for player in bracket.player_list:
            if player.name == winner:
                winning_players.append(player)
            else:
                player.status = 0  # Deactivate losing player's status
    bracket.player_list = winning_players
    playersNum = checkPlayers(len(bracket.player_list), len(bracket.player_list))
    match_list = []
    single_match = [None, None]
    print("--------Tournament Bracket------------")
    for y in range(0, math.ceil(bracket.size / 2)):
        if y + 1 != playersNum and y != 0:
            y = y + 1
        print("--------Bracket:------------")
        #       print(y)
        print("Player 1:" + bracket.player_list[y].name)
        single_match[0] = bracket.player_list[y]

        # cmd=num2words(player_list[y].name) #To convert the Numbers to Text
        # #Calls the Espeak TTS Engine to read aloud the Numbers
        # call([cmd_beg+cmd+cmd_end], shell=True)
        # num2words("Versus")

        if y + 1 != playersNum:
            y = y + 1
        print("Player 2: " + bracket.player_list[y].name)
        single_match[1] = bracket.player_list[y]

        # cmd=num2words(player_list[y].name) #To convert the Numbers to Text
        # #Calls the Espeak TTS Engine to read aloud the Numbers
        # call([cmd_beg+cmd+cmd_end], shell=True)

        match_list.append(single_match)

    #       print(y)
    print("-----------------------------")
    bracket.current_matches = match_list
    return bracket


def random_seed(player_list, bracket_size):
    """Creates random seeding for players.
    :param: player_list = list of players without seeding
    :param: bracket_size = number of players
    :return: player_list updated with seeding"""
    seeding = [i for i in range(bracket_size)]
    shuffle(seeding)
    for i in range(bracket_size):
        player_list[i].seed = int(seeding[i]) + 1
    return player_list


def main():
    bracket = bracket_setup()
    while len(bracket.current_matches) > 1:
        bracket = bracket_progression(bracket)
    # final_round

main()
