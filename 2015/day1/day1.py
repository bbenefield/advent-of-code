with open('2015/day1/day1input.txt', 'r') as fin:
    data = fin.readline()

# Part A
move_up: int = data.count("(")
move_down: int = data.count(")")

print(f'Move up: {move_up}')
print(f'Move down: {move_down}')
print(f'Final: {move_up - move_down}')

# Part B
floor: int = 0

for idx, char in enumerate(data):
    if floor < 0:
        print(f'Position: {idx}')
        break
        
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
        