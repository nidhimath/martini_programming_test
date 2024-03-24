# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#Function 1:
def min_paint(raw_data):
    # Convert_input converts data into dictionary usable format
    def convert_input():
        value_dict = {
            "W": 0,
            "B": 0
        }
        for i in raw_data:
            if i == "W":
                value_dict["W"] += 1
            elif i == "B":
                value_dict["B"] += 1
            else:
                print("Wrong input")
                return None

        return value_dict

    value_dict = convert_input()

    # If value_dict = None, then the Wrong Data has been inputted, so we return None
    if(value_dict == None):
        return None

    # tests to see the min number of houses that need to be painted for appealing
    first_val = 0
    second_val = 0
    for i in range(0,len(raw_data)):
        if (raw_data[i]=="B" and i<value_dict["W"]) or (raw_data[i]=="W" and i>=value_dict["W"]):
            first_val += 1
        elif (raw_data[i]=="W" and i<value_dict["B"]) or (raw_data[i]=="B" and i>=value_dict["B"]):
            second_val += 1

    return min(first_val,second_val)

# Function 2
def min_square():
    # Convert data into n by m array of arrays
    n, m = map(int, input().split())

    board = set()

    # Read board configuration
    for row_num in range(n):
        row = input().strip()
        for col in range(m):
            if row[col] == "X":
                board.add((row_num,col))

    print(board)

    # if no X exists
    if len(board) == 0:
        return min(n,m)

    # Finding the val of square frame
    min_row = n
    max_row = -1
    min_col = m
    max_col = -1

    for loc in board:
        if loc[0] < min_row:
            min_row = loc[0]
        if loc[0] > max_row:
            max_row = loc[0]
        if loc[1] < min_col:
            min_col = loc[1]
        if loc[1] > max_col:
            max_col = loc[1]

    row_len = max_row-min_row+1
    col_len = max_col-min_col+1


    # Testing to see if distance of row is greater than m VV
    if m < (row_len) or n < (col_len):
        return 1

    # Test to see if row len and col len are the same
    if row_len != col_len:
        return 1

    square_len = max(row_len, col_len)

    # Testing to see if stuff inside
    for loc in board:
        if loc[0] is not min_row and loc[0] is not max_row and loc[1] is not min_col and loc[1] is not max_col:
            return 1


    return square_len






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("This is the main function")
    # print(min_paint("BWBWBWBWBW"))
    # print(min_paint())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
