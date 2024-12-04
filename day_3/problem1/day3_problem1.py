import re

with open('day_3\problem1\day3_problem1_input.txt', "r") as file:
    
    instructions = []
    
    for line in file:
        instructions.append(line)

count = 0
# RegEx pattern
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = []

# find all the mul(X,Y) matches in the input 
for line in instructions:
    matches += re.findall(pattern, line)

# convert number strings to ints in the matches
matches_ints = []
for item in matches:
    matches_ints.append([int(item[0]), int(item[1])])

# multiply for each pair and add to count
for item in matches_ints:
    count += item[0] * item[1]

print(count)
