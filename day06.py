f = open('input/day06.txt')
lines = [line.rstrip() for line in f.readlines()]

from re import findall

part1 = 0
part2 = 0

seen = []
n = list(map(int, findall(r'-?\d+', lines[0])))

def redistribute(n):
    i = n.index(max(n))
    m, n[i] = n[i], 0
    for j in range(m):
        n[(i + j + 1) % len(n)] += 1

while seen.count(tuple(n)) < 1:
    seen.append(tuple(n))
    redistribute(n)
    part1 += 1

while seen.count(tuple(n)) < 2:
    seen.append(tuple(n))
    redistribute(n)
    part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
