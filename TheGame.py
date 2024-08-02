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
        columns = {"A": 0, "B": 1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
        ship_names = {"C": "Carrier", "B": "Battleship", "D": "Destroyer", "S": "Submarine", "P": "Patrol Boat"}
        player1_init_list_hidden = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], # these lists will be printed on output file
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],]
        player2_init_list_hidden = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],]

        #creating players' moves as lists
        player1_moves_list = []
        player2_moves_list = []
        for move in player1_moves.read().split(";"):
            player1_moves_list.append(move)
        for move in player2_moves.read().split(";"):
            player2_moves_list.append(move)
        player1_moves_list.pop(-1)
        player2_moves_list.pop(-1)        

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

        #parts left of battleships and patrol boats
        patrol_boats_1 = detect_pp_groups(player1_init_list.copy())
        patrol_boats_2 = detect_pp_groups(player2_init_list.copy())
        battleships_1 = detect_bbbb_groups(player1_init_list.copy())
        battleships_2 = detect_bbbb_groups(player2_init_list.copy())

        output_file.write("Battle of Ships Game\n\n")
        game_finished = False

        #the game starts here
        while not game_finished:

            #turn for player1
            turn = 1
            output_file.write(f"Player{turn}'s Move\n\nRound: {round}  --  Grid Size: 10x10\n\n")
            print_hidden_boards(output_file, player1_init_list_hidden, player2_init_list_hidden, False)
            row = int(player1_moves_list[round-1].split(",")[0])-1
            col = columns[player1_moves_list[round-1].split(",")[1]]

            if player2_init_list[row][col] == "O" or player2_init_list[row][col] == "X":
                print("This block has been already shot!")
            elif player2_init_list[row][col] == "-":
                player2_init_list_hidden[row][col] = "O"
                player2_init_list[row][col] = "O"
            else:
                ship = player2_init_list[row][col]
                player2_init_list_hidden[row][col] = "X"
                player2_init_list[row][col] = "X"
                if check_the_hitten_ship(ship, player2_init_list, battleships_2, patrol_boats_2, cbdsp2):
                    print(f"Player2's {ship_names[ship]} has been sunk!")
            print_players_ship_amounts(cbdsp1, cbdsp2, output_file)
            output_file.write(f"Enter your move: {player1_moves_list[round-1].split(',')[0]}, {player1_moves_list[round-1].split(',')[1]}\n\n")

            #turn for player2
            turn = 2
            output_file.write(f"Player{turn}'s Move\n\nRound: {round}  --  Grid Size: 10x10\n\n")
            print_hidden_boards(output_file, player1_init_list_hidden, player2_init_list_hidden, False)
            row = int(player2_moves_list[round-1].split(",")[0])-1
            col = columns[player2_moves_list[round-1].split(",")[1]]

            if player1_init_list[row][col] == "O" or player1_init_list[row][col] == "X":
                print("This block has been already shot!")
            elif player1_init_list[row][col] == "-":
                player1_init_list_hidden[row][col] = "O"
                player1_init_list[row][col] = "O"
            else:
                ship = player1_init_list[row][col]
                player1_init_list_hidden[row][col] = "X"
                player1_init_list[row][col] = "X"
                if check_the_hitten_ship(ship, player1_init_list, battleships_1, patrol_boats_1, cbdsp1):
                    print(f"Player1's {ship_names[ship]} has been sunk!")
            print_players_ship_amounts(cbdsp1, cbdsp2, output_file)
            output_file.write(f"Enter your move: {player2_moves_list[round-1].split(',')[0]}, {player2_moves_list[round-1].split(',')[1]}\n\n")
            
            #checking if the game is finished
            if cbdsp1 == cbdsp2 == [0,0,0,0,0]:
                output_file.write("It's a Draw!")
                game_finished = True
            elif cbdsp1 == [0,0,0,0,0]:
                output_file.write("Player2 wins!\n\nFinal Information\n\n")
                print_hidden_boards(output_file, player1_init_list, player2_init_list, True)
                print_players_ship_amounts(cbdsp1, cbdsp2, output_file)
                game_finished = True
            elif cbdsp2 == [0,0,0,0,0]:
                output_file.write("Player1 wins!\n\nFinal Information\n\n")
                print_hidden_boards(output_file, player1_init_list, player2_init_list, True)
                print_players_ship_amounts(cbdsp1, cbdsp2, output_file)
                game_finished = True

            round += 1

def print_hidden_boards(output_file, p1, p2, finish):
    #to print current boards during the game
    if finish:
        output_file.write("Player1's Board		            Player2's Board\n\n  A B C D E F G H I J		        A B C D E F G H I J\n")
    else:
        output_file.write("Player1's Hidden Board	      Player2's Hidden Board\n\n  A B C D E F G H I J	      	  A B C D E F G H I J\n")

