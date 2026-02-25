import argparse

from tqdm import tqdm


def estimate_e(iterations: int = 100, show_terms: bool = False) -> float:
    denominator = 1
    total = 0.0

    for i in tqdm(range(iterations), desc="factorial-series", unit="iter"):
        total += 1 / denominator
        if show_terms:
            print(denominator)
        denominator *= i + 1

    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Approximate e by summing 1/n! using incremental factorials."
    )
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument(
        "--show-terms",
        action="store_true",
        help="Print each denominator term while iterating.",
    )
    args = parser.parse_args()

    approximation = estimate_e(iterations=args.iterations, show_terms=args.show_terms)
    print(approximation)


if __name__ == "__main__":
    main()
