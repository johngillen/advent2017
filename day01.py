f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    for a, b in [(line[i], line[i - 1]) for i in range(len(line))]:
        part1 += int(a) if a == b else 0
    for a, b in [(line[i], line[i - len(line) // 2]) for i in range(len(line))]:
        part2 += int(a) if a == b else 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
