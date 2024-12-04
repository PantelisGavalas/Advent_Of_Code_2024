list1 = []
list2 = []

#with open("C:\\Users\\gavalas\\Desktop\\Advent_of_Code_2024\\day1_problem2_input.txt", "r") as file:
with open("day_1\problem2\input.txt", "r") as file:
    
    for line in file:
        num1, num2 = map(int, line.strip().split())
        list1.append(num1)
        list2.append(num2)

similarity = 0

for num1 in list1:
    appearances = 0
    for num2 in list2:
        if num2 == num1:
            appearances += 1

    similarity += num1 * appearances

print(similarity)
