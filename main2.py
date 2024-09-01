import math

from tqdm import tqdm

NUM_ITERS = 100
denominator = 1

total = 0
for i in tqdm(range(NUM_ITERS)):
    total += 1 / denominator
    print(denominator)
    denominator *= i + 1

print(total)
# 2.7182818284590455
