import os
from functools import reduce

ROTATION_ORDER = [(1, 0), (0, -1), (-1, 0), (0, 1)]

x = lambda vec: vec[0]
y = lambda vec: vec[1]
iter_commands = lambda input: (command.strip() for command in input.split(','))
rotate = lambda rotation, direction: ROTATION_ORDER[(ROTATION_ORDER.index(rotation) + direction) % len(ROTATION_ORDER)]
move = lambda position, rotation, distance: (x(position) + x(rotation) * distance, y(position) + y(rotation) * distance)
apply_position = lambda state, command: {**state, 'position': move(state['position'], state['rotation'], int(command[1:]))}
apply_rotation = lambda state, command: {**state, 'rotation': rotate(state['rotation'], (1 if command[0] == 'R' else -1))}
apply_command = lambda state, command: apply_position(apply_rotation(state, command), command)
reduce_state = lambda input: reduce(apply_command, iter_commands(input), {"position": (0, 0), "rotation": (0, 1)})
measure_distance = lambda position: abs(x(position)) + abs(y(position))
resolve = lambda input: measure_distance(reduce_state(input)['position'])


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as input:
        print(resolve(input.read()))