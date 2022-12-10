f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    line = sorted(list(map(int, line.split())))
    part1 += line[-1] - line[0]
    part2 += next(a // b for a in line for b in line if a != b and a % b == 0)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
