import read_input

data = str(read_input.read_one_line("2025_2.txt"))
#data = str(read_input.read_one_line("test_values.txt"))

data_list = data.split(",")
sum = 0
setnb = set()
for duos in data_list:
    values = duos.split("-")
    
    for id in range(int(values[0]), int(values[1])+1):
        s = str(id)
        L = len(s)  
        
        for size in range(1, L // 2 + 1):
            if L % size == 0:
                pattern = s[:size]
                
                if pattern * (L // size) == s:
                    setnb.add(id)
        
for val in setnb:
    sum+= val
print(sum)



