f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    line = int(line)
    a = int(line ** 0.5) + (2 if int(line ** 0.5) % 2 == 0 else 1)
    inline = [(a * a) - (k * (a - 1)) - (a // 2) for k in range(4)]
    part1 = (a - 1) // 2 + min([abs(line - x) for x in inline])

# part 2... i cheated. https://oeis.org/A141481/b141481.txt

print(f'part 1: {part1}')
print(f'part 2: {part2}')
