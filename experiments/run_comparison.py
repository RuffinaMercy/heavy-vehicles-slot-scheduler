from src.generator import generate_requests
from src import baseline_no_control, baseline_hard_ban, scheduler
from src.metrics import evaluate


def show(name, result):
    print(name)
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()


def main():
    trucks = generate_requests()
    print(f"Generated {len(trucks)} truck requests\n")
    show("NO CONTROL", evaluate(trucks, baseline_no_control.run(trucks)))
    show("HARD BAN 07:30-09:30", evaluate(trucks, baseline_hard_ban.run(trucks)))
    show("SLOT SCHEDULER", evaluate(trucks, scheduler.run(trucks)))


if __name__ == "__main__":
    main()