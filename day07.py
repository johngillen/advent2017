f = open('input/day07.txt')
lines = [line.rstrip() for line in f.readlines()]

def weightsum(node):
    if node in adj:
        weight[node] += sum(weightsum(child) for child in adj[node])
    return weight[node]

adj = {line.split()[0]:line.split(' -> ')[1].split(', ') \
    for line in lines if ' -> ' in line}
weight = {line.split()[0]:int(line.split()[1][1:-1]) \
    for line in lines}

part1 = [node for node in adj if node not in sum(adj.values(), [])][0]
part2 = weightsum(part1)

for children in adj.values():
    weights = [weight[c] for c in children]
    if len(set(weights)) > 1:
        unbalanced = min(weights, key=weights.count)
        balanced = max(weights, key=weights.count)
        program = children[weights.index(unbalanced)]

        part2 = weight[program] - sum([weight[c] for c in adj[program]]) \
            + (balanced - unbalanced)
        break


print(f'part 1: {part1}')
print(f'part 2: {part2}')
