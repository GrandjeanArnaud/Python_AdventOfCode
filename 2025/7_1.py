import read_input
lines = read_input.read_multiple_lines("2025_7.txt") 

liste_previous = list(next(lines, None))

print(''.join(liste_previous))

count_split = 0

for line in lines:
    liste_current = list(line)
    
    for i in range(0, len(liste_current)) :
        if liste_current[i] == '.' and (liste_previous[i] == 'S' or liste_previous[i] == '|'):
            liste_current[i] = "|"
        elif liste_current[i] == '^' and liste_previous[i] == '|':
            liste_current[i-1] = "|"
            liste_current[i+1] = "|"
            count_split += 1

    print(''.join(liste_current))
    liste_previous = liste_current
print(count_split)






