import read_input

total = 0
values : list[list] = []
for line in read_input.read_multiple_lines("2025_6.txt") :
#for line in read_input.read_multiple_lines("test_values.txt") :
    list = line.split(" ")
    list = [v for v in list if v != '']
    values.append(list)

operators = values.pop()

# print(values)
# print(operators)
nb_calcul = len(operators)

for i in range(0, nb_calcul):
    val = 0
    for nombres in values:
        current = int(nombres[i])
        if operators[i]  == '+':
            val = val + current
        else : 
            if val == 0 : val = 1
            val = val * current

    total += val


print(total)
        