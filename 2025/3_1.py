import read_input

sum_volt = 0
for w in read_input.read_multiple_lines("2025_3.txt") :
#for w in read_input.read_multiple_lines("test_values.txt") :
#    print(w)
    max_volt = 0
    for i in range(0, len(str(w))):
        after = w[i+1:]
        if after != "":
            max_after = max(after)

            concat = int(w[i]+max_after)
            if concat > max_volt :
                max_volt = concat

    sum_volt += max_volt
print(sum_volt)


