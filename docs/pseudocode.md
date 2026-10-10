# Pseudocode

## Data structures
- Min-heap of requests, keyed by deadline
- Array slot_dir[T] and slot_count[T] (direction and truck count per slot)
- One segment tree per direction; leaf = 1 if the slot is open for that direction

## Algorithm: Schedule(trucks)

    heap = MinHeap(trucks, key = deadline)
    FOR each direction d: tree[d] = SegmentTree(T, all leaves = 1)

    WHILE heap is not empty:
        t = heap.ExtractMin()                          // O(log R)
        s = tree[t.direction].FirstOpen(t.preferred)   // O(log T)
        IF s == NONE OR s > t.deadline:
            reject(t)
            CONTINUE
        slot_dir[s] = t.direction
        slot_count[s] = slot_count[s] + 1
        assign(t, s)
        FOR each direction d:                          // O(D log T)
            open = (slot_dir[s] == d) AND (slot_count[s] < MAX_TRUCKS)
            tree[d].Update(s, open)

## FirstOpen(start)
Descend the tree; skip any subtree whose max is 0 or which lies entirely
before `start`; return the leftmost leaf with value 1.

## Complexity
| Operation | Time |
|---|---|
| Heap push / pop | O(log R) |
| FirstOpen | O(log T) |
| Book one truck (D directions) | O(D log T) |
| Whole batch of R trucks | O(R log R + R D log T) |
| Naive scan alternative | O(R * T) |
| Space | O(D * T + R) |

## Design justification
- Heap: serves the most urgent truck first, so tight deadlines are not starved.
- Segment tree: answers "first open slot for this direction after time x" without scanning.
- One tree per direction: a slot's openness depends on the truck's direction.
- Array: O(1) access to slot state.