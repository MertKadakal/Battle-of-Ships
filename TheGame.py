def main():
    with open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player1.txt") as player1_init, open("C:\\Users\\HP\\OneDrive\\Belgeler\\GitHub\\Battle-of-Ships\\Player2.txt") as player2_init:
        player1_init_list = []
        player2_init_list = []

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

        for i in player1_init_list:
            print(i)
        print()
        for i in player2_init_list:
            print(i)

if __name__ == "__main__":
    main()