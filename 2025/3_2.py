import read_input

def max_in(chaine, start = 0, retrait = 0):
    fin = len(chaine) - retrait

    fenetre = chaine[start:fin]
    print(chaine, start, retrait, fenetre)
    meilleur_v = max(fenetre)
    position_reelle = chaine.find(meilleur_v, start)
    return meilleur_v,position_reelle


nb_str: str = ''
sum_volt = 0
for w in read_input.read_multiple_lines("2025_3.txt") :
#for w in read_input.read_multiple_lines("test_values.txt") :
    print(w)
    
    nb_str = ''
    s_modifiee = w
    pos  = 0
    for i in range(12) :
        reste_a_prendre = 11 - i
        chiffre, pos = max_in(w, pos, reste_a_prendre)

        nb_str += chiffre
        pos +=1
        if(len(nb_str) == 12):
            break
        print(nb_str)

    print(nb_str)
    sum_volt += int(nb_str)
    print(sum_volt)

print(sum_volt)
    


    
    # for i in range(0, len(str(w))-10):
    #     print(w[i:i+10])
#         after = w[i+1:]
#         if after != "":
#             max_after = max(after)

#             concat = int(w[i]+max_after)
#             if concat > max_volt :
#                 max_volt = concat

#     sum_volt += max_volt
# print(sum_volt)


