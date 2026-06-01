from asyncio import coroutines
from asyncio import proactor_events
from asyncio import base_subprocess
from encodings.punycode import T
from asyncio import coroutines
import read_input

grid = read_input.read_all_lines_as_listlistint("2021_11.txt")
#grid = read_input.read_all_lines_as_listlistint("test_values.txt")

def flash(grid, pos_x, pos_y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:

            nx = pos_x + dx
            ny = pos_y + dy

            if dx == 0 and dy == 0:
                 grid[nx][ny] = -10

            # Vérifie les limites
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                grid[nx][ny] += 1
    return grid

def return_to_zero(grid) :
    count_nb_zero = 0
    for i in range(len(grid)):  
        for j in range(len(grid[i])):
            if grid[i][j]<0 :
                grid[i][j] = 0
                count_nb_zero +=1

    somme = (sum(grid[0])+sum(grid[1])+sum(grid[2])+sum(grid[3])+sum(grid[4])
    +sum(grid[5])+sum(grid[6])+sum(grid[7])+sum(grid[8])+sum(grid[9]))
    print(f"Sum {somme}")
    return count_nb_zero

count = 0

for step in range(0,100):

    for i in range(len(grid)):  
        for j in range(len(grid[i])):
            grid[i][j] += 1

    
    while True:
        prev_count = count
        for i in range(len(grid)):  
            for j in range(len(grid[i])):
                if grid[i][j]>=10 :
                    count += 1
                    grid = flash(grid, i, j)
        if prev_count == count:
            break

    if return_to_zero(grid) == 100 :
        print(f"All zeros {step}")
        #break #Pour part 2 après avoir set step jusque 1000
    print(grid)

print(grid)
print(count)  
##TOO HIGH
    

