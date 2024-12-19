import sys

sys.setrecursionlimit(10**6)

with open('day_6\\problem1\\input.txt', mode='r') as file:
    lab_map = []

    for line in file:
        lab_map.append(list(line))
    for line in lab_map:
        line[:] = line[:len(line)-1]


def guard_start(lab_map):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] == 'v':
                return [i,j], 'v'
            elif lab_map[i][j] == '>':
                return [i,j], '>'
            elif lab_map[i][j] == '<':
                return [i,j], '<'
            elif lab_map[i][j] == '^':
                return [i,j], '^'
    

def movement(guard_pos, guard_orient, lab_map):
    # Check if guard leaves the map
    if (guard_orient == 'v') and (guard_pos[0] == len(lab_map)-1) :
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        return
    elif (guard_orient == '^') and (guard_pos[0] == 0) :
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        return
    elif (guard_orient == '<') and (guard_pos[1] == 0) :
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        return
    elif (guard_orient == '>') and (guard_pos[1] == len(lab_map[guard_pos[0]])) :
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        return
    
    # Check if guard needs to turn
    if (guard_orient == 'v') and (lab_map[guard_pos[0]+1][guard_pos[1]] == '#') :
        guard_orient = '<'
    elif (guard_orient == '<') and (lab_map[guard_pos[0]][guard_pos[1]-1] == '#') :
        guard_orient = '^'
    elif (guard_orient == '^') and (lab_map[guard_pos[0]-1][guard_pos[1]] == '#') :
        guard_orient = '>'
    elif (guard_orient == '>') and (lab_map[guard_pos[0]][guard_pos[1]+1] == '#') :
        guard_orient = 'v'
    
    # Movement of guard
    if (guard_orient == 'v'):
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        guard_pos[0] += 1 
    elif (guard_orient == '<'):
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        guard_pos[1] -= 1
    elif (guard_orient == '^'):
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        guard_pos[0] -= 1
    elif (guard_orient == '>'):
        lab_map[guard_pos[0]][guard_pos[1]] = 'X'
        guard_pos[1] += 1
        
    movement(guard_pos, guard_orient, lab_map)
        
    

guard_pos, guard_orient = guard_start(lab_map)
# print(guard_pos, '  |  ', guard_orient, '\n')

movement(guard_pos, guard_orient, lab_map)
# for line in lab_map:
#     print(''.join(line))
# print()

count = 0
for line in lab_map:
    for item in line:
        if item == 'X':
            count += 1
print(count)
