from random import shuffle

def player_guess():
    options = input('Hello! Welcome to the cup game!\n Press 6 - Start / 7 -  Exit game / 9 - Help: \n')
    while options not in ['6', '7', '9']:
        print("Choose a correct option!")

    if options == '6':
        player = input("Guess what cup has the ball below it: use 0 for - left cup/ 1 - middle cup/ 2 - right cup: \n")
        while player not in ['0', '1', '2']:
            print('Type a valid choice!')
        return int(player)

    elif options == '7':
        print('Ok, Se you next!')
        return 9

    elif options == '9':
        print('This is a guess game. You need to guess where the ball is.')
        print('This game has three cups and one ball.')
        options_help = input('Did you understand the rules? So... can we play now?\n 5 -  Go to home screen: \n Other number - Leave game\n')
        if options_help == '5':
            return player_guess()
        else:
            return 9

def shuffle_cup_game(cup_game):
    shuffle(cup_game)
    return cup_game

def game_answer(cup_game, player_guess):
    if cup_game[player_guess] == ' O ':
        print("YES!! You won the match!!")
        print(cup_game)
    else:
        print("Sorry, but you lost the match.")
        print(cup_game)

cup_game=['   ', '   ', ' O ']

want_to_play = int(input("Do you want to play the cup game? 1 - yes/ Other number - no.\n"))

while want_to_play == 1:
    answer_player = player_guess()
    if answer_player == 9:
        print("You chose to leave")
        break
    random_mixt_list = shuffle_cup_game(cup_game)
    game_answer(random_mixt_list, answer_player)
    want_to_play = int(input("Do you still want to play the cup game? 1 - yes/ Other number - no.\n"))