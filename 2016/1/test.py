import unittest
from resolve import (
    iter_commands,
    rotate,
    move,
    apply_command,
    reduce_state,
    resolve
)

class Tests(unittest.TestCase):
    def test_iter_commands(self):
        self.assertEqual(list(iter_commands('R2, L3')), ['R2', 'L3'])

    def test_rotate(self):
        self.assertEqual(rotate((1, 0), 1), (0, -1))
        self.assertEqual(rotate((1, 0), -1), (0, 1))

    def test_move(self):
        self.assertEqual(move((0, 0), (1, 0), 1), (1, 0))
        self.assertEqual(move((0, 0), (1, 0), 5), (5, 0))
        self.assertEqual(move((-1, 0), (1, 0), 5), (4, 0))
        self.assertEqual(move((0, -1), (0, 1), 5), (0, 4))

    def test_apply_command(self):
        self.assertEqual(apply_command({'position': (0, -1), 'rotation': (-1, 0)}, 'R5'), {'position': (0, 4), 'rotation': (0, 1)})

    def test_reduce_state(self):
        self.assertEqual(reduce_state('R5'), {'position': (5, 0), 'rotation': (1, 0)})

    def test_resolve(self):
        self.assertEqual(resolve('R5'), 5)
        self.assertEqual(resolve('R2, L3'), 5)
        self.assertEqual(resolve('R2, R2, R2'), 2)
        self.assertEqual(resolve('R5, L5, R5, R3'), 12)
        

if __name__ == '__main__':
    unittest.main()