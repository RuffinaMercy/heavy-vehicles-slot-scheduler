import random
from dataclasses import dataclass
from src import config as C


@dataclass
class Truck:
    id: int
    direction: str
    preferred: int    # slot the truck wants to pass
    deadline: int     # latest slot it can accept


def _make_truck(rng, tid, preferred):
    preferred = min(preferred, C.NUM_SLOTS - 1)
    slack = rng.randint(C.MIN_SLACK_SLOTS, C.MAX_SLACK_SLOTS)
    deadline = min(preferred + slack, C.NUM_SLOTS - 1)
    return Truck(tid, rng.choice(C.DIRECTIONS), preferred, deadline)


def generate_requests(n=C.NUM_TRUCKS, seed=C.SEED):
    rng = random.Random(seed)
    trucks = []
    n_burst = int(n * C.BURST_FRACTION)
    first = C.time_to_slot(8, 0)
    last = C.time_to_slot(9, 25)

    # Bursts: 3-6 trucks arriving within about 10 minutes
    while len(trucks) < n_burst:
        size = min(rng.randint(3, 6), n_burst - len(trucks))
        center = rng.randint(first, last)
        for _ in range(size):
            trucks.append(_make_truck(rng, len(trucks), center + rng.randint(0, 1)))

    # The rest are spread through the day
    while len(trucks) < n:
        trucks.append(_make_truck(rng, len(trucks), rng.randint(0, C.NUM_SLOTS - 1)))

    return trucks