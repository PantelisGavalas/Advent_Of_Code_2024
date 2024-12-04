def vertical(row, column):
    if (word_search[row][column] == "X" and word_search[row][column+1] == "M" and word_search[row][column+2] == "A" and word_search[row][column+3] == "S") or (
        word_search[row][column] == "S" and word_search[row][column+1] == "A" and word_search[row][column+2] == "M" and word_search[row][column+3] == "X"):
        return 1
    else:
        return 0

def horizontal(row, column):
    if (word_search[row][column] == "X" and word_search[row+1][column] == "M" and word_search[row+2][column] == "A" and word_search[row+3][column] == "S") or (
        word_search[row][column] == "S" and word_search[row+1][column] == "A" and word_search[row+2][column] == "M" and word_search[row+3][column] == "X"):
        return 1
    else:
        return 0

def diag_down_right(row, column):
    if (word_search[row][column] == "X" and word_search[row+1][column+1] == "M" and word_search[row+2][column+2] == "A" and word_search[row+3][column+3] == "S") or (
        word_search[row][column] == "S" and word_search[row+1][column+1] == "A" and word_search[row+2][column+2] == "M" and word_search[row+3][column+3] == "X"):
        return 1
    else:
        return 0

def diag_down_left(row, column):
    if (word_search[row][column] == "X" and word_search[row+1][column-1] == "M" and word_search[row+2][column-2] == "A" and word_search[row+3][column-3] == "S") or (
        word_search[row][column] == "S" and word_search[row+1][column-1] == "A" and word_search[row+2][column-2] == "M" and word_search[row+3][column-3] == "X"):
        return 1
    else:
        return 0
   
# for debug
#word_search = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]


with open("day_4\problem1\input.txt", "r") as file:
    
    word_search = []
    
    for line in file:
        word_search.append(line)
    
count = 0

for row_index in range(0, len(word_search)):
    for column_index in range(0, len(word_search[row_index])):
        if column_index <= len(word_search[row_index])-4:
            count += vertical(row_index, column_index)
        if row_index <= len(word_search)-4:
            count += horizontal(row_index, column_index)
        if (column_index <= len(word_search[row_index])-4) and (row_index <= len(word_search)-4):
            count += diag_down_right(row_index, column_index)
        if (column_index >= 3) and (row_index <= len(word_search)-4):
            count += diag_down_left(row_index, column_index)
            
print(count)