import argparse
import math
import random

from tqdm import tqdm


def f(base: float, x: float) -> float:
    return base**x


def df(base: float, x: float) -> float:
    return base**x * math.log(base)


def estimate_e(
    iterations: int = 100,
    samples: int = 8,
    start_base: float = 6.0,
    start_delta: float = 0.5,
    seed: int | None = None,
) -> float:
    if seed is not None:
        random.seed(seed)

    base = start_base
    delta = start_delta
    last_jump_directions: list[int] = []

    for _ in tqdm(range(iterations), desc="derivative-search", unit="iter"):
        total_error = 0.0
        for _ in range(samples):
            sample_x = random.uniform(0.1, 10.0)
            total_error += df(base, sample_x) - f(base, sample_x)

        # If derivative > function, shrink base; otherwise grow it.
        if total_error > 0:
            base -= delta
            last_jump_directions.append(-1)
        elif total_error < 0:
            base += delta
            last_jump_directions.append(1)
        else:
            break

        if len(last_jump_directions) > 3:
            last_jump_directions = last_jump_directions[-3:]

        if len(last_jump_directions) == 3:
            ljd = last_jump_directions
            if ljd[0] == ljd[2] and ljd[0] != ljd[1]:
                delta *= 0.5

    return base


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Approximate e by matching f(x)=b^x with its derivative."
    )
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--samples", type=int, default=8)
    parser.add_argument("--start-base", type=float, default=6.0)
    parser.add_argument("--start-delta", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    approximation = estimate_e(
        iterations=args.iterations,
        samples=args.samples,
        start_base=args.start_base,
        start_delta=args.start_delta,
        seed=args.seed,
    )
    print(approximation)


if __name__ == "__main__":
    main()
