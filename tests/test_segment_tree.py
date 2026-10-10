import random
from src.segment_tree import FirstOpenTree


def brute_force(values, start):
    for i in range(start, len(values)):
        if values[i] == 1:
            return i
    return -1


def test_matches_brute_force():
    rng = random.Random(1)
    n = 72
    tree = FirstOpenTree(n)
    values = [1] * n
    for _ in range(500):
        pos = rng.randrange(n)
        val = rng.randint(0, 1)
        tree.update(pos, val)
        values[pos] = val
        start = rng.randrange(n)
        assert tree.first_open(start) == brute_force(values, start)