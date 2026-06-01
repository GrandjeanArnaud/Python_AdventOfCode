import read_input

data = read_input.read_all_lines("2025_5.txt")
#data = read_input.read_all_lines("test_values.txt")

idx = data.index('')
stocks = data[:idx]
ingredients = data[idx + 1:]
fresh = 0

for ingredient in ingredients :
    for stock in stocks:
        range_stock = stock.split("-")
        if int(ingredient) >= int(range_stock[0]) and int(ingredient) <= int(range_stock[1]) :
            fresh += 1
            break

print(fresh)
