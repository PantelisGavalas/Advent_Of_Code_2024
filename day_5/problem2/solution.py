with open('day_5\problem2\input.txt', mode='r') as file:
    
    rules_list = []
    updates = []
    empty_line_passed = False
    
    for line in file:
        if line == "\n":
            empty_line_passed = True
        elif not empty_line_passed:
            rules_list.append(line.split('|'))
        elif empty_line_passed:
            updates.append(line.split(','))

# Get the rules in a set of tuples
for rule in rules_list:
    rule[0] = int(rule[0])
    rule[1] = int(rule[1][:len(rule[1])-1])
rules = {(x,y) for x,y in rules_list}

# Get update sequences in a list of lists
for update in updates:
    update[-1] = update[-1][:len(update[-1])-1]
    for i in range(0, len(update)):
        update[i] = int(update[i])
        
# Logic to keep only invalid updates 
bad_updates = []
for update in updates:
    update_validity = True
    for i in range(len(update)-1, 0, -1):
        for j in range(i, -1, -1):
            if (update[i], update[j]) in rules:
                update_validity = False
                
    if not update_validity:
        bad_updates.append(update)

# Logic to fix the bad updates
def swap_rules(update, rule_i, rule_j):
    temp = update[rule_i]
    update[rule_i] = update[rule_j]
    update[rule_j] = temp
    return update

def check_for_swap(update):
    for i in range(len(update)-1, 0, -1):
        for j in range(i, -1, -1):
            if (update[i], update[j]) in rules:
                swaped_update = swap_rules(update, i, j)
                return check_for_swap(swaped_update)
    return update

count = 0
for update in bad_updates:
    fixed_update = check_for_swap(update)
    count += fixed_update[int(len(fixed_update)/2)]

print(count)