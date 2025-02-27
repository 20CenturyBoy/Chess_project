class Game:

    def __init__(self, game_mode)
            initilze_players(game_mode)
            initilze_board

    def initilze_players(game_mode)
        if  game_mode == 1
            color = input("Which color would you like to pick")
            player_1 = Human_Player.new(color)
            if color.to_lowercase == "white"
                player_2 = Human_Player.new(color = "black")
            else
                player_2 = Human_Player.new(color = "white")
        #else

    def initilze_board
        board = [ [0]*8 for i in range(8)]
        for i in range(8)
            board[1][i] = Pawn.new
            board[6][i] = Pawn.new

        pieces = [Tower.new, Knight.new, Bishop.new, Queen.new, King.new]
        for i in range(4)
            board[0][i], board[0][-i] = pieces[i]
            board[7][i], board[7][-i] = pieces[i]
            if i == 3
                board[0][i] = Queen.new
                board[7][i] = Queen.new
                board[0][i + 1] = King.new
                board[0][i + 1] = King.new