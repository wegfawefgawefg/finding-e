import random
import math

from tqdm import tqdm


def f(base, x):
    return base**x


def df(base, x):
    return base**x * math.log(base)


NUM_ITERS = 100
NUM_SAMPLES = 8
base = 6
delta = 0.5
last_jump_directions = []

for i in tqdm(range(NUM_ITERS)):
    total_error = 0
    for si in range(NUM_SAMPLES):
        sample_x = random.uniform(0.1, 10.0)
        f_out = f(base, sample_x)
        d_out = df(base, sample_x)
        total_error += d_out - f_out

    # if the derivative is bigger, shrink the base
    # if the derivative is smaller, grow the base
    if total_error > 0:
        base -= delta
        last_jump_directions.append(-1)
    elif total_error == 0:
        break
    elif total_error < 0:
        base += delta
        last_jump_directions.append(1)

    if len(last_jump_directions) > 3:
        last_jump_directions = last_jump_directions[-3:]

    if len(last_jump_directions) == 3:
        ljd = last_jump_directions
        # if we jumped down, then up, then down - or - up, then down, then up
        # ex: [1,-1, 1] or [-1, 1, -1]
        if ljd[0] == ljd[2] and ljd[0] != ljd[1]:
            delta *= 0.5

print(base)
# 2.7182818284590455
