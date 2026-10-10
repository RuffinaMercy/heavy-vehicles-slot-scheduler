import heapq
from src import config as C
from src.segment_tree import FirstOpenTree


def run(trucks):
    """Heap by deadline + one segment tree per direction.
    Returns {truck_id: slot}; rejected trucks are absent."""
    n = C.NUM_SLOTS
    trees = {d: FirstOpenTree(n) for d in C.DIRECTIONS}
    slot_dir = [None] * n
    slot_count = [0] * n

    heap = [(t.deadline, t.id, t) for t in trucks]
    heapq.heapify(heap)

    assignment = {}
    while heap:
        _, _, t = heapq.heappop(heap)
        s = trees[t.direction].first_open(t.preferred)
        if s == -1 or s > t.deadline:
            continue                      # no feasible slot
        slot_dir[s] = t.direction
        slot_count[s] += 1
        assignment[t.id] = s
        for d in C.DIRECTIONS:
            open_for_d = slot_dir[s] == d and slot_count[s] < C.MAX_TRUCKS_PER_SLOT
            trees[d].update(s, 1 if open_for_d else 0)
    return assignment