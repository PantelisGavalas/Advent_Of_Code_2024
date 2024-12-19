import sys
import copy

sys.setrecursionlimit(10**6)

with open('day_6\\problem2\\input.txt', mode='r') as file:
    lab_map = []

    for line in file:
        lab_map.append(list(line))
    for line in lab_map:
        line[:] = line[:len(line)-1]

map_rows = len(lab_map)
map_columns = len(lab_map[0])
# print(map_rows * map_columns)


# Get starting position and orientation of the guard
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
                 
                 
# Movement of the guard
def movement(guard_positions, guard_pos, guard_orient, lab_map):
    # Check if guard leaves the map => No loop 
    if (guard_orient == 'v') and (guard_pos[0] == map_rows-1) :
        return 0
    elif (guard_orient == '^') and (guard_pos[0] == 0) :
        return 0
    elif (guard_orient == '<') and (guard_pos[1] == 0) :
        return 0
    elif (guard_orient == '>') and (guard_pos[1] == map_columns-1) :
        return 0
    else:
        # Check if guard needs to turn or walk
        if (guard_orient == 'v') and (lab_map[guard_pos[0]+1][guard_pos[1]] == '#') :
            guard_orient = '<'
        elif (guard_orient == '<') and (lab_map[guard_pos[0]][guard_pos[1]-1] == '#') :
            guard_orient = '^'
        elif (guard_orient == '^') and (lab_map[guard_pos[0]-1][guard_pos[1]] == '#') :
            guard_orient = '>'
        elif (guard_orient == '>') and (lab_map[guard_pos[0]][guard_pos[1]+1] == '#') :
            guard_orient = 'v'
        else:
            # Movement of guard
            if (guard_orient == 'v'):
                guard_pos[0] += 1 
            elif (guard_orient == '<'):
                guard_pos[1] -= 1
            elif (guard_orient == '^'):
                guard_pos[0] -= 1
            elif (guard_orient == '>'):
                guard_pos[1] += 1
        
        # Check if new guard position is repeated => Loop
        if (guard_pos[0], guard_pos[1], guard_orient) in guard_positions:
            return 1
        else:
            # Add new guard position to positions and move again
            guard_positions.add((guard_pos[0], guard_pos[1], guard_orient)) 
            # print(guard_pos[0], guard_pos[1], guard_orient)
            return movement(guard_positions, guard_pos, guard_orient, lab_map)
    

# Get starting guard position
starting_pos, starting_orient = guard_start(lab_map)

# Create a set to hold guard positions --> (position X, position Y, orientation)
positions = set()

# Check obstancle in any postition
obstacle_count = 0
for i in range (0, map_rows):
    for j in range(0, map_columns):
        if [i,j] != starting_pos:
            new_lab_map = copy.deepcopy(lab_map)
            new_lab_map[i][j] = '#'
            # print('\n---------------------')
            # for line in new_lab_map:
            #     print(''.join(line))
            # print('---------------------\n')
            
            positions.add((starting_pos[0], starting_pos[1], starting_orient))
            guard_pos = copy.deepcopy(starting_pos)
            guard_orient = starting_orient
            # print('We are on: ', i, j)
            # print(guard_pos[0], guard_pos[1], guard_orient)
            obstacle_count += movement(positions, guard_pos, guard_orient, new_lab_map)
            # print('obstacle_count = ', obstacle_count, '\n\n\n')
            positions.clear()

print(obstacle_count)
