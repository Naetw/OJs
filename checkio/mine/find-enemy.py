#!/usr/bin/env python3
# -*- coding: utf8 -*-

even = [(0, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
odd = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 0), (-1, -1)]
DIRECTIONS = [even, odd]
ABSOLUTE_DIR = ['N', 'NE', 'SE', 'S', 'SW', 'NW']
RELATIVE_DIR = ['F', 'R', 'R', 'B', 'L', 'L']

def check_boundary(position, right_side=True):
    # parameter right_side is for checking whether it's getting closer to enemy instead of the opposite direction
    return True if right_side and chr(position[0]).isupper() and chr(position[1]).isdigit() else False

def find_neighbor(position, right_or_left, fake_dir, off):
    x, y = position
    neighbors = []

    # range(2) since each side can only have two directions to choose except 'F' or 'B' and it will be checked later
    for idx in range(2):
        ''' 
            x%2 for judge it's on the even or odd column
            fake_dir is the offset of direction based on 'N' not based on the parameter dir
        '''
        dx, dy = DIRECTIONS[x%2][(fake_dir+idx)%6]

        if check_boundary((x+dx, y+dy), dx*right_or_left >= 0):
            neighbors.append((x+dx, y+dy))

    # if the real direction is 'F' or 'B', then add third direction for it
    if RELATIVE_DIR[fake_dir-off] in ['F', 'B']:
        dx, dy = DIRECTIONS[x%2][(fake_dir-1)%6]
        if check_boundary((x+dx, y+dy), dx*right_or_left >= 0):
            neighbors.append((x+dx, y+dy))

    return neighbors

def find_enemy(you, dir, enemy):
    
    start = list(map(ord, list(you)))
    end = tuple(map(ord, list(enemy)))
    
    # queue = [current_position, direction, step]
    queue = list()
    visited = set()

    # initialize queue
    flag_rl = 1 if end[0] >= start[0] else -1
    offset = ABSOLUTE_DIR.index(dir)

    # walk one step for four directions of left or right
    for i in range(4):
        dx, dy = DIRECTIONS[start[0]%2][i*flag_rl]

        if check_boundary((start[0]+dx, start[1]+dy)):
            queue.append([(start[0]+dx, start[1]+dy), (i*flag_rl-offset)%6, 1])

    while queue:
        current_position, init_direct, step = queue.pop(0)

        # enemy found
        if current_position == end:
            return [RELATIVE_DIR[init_direct], step]

        if current_position in visited:
            continue

        for neighbor in find_neighbor(current_position, flag_rl, (init_direct+offset)%6, offset):
            if neighbor not in visited and neighbor not in list(map(lambda x : x[0], queue)):
                queue.append([neighbor, init_direct, step+1])

        visited.add(current_position)


if __name__ == '__main__':
    assert find_enemy("A1","SW","Z9") == ['B', 25]
    assert find_enemy("C3","SE","A1") == ['B', 3]
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
