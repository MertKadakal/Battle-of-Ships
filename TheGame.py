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
        player1_init_list_hidden = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
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
        patrol_boats_1 = park_gruplarini_belirle(player1_init_list)
        patrol_boats_2 = park_gruplarini_belirle(player2_init_list)
        battleships_1 = dortlu_b_gruplarini_belirle(player1_init_list)
        battleships_2 = dortlu_b_gruplarini_belirle(player2_init_list)

        output_file.write("Battle of Ships Game\n\n")
        game_finished = False

        while not game_finished:
            turn = 1
            output_file.write(f"Player{turn}'s Move\n\nRound: {round}         Grid Size: 10x10\n\n")
            print_hidden_boards(output_file, player1_init_list_hidden, player2_init_list_hidden)
            if turn == 1:
                row = int(player1_moves_list[round-1].split(",")[0])-1
                col = columns[player1_moves_list[round-1].split(",")[1]]

                if player2_init_list[row][col] == "O" or player2_init_list[row][col] == "X":
                    print("This block has been already shot!")
                elif player2_init_list[row][col] == "-":
                    player2_init_list_hidden[row][col] = "O"
                    player2_init_list[row][col] = "O"
                else:
                    player2_init_list_hidden[row][col] = "X"
                    player2_init_list[row][col] = "X"
                    if check_the_hitten_ship(player2_init_list[row][col], player2_init_list, battleships_2, patrol_boats_2, cbdsp2):
                        output_file.write(f"Player2's {ship_names[player2_init_list[row][col]]} has been sunk!")

            turn = 2
            output_file.write(f"Player{turn}'s Move\n\nRound: {round}         Grid Size: 10x10\n\n")
            print_hidden_boards(output_file, player1_init_list_hidden, player2_init_list_hidden)
            if turn == 1:
                row = int(player1_moves_list[round-1].split(",")[0])
                col = columns[player1_moves_list[round-1].split(",")[1]]

                if player1_init_list[row][col] == "O" or player1_init_list[row][col] == "X":
                    print("This block has been already shot!")
                elif player1_init_list[row][col] == "-":
                    player1_init_list_hidden[row][col] = "O"
                    player1_init_list[row][col] = "O"
                else:
                    player1_init_list_hidden[row][col] = "X"
                    player1_init_list[row][col] = "X"
                    if check_the_hitten_ship(player1_init_list[row][col], player1_init_list, battleships_1, patrol_boats_1, cbdsp1):
                        output_file.write(f"Player1's {ship_names[player1_init_list[row][col]]} has been sunk!")

            round += 1


def print_hidden_boards(output_file, p1, p2):
    output_file.write("Player1's Hidden Board		Player2's Hidden Board\n\n  A B C D E F G H I J		  A B C D E F G H I J\n")
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
            output_file.write("   " + str(i+1))
        else:
            output_file.write("   " + str(i+1) + " ")

        for j in range(10):
            if j == 9:
                output_file.write(p2[i][j])
            else:
                output_file.write(p2[i][j] + " ")

        output_file.write("\n")
    output_file.write("\n")

def park_gruplarini_belirle(grid):
    init_grid = grid
    satir_sayisi = 10
    sutun_sayisi = 10
    gruplar = []  # Grupları saklamak için liste

    def pp_cifti_var_mi(satir, sutun):
        # İkili "PP" yatay olarak kontrol edilir
        if sutun + 1 < sutun_sayisi and grid[satir][sutun] == 'P' and grid[satir][sutun + 1] == 'P':
            return [satir, sutun], [satir, sutun + 1]
        # İkili "PP" dikey olarak kontrol edilir
        if satir + 1 < satir_sayisi and grid[satir][sutun] == 'P' and grid[satir + 1][sutun] == 'P':
            return [satir, sutun], [satir + 1, sutun]
        return None

    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            if grid[i][j] == 'P':
                cift = pp_cifti_var_mi(i, j)
                if cift:
                    gruplar.append(cift)
                    # İşaretlenen "PP" çiftlerini "Z" olarak işaretleyerek tekrar kontrol edilmelerini önleyin
                    grid[cift[0][0]][cift[0][1]] = 'Z'
                    grid[cift[1][0]][cift[1][1]] = 'Z'

    grid = init_grid
    return gruplar

def dortlu_b_gruplarini_belirle(grid):
    init_grid = grid
    satir_sayisi = 10
    sutun_sayisi = 10
    gruplar = []  # Grupları saklamak için liste

    def bbbb_dortlusu_var_mi(satir, sutun):
        # Dörtlü "BBBB" yatay olarak kontrol edilir
        if sutun + 3 < sutun_sayisi and all(grid[satir][sutun + i] == 'B' for i in range(4)):
            return [(satir, sutun + i) for i in range(4)]
        # Dörtlü "BBBB" dikey olarak kontrol edilir
        if satir + 3 < satir_sayisi and all(grid[satir + i][sutun] == 'B' for i in range(4)):
            return [(satir + i, sutun) for i in range(4)]
        return None

    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            if grid[i][j] == 'B':
                dortlu = bbbb_dortlusu_var_mi(i, j)
                if dortlu:
                    gruplar.append(dortlu)
                    # İşaretlenen "BBBB" dörtlülerini "Z" olarak işaretleyerek tekrar kontrol edilmelerini önleyin
                    for (x, y) in dortlu:
                        grid[x][y] = 'Z'

    grid = init_grid
    return gruplar

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
        amount = 0
        for i in range(len(pat_boats)):
            row1 = pat_boats[i][0][0]
            col1 = pat_boats[i][0][1]
            row2 = pat_boats[i][1][0]
            col2 = pat_boats[i][1][1]
            if grid[row1][col1] + grid[row2][col2]  == "XX":
                amount =+ 1
        if amount == 4:
            return True
        else:
            cbdsp[2] = amount
        
    if ship == "B":
        amount = 0
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
                amount =+ 1
        if amount == 2:
            return True
        else:
            cbdsp[1] = amount

    return False

if __name__ == "__main__":
    main()