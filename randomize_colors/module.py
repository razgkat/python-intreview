import random


def run_estimated(count: int):
    colors = ['blue', 'yellow', 'green', 'red']
    probs = [0.3, 0.4, 0.1, 0.2]

    n = count

    # We aggregate the probabilities
    percents = []
    for i, p in enumerate(probs):
        if i == 0:
            percents.append((probs[i], colors[i]))
        else:
            percents.append((probs[i] + percents[i-1][0], colors[i]))

    counts = {
        'blue': 0,
        'yellow': 0,
        'green': 0,
        'red': 0
    }

    for i in range(0, n):
        rand = random.random()
        for x in percents:
            if rand <= x[0]:
                # print(x[1])
                counts[x[1]] += 1
                break

    print(("Actual Counts (Estimated): %s" % str(counts)))


def run_iterative(count: int):
    colors = ['blue', 'yellow', 'green', 'red']
    probs = [0.3, 0.4, 0.1, 0.2]

    n = count

    # We count by probabilities the probabilities
    counts = [n*p for p in probs]

    print(("Expected Counts: %s" % counts))
    total = 1

    counts_dict = {}
    for c in colors:
        counts_dict[c] = 0

    while total <= n:
        idx = random.randint(0, len(colors) - 1)
        # print(colors[idx])
        counts_dict[colors[idx]] += 1
        counts[idx] -= 1
        if counts[idx] == 0:
            colors.remove(colors[idx])
            counts.pop(idx)
        total += 1

    print(("Actual Counts (Iterative): %s" % counts_dict))


def run(method: str, count: int):
    if method == 'estimated':
        run_estimated(count)
    if method == 'iterative':
        run_iterative(count)
