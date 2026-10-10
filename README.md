# Heavy Vehicle Slot Scheduler (Kumbalgodu Junction)

## Problem
During the 8-9:30 am school and college rush, heavy vehicles reach the Kumbalgodu
junction (Mysore Road) together, heading in different directions. On the narrow road
they block each other and the junction stands still for 15-20 minutes. This project
assigns each truck a 5-minute arrival slot so that no slot mixes directions.

## Method
Min-heap (deadline order) + one segment tree per direction (first open slot lookup)
+ slot arrays. See docs/pseudocode.md.

## Results (30 random seeds, simulated, assumed parameters)
| | No control | Hard ban | Slot scheduler |
|---|---|---|---|
| Conflict slots | 6.6 | 1.9 | 0 |
| Vehicle-minutes lost | 3095 | 423 | 0 |
| Trucks rejected (of 40) | 0 | 16.5 | 0 |
| Avg truck wait (min) | 0 | 11.4 (served trucks only) | 6.8 |

Worst-case lookup benchmark: naive scan 6267 ms vs segment tree 15 ms at T = 100,000.
The tree is slower at the real size (T = 72), so its benefit is at scale.

## Limitations
- Simulation, not real traffic data. Parameters are assumptions based on my daily commute.
- Trucks are assumed to follow assigned slots; enforcement is outside the model.
- The one-direction-per-slot rule is a simplified junction model.
- Bus waiting and crowding also contribute to peak-hour delay.

## Run
    pip install -r requirements.txt
    python -m experiments.run_comparison
    python -m experiments.multi_seed
    python -m experiments.benchmark
    python -m pytest