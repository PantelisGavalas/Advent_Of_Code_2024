def check_XMAS(row, column):
    if ((word_search[row-1][column-1] == "M" and word_search[row+1][column+1] == "S") or (word_search[row-1][column-1] == "S" and word_search[row+1][column+1] == "M")) and (
        (word_search[row-1][column+1] == "M" and word_search[row+1][column-1] == "S") or (word_search[row-1][column+1] == "S" and word_search[row+1][column-1] == "M")):
        return 1
    else:
        return 0

   
# for debug
# word_search = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]


with open("day_4\problem2\input.txt", "r") as file:
    
    word_search = []
    
    for line in file:
        word_search.append(line)

    
count = 0

for row_index in range(1, len(word_search)-1):
    for column_index in range(1, len(word_search[row_index])-1):
        if word_search[row_index][column_index] == "A":
            count += check_XMAS(row_index, column_index)
            
print(count)