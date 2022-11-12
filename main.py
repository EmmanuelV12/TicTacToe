# *****************************************************************************
#                                                                             #
#                 Project name: Tic Tac Toe Text-based                        #
#                   Author: Emmanuel Vera Sanchez                             #
#                     Date: November 2th 2022                                 #
#                                                                             #
# ****************************************************************************

from random import choice
from ascii_art import logo, start

win_flag = False
player_character = {
    "first_player_character": "",
    "second_player_character": ""
}
player_1 = ""
player_2 = ""
first_player_char = ""
available_character = ['X', 'O']
player_turn = {
    "first_player": 0,
    "second_player": 0
}
player_result = {}
logic_game_area = ["", "", "", "", "", "", "", "", ""]
win_patterns_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]
game_area = """
                        *---*---*---*
                        | 7 | 8 | 9 |
                        *---*---*---*
                        | 4 | 5 | 6 |
                        *---*---*---*
                        | 1 | 2 | 3 |
                        *---*---*---*\n"""


def is_a_valid_name(name):
    if name != "":
        return True
    else:
        return False


def is_a_valid_char(char):
    if char == 'X' or char == 'O':
        return True
    elif char == "":
        return False
    else:
        print(f"The character {char} is unavailable.")
        return False


def update_game_area(player_move, player):
    global game_area
    game_area = game_area.replace(player_move,
                                  player_character[player + '_character'])
    print(game_area)


def is_the_box_available(player_move):
    available_box = False
    while not available_box:
        box = int(player_move) - 1
        if logic_game_area[box] == "":
            return True
        else:
            print("Box is unavailable")
            return False


def update_logic_game_area(player_move, player):
    box = int(player_move) - 1
    logic_game_area[box] = player_character[player + "_character"]
    player_turn[player] += 1


def did_the_player_win(player_name, player):
    global win_flag
    logic_game_area_cp = logic_game_area.copy()
    if player_turn[player] <= 2:
        return False
    else:
        player_moves = []
        while player_character[player + '_character'] in logic_game_area_cp:
            character_index = logic_game_area_cp.index(player_character[player + '_character'])
            player_moves.append(character_index)
            logic_game_area_cp[character_index] = ""
        for win_patter in win_patterns_list:
            for element in win_patter:
                if element in player_moves:
                    if win_patter.index(element) == 2:
                        player_result[player_name] = 'winner'
                        return True
                    continue
                else:
                    break


def are_there_empty_boxes():
    if "" in logic_game_area:
        return True
    else:
        return False


def play_turn(player, player_number):
    global win_flag
    player_move = input(f'{player} pick one box: ')
    while not is_the_box_available(player_move):
        player_move = input(f'{player} pick one box: ')
    update_logic_game_area(player_move, player_number)
    win_flag = did_the_player_win(player, player_number)
    update_game_area(player_move, player_number)


def display_result():
    if win_flag:
        for player, result in player_result.items():
            if result == 'winner':
                print(f'{player} wins !!!')
                break
    else:
        print("Match draw")


print(logo)
print(game_area)
while not is_a_valid_name(player_1):
    player_1 = input("Player one, please type your name: ")
while not is_a_valid_name(player_2):
    player_2 = input("Player two, please type your name: ")
players_list = [player_1, player_2]
first_player = choice(players_list)
players_list.remove(first_player)
second_player = players_list[0]
player_result[first_player] = ""
player_result[second_player] = ""
print(f'\nThe first player will be {first_player} and the second player'
      f' will be {second_player}\n')
while not is_a_valid_char(first_player_char):
    first_player_char = input(f"{first_player} please select -> 'X' or 'O': ").upper()
player_character['first_player_character'] = first_player_char
available_character.remove(first_player_char)
player_character['second_player_character'] = available_character[0]
print(f"{first_player}'s character -> {player_character['first_player_character']}")
print(f"{second_player}'s character -> {player_character['second_player_character']}\n")
print(start)
print(game_area)
while not win_flag and player_turn["first_player"] != 5:
    play_turn(first_player, 'first_player')
    if win_flag:
        break
    if player_turn["second_player"] < 4:
        play_turn(second_player, 'second_player')

display_result()
