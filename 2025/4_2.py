import read_input


data = read_input.read_all_lines("2025_4.txt")
#data = read_input.read_all_lines("test_values.txt")

def is_pos_a_symbol(char : str = ""):
    return char == "@"

def count_surround(cur :str,  pos:int, prev : str, next:str = ""):
    quant = 0
    for i in range (-1, 2, 1):
        if pos == 0 and i == -1 :
            continue
        try :
            if is_pos_a_symbol(prev[pos + i]):
                quant += 1
        except :
            #Erreur si prev = "" parce que current = 1er ligne    
            pass

        try :
            if is_pos_a_symbol(next[pos + i]):
                quant += 1
        except :
            #Erreur si next = "" parce que current = dernière ligne
            pass

    if pos != 0:
        if is_pos_a_symbol(current[pos - 1]):
            quant += 1
 
    try:
        if is_pos_a_symbol(current[pos + 1]):
            quant += 1
    except :
        #Erreur pos +1 si pos = dernier caractère donne une index erreur
        pass

    return quant

removed_total = 0

new_data : list[str] = []

while True :
    removed_current = 0 
    for i in range(0,len(data)):

        #print(data)

        previous : str = ""
        current :str = ""
        next: str = ""

        current = data[i]
        if i != 0:
            previous = data[i-1]
        if i < len(data)-1:
            next = data[i+1]

        new_line = current

        pos_symbol = 0
        for symbol in current :
            if symbol == "@":
                if  count_surround(current,pos_symbol,previous, next) < 4 :
                    liste_temp = list(new_line) 
                    liste_temp[pos_symbol] = "."
                    new_line = "".join(liste_temp) 
                    removed_current += 1

            pos_symbol+=1

        data[i] = (new_line)

    if removed_current == 0 :
        break
    else :
        removed_total += removed_current

print(removed_total)



