# Smash Bracket v1
# CalvinHacks 2019
# Created by:

from random import shuffle


class Bracket:

    def __init__(self, bracket_size, player_list):
        """
        Initialize bracket
        :param bracket_size: number of players
        :param player_list: list of players sorted by seed
        """
        self.size = bracket_size
        self.player_list = player_list

    def __repr__(self):
        """
        Bracket shown in the terminal.
        :return: string representation of bracket
        """
        pass

    __str__ = __repr__

    def matchmaking(self):
        i = 0
        match_list = []
        if self.size // 2 == 0:  # if there is an even number of players every player has a match
            pass
        else:  # If there is an even number of players, one player is skipped first round
            pass
        return match_list


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
    bracket = Bracket(bracket_size, player_list)




def bracket_progression():
    """Progresses bracket through each round until the end.
    :return: New bracket for new round"""
    pass


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
    bracket_setup()


main()