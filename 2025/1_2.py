import read_input

pos = 50
count0 = 0
for w in read_input.read_multiple_lines("2025_1.txt") :

    direction = w[0]
    steps = int(w[1:])

    for _ in range(steps):
        if direction == 'R':
            pos = (pos + 1) % 100
        else:  
            pos = (pos - 1) % 100

        if pos == 0:
            count0 += 1

print(count0)