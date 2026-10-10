# ---- Time ----
SLOT_MINUTES = 5
DAY_START = 6 * 60           # 06:00, in minutes after midnight
DAY_END = 12 * 60            # 12:00
NUM_SLOTS = (DAY_END - DAY_START) // SLOT_MINUTES   # 72 slots

# ---- Junction (rename these to match the real Kumbalgodu directions) ----
DIRECTIONS = ["TO_KANMANIKE", "TO_KENGERI", "SIDE_ROAD"]
MAX_TRUCKS_PER_SLOT = 2
BLOCKAGE_MINUTES = 15        # from your observation: 15-20 min

# ---- Background traffic reaching the junction per 5-min slot (assumed) ----
PEAK_START_SLOT = (8 * 60 - DAY_START) // SLOT_MINUTES        # 08:00
PEAK_END_SLOT = (9 * 60 + 30 - DAY_START) // SLOT_MINUTES     # 09:30
PEAK_VEHICLES = 30
OFFPEAK_VEHICLES = 10

# ---- Truck request generation ----
NUM_TRUCKS = 40              # trucks in the morning window
BURST_FRACTION = 0.6         # share of trucks arriving in bursts of 3-6
MIN_SLACK_SLOTS = 3          # deadline = preferred + 3..12 slots
MAX_SLACK_SLOTS = 12
SEED = 42


def time_to_slot(hour, minute):
    return ((hour * 60 + minute) - DAY_START) // SLOT_MINUTES


def slot_to_time(slot):
    t = DAY_START + slot * SLOT_MINUTES
    return f"{t // 60:02d}:{t % 60:02d}"


def bg_vehicles(slot):
    if PEAK_START_SLOT <= slot < PEAK_END_SLOT:
        return PEAK_VEHICLES
    return OFFPEAK_VEHICLES