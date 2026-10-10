from src import config as C


def evaluate(trucks, assignment):
    by_slot = {}
    waits = []
    scheduled = 0
    for t in trucks:
        s = assignment.get(t.id)
        if s is None:
            continue
        scheduled += 1
        by_slot.setdefault(s, []).append(t)
        waits.append((s - t.preferred) * C.SLOT_MINUTES)

    conflict_slots = 0
    blocked_until = 0
    vehicle_minutes_lost = 0.0

    for s in range(C.NUM_SLOTS):
        start = s * C.SLOT_MINUTES
        directions = {t.direction for t in by_slot.get(s, [])}
        if len(directions) >= 2:
            conflict_slots += 1
            blocked_until = max(blocked_until, start + C.BLOCKAGE_MINUTES)
        if start < blocked_until:
            delay = max(0, blocked_until - (start + C.SLOT_MINUTES / 2))
            vehicle_minutes_lost += C.bg_vehicles(s) * delay

    return {
        "trucks_scheduled": scheduled,
        "trucks_rejected": len(trucks) - scheduled,
        "conflict_slots": conflict_slots,
        "vehicle_minutes_lost": round(vehicle_minutes_lost),
        "avg_truck_wait_min": round(sum(waits) / len(waits), 1) if waits else 0,
    }