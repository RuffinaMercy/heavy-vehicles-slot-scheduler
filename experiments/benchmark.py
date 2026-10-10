import random
import time
from src.segment_tree import FirstOpenTree


def naive_first_open(values, start):
    for i in range(start, len(values)):
        if values[i]:
            return i
    return -1


def bench(n, queries=2000):
    # Worst case: only the last slot is open, so a scan walks the whole array.
    values = [0] * n
    values[n - 1] = 1
    tree = FirstOpenTree(n)
    for i in range(n - 1):
        tree.update(i, 0)
    rng = random.Random(1)
    starts = [rng.randrange(n // 2) for _ in range(queries)]

    t0 = time.perf_counter()
    a = [naive_first_open(values, s) for s in starts]
    t1 = time.perf_counter()
    b = [tree.first_open(s) for s in starts]
    t2 = time.perf_counter()

    assert a == b, "tree and naive scan disagree"
    print(f"T={n:>7}: naive {(t1 - t0) * 1000:9.1f} ms | segment tree {(t2 - t1) * 1000:9.1f} ms")

if __name__ == "__main__":
    for n in (72, 1_000, 10_000, 100_000):
        bench(n)