import read_input

lines =  read_input.read_all_lines_with_spaces("2025_6.txt")
# lines =  read_input.read_all_lines_with_spaces("test_values.txt") 
#print(lines)
longueur = len(lines[0])

total = 0
list_nb =[]
for i in range(1,longueur+1,1):
    result = 0
    nb = ''

    for line in lines[:-1]:
        nb+=line[-i]
    cleaned = nb.strip()
    if cleaned != '':
        list_nb.append(nb)

    if lines[-1][-i] == '+':
        for val in list_nb :
            result = result + int(val)
        list_nb.clear()
    elif lines[-1][-i] == '*' :
        result = 1
        for val in list_nb :
            result = result * int(val)
        list_nb.clear()
            
    total += result
    
print(total)
# operators = values.pop()

# # print(values)
# # print(operators)
# nb_calcul = len(operators)

# for i in range(0, nb_calcul):
#     val = 0
#     for nombres in values:
#         current = int(nombres[i])
#         if operators[i]  == '+':
#             val = val + current
#         else :
#             if val == 0 : val = 1
#             val = val * current

#     total += val


# print(total)
