from game import Game


def main():
    play = True
    game = Game()
    while play:
        print("Welcome to Tic Tac Toe game")
        option = str(input("Please choose an option, for two players, press 1, for human vs computer, press 2\n"))
        if option == '1':
            game.two_players()
        elif option == '2':
            game.player_vs_computer()
        else:
            print('Wrong choice! please press 1 or 2')


if __name__ == '__main__':
    main()
