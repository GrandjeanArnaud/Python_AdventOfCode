import read_input

data = read_input.read_all_lines("2025_5.txt")
#data = read_input.read_all_lines("test_values.txt")

idx = data.index('')
stocks = data[:idx]
ranges: list[list] = []


def adapt_borders(ranges, min_range,max_range):

    if ranges == []:
        ranges.append([min_range,max_range])
        
    else :
        has_aumented = False
        for borders in ranges : 
            if min_range == borders[0] and max_range == borders[1]:
                has_aumented = True
            if min_range < borders[0] and ((max_range >= borders[0] and max_range <= borders[1]) or max_range == borders[0]): #augment min border
                borders[0] = min_range
                has_aumented = True
            if max_range > borders[1] and ((min_range <= borders[1] and min_range >= borders[0]) or min_range == borders[1]): #augment min border
                borders[1] = max_range
                has_aumented = True
            if min_range < borders[0] and max_range > borders[1]: #replace range
                borders[0] = min_range
                borders[1] = max_range
                has_aumented = True
            
        if not has_aumented :
            ranges.append([min_range,max_range])


for stock in stocks:
    range_stock = stock.split("-")
    adapt_borders(ranges, int(range_stock[0]), int(range_stock[1]))

for _ in range(0, len(ranges)) :
    sub = ranges.pop(0)
    adapt_borders(ranges, sub[0], sub[1])

print(ranges)

total = 0
for pair in ranges :
    total = total + (pair[1] - pair[0]) +1 #+1 car soustraction inclusive ex 5-3 = 2 mais je veux 3, 4 ET 5

print(total)
