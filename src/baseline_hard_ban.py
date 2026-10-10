from src import config as C


def run(trucks):
    """Trucks are banned from BAN_START to BAN_END. A banned truck waits until
    the ban ends. If its deadline is earlier than that, it is rejected."""
    assignment = {}
    for t in trucks:
        s = t.preferred
        if C.BAN_START_SLOT <= s < C.BAN_END_SLOT:
            s = C.BAN_END_SLOT
        if s > t.deadline:
            continue                      # cannot wait that long
        assignment[t.id] = s
    return assignment