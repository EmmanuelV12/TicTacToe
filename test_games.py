from random import randint, choice


def game():
    is_game_on = True
    current_winner = "None"
    position_already_taken = True

    # Possible winning combos for Player One During Move 4
    possible_winning_combos = []

    # Possible winning combos for Player One During Move 6
    possible_winning_combos_move_6 = []

    # Keeps track of previous computer positions
    computer_positions = []

    # Keeps track of previous player positions
    player_positions = []

    # Defines position that allows a player to win
    winning_combo_positions = [
        # Horizontal Winning Positions
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Vertical Winning Positions
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonal Winning Positions
        [0, 4, 8],
        [2, 4, 6],
    ]

    print("""
     _____  _  ____    _____  ____  ____    _____  ____  _____
    /__ __\/ \/   _\  /__ __\/  _ \/   _\  /__ __\/  _ \/  __/
      / \  | ||  /      / \  | / \||  /      / \  | / \||  \  
      | |  | ||  \_     | |  | |-|||  \_     | |  | \_/||  /_ 
      \_/  \_/\____/    \_/  \_/ \|\____/    \_/  \____/\____/
    """)

    print(
        "Welcome to the Tic Tac Toe Game!\nThis is a two player game. Player One is X and the Computer is O.\n")

    input("Press Enter to continue... ")

    print(
        "\nTo place a X or O, input the number of the position you would like to input a X or O.\n")
    print(" 0 | 1 | 2 ")
    print("___________")
    print(" 3 | 4 | 5 ")
    print("___________")
    print(" 6 | 7 | 8 ")

    symbol_tracker = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    for move in range(1, 10):

        # Human Player
        if move % 2 != 0:
            player = "Player One"
            symbol = "X"

            player_position = int(input(
                f"\n{player}, where would you like to place {symbol}? Input a number 0 to 8: "))

            # Checks if player tries to put character in position that is already taken
            while position_already_taken:
                if symbol_tracker[player_position] == "X" or symbol_tracker[
                    player_position] == "O":
                    player_position = int(
                        input(
                            f"\n{player}, that position is already taken. Please input another number 0 to 8: "))
                else:
                    break

            symbol_tracker[player_position] = symbol

            player_positions.append(player_position)

            # print(f"Player positions so far {player_positions}")

        # Computer Player Logic
        else:
            player = "Computer"
            symbol = "O"

            if move == 2:

                if player_positions[0] != 4:
                    computer_position = 4
                else:
                    computer_position = randint(0, 8)

            elif move == 4:

                for winning_combo in winning_combo_positions:
                    for winning_position in winning_combo:
                        if winning_position == player_positions[0]:
                            possible_winning_combos.append(winning_combo)

                # print(f'The first round of possible winning combos for Player One are {possible_winning_combos}')

                found_target_combo = False

                for winning_combo in possible_winning_combos:
                    if found_target_combo:
                        break
                    for winning_position in winning_combo:
                        if winning_position == player_positions[1]:
                            combo_to_target = winning_combo
                            found_target_combo = True
                            break
                        else:
                            combo_to_target = choice(possible_winning_combos)

                # print(f'The second round of possible winning combos for Player One are {possible_winning_combos}')

                random_winning_combo_selection = combo_to_target
                # print(f"The computer chose to go with {random_winning_combo_selection} to try to block Player One.")

                for position_to_target in combo_to_target:
                    if position_to_target not in player_positions:
                        computer_position = position_to_target
                        break

                # print(f"The computer chose position {computer_position} for move 4.")

            elif move == 6 or move == 8:

                for winning_combo in winning_combo_positions:
                    for winning_position in winning_combo:
                        if winning_position in player_positions and winning_combo not in possible_winning_combos_move_6:
                            possible_winning_combos_move_6.append(
                                winning_combo)

                # print(f'The first round of possible winning combos for Player One are {possible_winning_combos_move_6}')

                found_target_combo = False

                for winning_combo in possible_winning_combos_move_6:
                    for winning_position in winning_combo:
                        if symbol_tracker[winning_position] == 'O':
                            possible_winning_combos_move_6.remove(
                                winning_combo)
                            break

                # print(
                #     f'The second round of possible winning combos for Player One are {possible_winning_combos_move_6}')

                found_target_combo = False

                for winning_combo in possible_winning_combos_move_6:
                    # To find winning combo with 2 X's and One Space
                    num_x = 0
                    num_space = 0
                    for winning_position in winning_combo:
                        if 'X' in symbol_tracker[winning_position]:
                            num_x += 1
                        elif ' ' in symbol_tracker[winning_position]:
                            num_space += 1

                    if num_x == 2 and num_space == 1:
                        combo_to_target_move_6 = winning_combo
                        break
                    else:
                        combo_to_target_move_6 = choice(
                            possible_winning_combos_move_6)

                # print(f"The computer chose to go with {combo_to_target_move_6} to try to block Player One.")

                for position_to_target in combo_to_target_move_6:
                    if position_to_target not in player_positions:
                        computer_position = position_to_target
                        break

                # print(f"The computer chose position {computer_position} for move 6.")

            else:
                computer_position = randint(0, 8)

            # Checks if AI tries to put character in position that is already taken
            while position_already_taken:
                if symbol_tracker[computer_position] == "X" or symbol_tracker[
                    computer_position] == "O":
                    # print(f"The computer tried to place O in position {computer_position}, which is already taken.")
                    computer_position = randint(0, 8)
                else:
                    break

            computer_positions.append(computer_position)

            symbol_tracker[computer_position] = symbol

            # print(f"The computer has played the positions so far of {computer_positions}")

        print(
            f"\n {symbol_tracker[0]} | {symbol_tracker[1]} | {symbol_tracker[2]} ")
        print("___________")
        print(
            f" {symbol_tracker[3]} | {symbol_tracker[4]} | {symbol_tracker[5]} ")
        print("___________")
        print(
            f" {symbol_tracker[6]} | {symbol_tracker[7]} | {symbol_tracker[8]} ")

        # Winning Logic for Current Player

        for winning_combo in winning_combo_positions:
            if symbol_tracker[winning_combo[0]] == symbol and symbol_tracker[
                winning_combo[1]] == symbol and \
                    symbol_tracker[winning_combo[2]] == symbol:
                current_winner = player
                is_game_on = False
                break

        if not is_game_on:
            break

    if current_winner == "None":
        print("\nThere was no winner. The result is a tie!")
    else:
        print(f'\nThe winner is {current_winner}.')


want_to_play = "Y"

# Initializes Tic Tac Toe Game
while want_to_play == "Y":
    game()
    want_to_play = input("\nWould you like to play Tic Tac Toe again? (Y/N): ")

print("\nThank you for playing Tic Tac Toe!")
