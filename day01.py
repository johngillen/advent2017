f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

invalid = 0
for line in lines:
    words = line.split()
    for word in words:
        if words.count(word) > 1:
            invalid += 1
            break

part1 = invalid
part2 = 0


print(f'part 1: {part1}')
print(f'part 2: {part2}')
