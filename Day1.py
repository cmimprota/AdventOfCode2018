# PART 1
with open("Day1input.txt") as f:
    input = f.readlines()
frequency = sum(map(int, input))
print(frequency)

# PART 2
frequency = 0
frequencies = set()
#input = list(map(int, input))
while True:
    for i in input:
        if frequency in frequencies:
            print(frequency)
            exit(0)
        frequencies.add(frequency)
        frequency += int(i)





