class FirstOpenTree:
    """Segment tree over slots. Leaf = 1 if open, 0 if closed.
    Finds the first open slot at or after a position in O(log T)."""

    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i in range(n):
            self.tree[self.size + i] = 1
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        i = pos + self.size
        self.tree[i] = value
        i //= 2
        while i >= 1:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def first_open(self, start):
        """First index >= start with value 1, or -1 if none."""
        if start >= self.n:
            return -1
        return self._find(1, 0, self.size - 1, start)

    def _find(self, node, lo, hi, start):
        if hi < start or self.tree[node] == 0:
            return -1
        if lo == hi:
            return lo if lo < self.n else -1
        mid = (lo + hi) // 2
        left = self._find(2 * node, lo, mid, start)
        if left != -1:
            return left
        return self._find(2 * node + 1, mid + 1, hi, start)