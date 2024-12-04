import re

with open("day_3\problem2\input.txt", "r") as file:
    
    instructions = ""
    
    for line in file:
        instructions += line

# RegEx pattern
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_pattern = r"(do\(\)|don't\(\))"

# split string in parts based on control pattern
parts = re.split(control_pattern, instructions)

# Track if we are inside do() or don't() area
enabled = True
count = 0

for part in parts:
    part = part.strip()
    
    if part == "do()":
        enabled = True
    elif part == "don't()":
        enabled = False
    elif enabled:
        # find all the mul(X,Y) matches in this input part
        matches = re.findall(mul_pattern, part)
        # multiply for each pair and add to count
        for x, y in matches:
            count += int(x) * int(y)


print(count)
