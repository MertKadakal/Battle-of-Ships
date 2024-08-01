def main():
    with open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player1.txt", "r") as player1_init, open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player2.txt", "r") as player2_init, open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player1_moves.txt", "r") as player1_moves, open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player2_moves.txt", "r") as player2_moves, open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Battleship.txt", "w") as output_file:
        #initial ship positions of players
        player1_init_list = []
        player2_init_list = []

        #ship amounts of players
        cbdsp1 = [1,2,1,1,4]
        cbdsp2 = [1,2,1,1,4]

        #other initial variables
        turn = 1
        round = 1

        #creating players' moves as lists
        player1_moves_list = []
        player2_moves_list = []
        for move in player1_moves.read().split(";"):
            player1_moves_list.append(move)
        for move in player2_moves.read().split(";"):
            player2_moves_list.append(move)
        

        #creating players' initial hidden boards
        for line in player1_init:
            tem_line = ["-" for i in range(10)]
            ind = 0
            for i in range(len(line)):
                if line[i] == ";":
                    ind += 1
                elif line[i] != "\n":
                    tem_line[ind] = line[i]
            player1_init_list.append(tem_line)

        for line in player2_init:
            tem_line = ["-" for i in range(10)]
            ind = 0
            for i in range(len(line)):
                if line[i] == ";":
                    ind += 1
                elif line[i] != "\n":
                    tem_line[ind] = line[i]
            player2_init_list.append(tem_line)

        output_file.write("Battle of Ships Game\n\n")
        game_finished = False

        while not game_finished and False:
            output_file.write(f"Player{turn}'s Move\n\nRound: {round}         Grid Size: 10x10\n\n")
            print_hidden_boards(player1_init_list, player2_init_list, output_file)

def print_hidden_boards(p1, p2, output_file):
    output_file.write("Player1's Hidden Board		Player2's Hidden Board\n\n  A B C D E F G H I J		  A B C D E F G H I J\n")
    for i in range(10):
        if i == 9:
            output_file.write(str(i+1))
        else:
            output_file.write(str(i+1) + " ")

        for j in range(10):
            if j == 9:
                output_file.write(str(p1[i][j]))
            else:
                output_file.write(str(p1[i][j]) + " ")

        if i == 9:
            output_file.write("   " + str(i+1))
        else:
            output_file.write("   " + str(i+1) + " ")

        for j in range(10):
            if j == 9:
                output_file.write(str(p2[i][j]))
            else:
                output_file.write(str(p2[i][j]) + " ")

        output_file.write("\n")
    output_file.write("\n")


if __name__ == "__main__":
    main()