<<<<<<< HEAD
=======
def print_hidden_boards(output_file, p1, p2, finish):
    if finish:
        output_file.write("Player1's Board		            Player2's Board\n\n  A B C D E F G H I J		        A B C D E F G H I J\n")
    else:
        output_file.write("Player1's Hidden Board	      Player2's Hidden Board\n\n  A B C D E F G H I J	      	  A B C D E F G H I J\n")

>>>>>>> d9a6d2d (Oyun tamamlandı, birkaç küçük eksik var)
    for i in range(10):
        if i == 9:
            output_file.write(str(i+1))
        else:
            output_file.write(str(i+1) + " ")

        for j in range(10):
            if j == 9:
                output_file.write(p1[i][j])
            else:
                output_file.write(p1[i][j] + " ")

        if i == 9:
            output_file.write("         " + str(i+1))
        else:
            output_file.write("         " + str(i+1) + " ")

        for j in range(10):
            if j == 9:
                output_file.write(p2[i][j])
            else:
                output_file.write(p2[i][j] + " ")
        output_file.write("\n")
    output_file.write("\n")

def detect_pp_groups(grid):
    groups = []

    def is_there_pp(row, col):
        if col + 1 < 10 and grid[row][col] == 'P' and grid[row][col + 1] == 'P':
            return [row, col], [row, col + 1]
        if row + 1 < 10 and grid[row][col] == 'P' and grid[row + 1][col] == 'P':
            return [row, col], [row + 1, col]
        return None

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'P':
                twos = is_there_pp(i, j)
                if twos:
                    groups.append(twos)
                    grid[twos[0][0]][twos[0][1]] = 'Z'
                    grid[twos[1][0]][twos[1][1]] = 'Z'

    for i in range(4):
        for j in range(2):
            grid[groups[i][j][0]][groups[i][j][1]] = "P"

    return groups

def detect_bbbb_groups(grid):
    groups = []

    def is_there_bbbb(row, col):
        if col + 3 < 10 and all(grid[row][col + i] == 'B' for i in range(4)):
            return [(row, col + i) for i in range(4)]
        if row + 3 < 10 and all(grid[row + i][col] == 'B' for i in range(4)):
            return [(row + i, col) for i in range(4)]
        return None

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'B':
                fours = is_there_bbbb(i, j)
                if fours:
                    groups.append(fours)
                    for (x, y) in fours:
                        grid[x][y] = 'Z'
    
    for i in range(2):
        for j in range(4):
            grid[groups[i][j][0]][groups[i][j][1]] = "B"

    return groups

def check_the_hitten_ship(ship, grid, bat_ship, pat_boats, cbdsp):
    #check the given ship if it's sunk completely
    if ship == "C" or ship == "S" or ship == "D":
        amount = 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == ship:
                    amount += 1
        if amount == 0:
            if ship == "C":
                cbdsp[0] = 0
            if ship == "S":
                cbdsp[3] = 0
            if ship == "D":
                cbdsp[2] = 0
            return True
        
    if ship == "P":
        pre_amo = cbdsp[4]
        amount = 4
        for i in range(len(pat_boats)):
            row1 = pat_boats[i][0][0]
            col1 = pat_boats[i][0][1]
            row2 = pat_boats[i][1][0]
            col2 = pat_boats[i][1][1]
            if grid[row1][col1] + grid[row2][col2]  == "XX":
                amount -= 1
        if amount == 0:
            cbdsp[4] = amount
            return True
        else:
            cbdsp[4] = amount
            if amount != pre_amo:
                return True
        
    if ship == "B":
        pre_amo = cbdsp[1]
        amount = 2
        for i in range(len(bat_ship)):
            row1 = bat_ship[i][0][0]
            col1 = bat_ship[i][0][1]
            row2 = bat_ship[i][1][0]
            col2 = bat_ship[i][1][1]
            row3 = bat_ship[i][2][0]
            col3 = bat_ship[i][2][1]
            row4 = bat_ship[i][3][0]
            col4 = bat_ship[i][3][1]
            if grid[row1][col1] + grid[row2][col2] + grid[row3][col3] + grid[row4][col4]  == "XXXX":
                amount -= 1
        if amount == 0:
            cbdsp[1] = amount
            return True
        else:
            cbdsp[1] = amount
            if amount != pre_amo:
                return True

    return False

def print_players_ship_amounts(p1, p2, output):
    nameslist = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boats"]
    namesdict = {"Carrier": 1, "Battleship": 2, "Destroyer": 1, "Submarine": 1, "Patrol Boats": 4}
    for i in range(5):
        row1 = f"{nameslist[i]}:" + (namesdict[nameslist[i]]-p1[i])*" X" + p1[i]*" -"
        row2 = f"{nameslist[i]}:" + (namesdict[nameslist[i]]-p2[i])*" X" + p2[i]*" -"
        row = "%-30s" % row1
        output.write(row + row2 + "\n")
    output.write("\n")

if __name__ == "__main__":
    main()