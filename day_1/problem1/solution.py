list1 = []
list2 = []

#with open("C:\\Users\\gavalas\\Desktop\\Advent_of_Code_2024\\day1_problem1_input.txt", "r") as file:
with open("day_1\problem1\input.txt", "r") as file:

    for line in file:
        num1, num2 = map(int, line.strip().split())
        list1.append(num1)
        list2.append(num2)

list1_sorted = sorted(list1)
list2_sorted = sorted(list2)
'''
print(list1)
print("\n\n\n")
print(list1_sorted)
print("\n\n\n\n\n\n")
print(list2)
print("\n\n\n")
print(list2_sorted)
print("\n\n\n\n\n\n")
'''

count = 0

for i in range(0, len(list1_sorted)):
    count += abs(list1_sorted[i] - list2_sorted[i])

print(count)
