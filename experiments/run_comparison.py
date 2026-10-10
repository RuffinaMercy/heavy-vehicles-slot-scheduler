from src.generator import generate_requests
from src import baseline_no_control
from src.metrics import evaluate


def main():
    trucks = generate_requests()
    print(f"Generated {len(trucks)} truck requests\n")

    result = evaluate(trucks, baseline_no_control.run(trucks))
    print("NO CONTROL")
    for key, value in result.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()