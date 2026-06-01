import read_input

pos = 50
count0 = 0
for w in read_input.read("2025_1.txt") :
    if w[0] == 'R' :
        pos = (pos + int(w[1:])) % 100
    else:
        pos = pos - (int(w[1:]) % 100)
        if pos < 0 :
            pos = 100 + pos
    if pos == 0 :
        count0 += 1

print(count0)



