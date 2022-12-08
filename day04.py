f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    words = line.split()
    for word in words:
        if words.count(word) > 1:
            part1 += 1
            break
    for word in words:
        if [sorted(w) for w in words].count(sorted(word)) > 1:
            part2 += 1
            break
                
part1 = len(lines) - part1
part2 = len(lines) - part2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
