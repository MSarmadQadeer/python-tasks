list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def panel():
    for row in range(0, 3):
        for column in range(0, 3):
            print(list1[row][column], end=" ")
            if column != 2:
                print(" | ", end="")
            if row == 2 and column == 2:
                break
            if column == 2:
                print()
                print("------------")


panel()
