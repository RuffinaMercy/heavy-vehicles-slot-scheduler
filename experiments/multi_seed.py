import os
import matplotlib.pyplot as plt
from src.generator import generate_requests
from src import baseline_no_control, baseline_hard_ban, scheduler
from src.metrics import evaluate

SEEDS = range(1, 31)
METHODS = {
    "No control": baseline_no_control,
    "Hard ban": baseline_hard_ban,
    "Slot scheduler": scheduler,
}
KEYS = ["conflict_slots", "vehicle_minutes_lost", "trucks_rejected", "avg_truck_wait_min"]


def main():
    totals = {m: {k: 0.0 for k in KEYS} for m in METHODS}
    for seed in SEEDS:
        trucks = generate_requests(seed=seed)
        for name, module in METHODS.items():
            result = evaluate(trucks, module.run(trucks))
            for k in KEYS:
                totals[name][k] += result[k]

    avg = {m: {k: v / len(SEEDS) for k, v in d.items()} for m, d in totals.items()}
    for m, d in avg.items():
        print(m, {k: round(v, 1) for k, v in d.items()})

    os.makedirs("results", exist_ok=True)
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, k in zip(axes, KEYS):
        ax.bar(list(METHODS), [avg[m][k] for m in METHODS],
               color=["#d9534f", "#f0ad4e", "#5cb85c"])
        ax.set_title(k.replace("_", " "))
        ax.tick_params(axis="x", rotation=20)
    fig.suptitle(f"Average over {len(SEEDS)} random seeds (simulated, assumed parameters)")
    fig.tight_layout()
    fig.savefig("results/comparison.png", dpi=150)
    print("Saved results/comparison.png")


if __name__ == "__main__":
    main()