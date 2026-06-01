import read_input

data = str(read_input.read_one_line("2025_2.txt"))
#data = str(read_input.read_one_line("test_values.txt"))

data_list = data.split(",")
sum = 0

for duos in data_list:
    values = duos.split("-")
    for id in range(int(values[0]), int(values[1])+1):
        lenstr = len(str(id))
        if(lenstr % 2 == 1):
            continue
        else :
            mid = lenstr//2
            if str(id)[:mid] == str(id)[mid:] :
                sum += id

print(sum)

