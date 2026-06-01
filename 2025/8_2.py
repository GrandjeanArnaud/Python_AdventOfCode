import posixpath
import read_input

lines = read_input.read_all_lines("2025_8.txt") 

positions: dict[int, str] = {}
counter = 1
for item in lines:
    positions.update({counter: item})
    counter += 1

distances : dict[str,int] = {}
for item1 in positions.items():
    for item2 in positions.items():
        if item2[0] < item1[0]:
            continue
        pos1 = [int(item1[1].split(',')[0]), int(item1[1].split(',')[1]), int(item1[1].split(',')[2])]
        pos2 = [int(item2[1].split(',')[0]), int(item2[1].split(',')[1]), int(item2[1].split(',')[2])]
        distance = (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2

        key = ''
        if item1[0] < item2[0]:
            key =  f"{item1[0]}:{item2[0]}"
        elif item1[0] > item2[0]:
            key = f"{item2[0]}:{item1[0]}"
        else :
            continue

        if key in distances:
            continue
        else:
            distances.update({key: distance })


ordered_distances = sorted(distances.items(), key=lambda x: x[1])
print(len(ordered_distances))

list_of_junctions = [[]]

set_points: set[int] = set()
i = 0
while(True):
    key = ordered_distances[i][0]
    key0 = key.split(":")[0]
    key1 = key.split(":")[1]
    added = False
    
    for sublist in list_of_junctions:
        if(
            any(key0 in item.split(":") for item in sublist)
            or any(key1 in item.split(":") for item in sublist)
        ) :
            if added:
                for item in sublist:
                    mem.append(item)
                sublist.clear()
                continue
            sublist.append(key)
            added=True
            mem = sublist
        
    if not added :
        list_of_junctions.append([key]) 

    sorted_lists = sorted(list_of_junctions, key=len, reverse=True)

    i+=1

    set_points.clear()
    count = 0
    for item in sorted_lists[0]:
        set_points.add(item.split(":")[0])
        set_points.add(item.split(":")[1])
    count = len(set_points)   
    
    if count==1000:
        print(key0)
        print(key1)
        x0 = int(positions[int(key0)].split(",")[0])
        x1 = int(positions[int(key1)].split(",")[0])    
        print(x0)
        print(x1)
        print(x0*x1)
        break
 
