import read_input
import os
from collections import defaultdict

## AI SOLUTION##

grid = read_input.read_all_lines("2025_7.txt")
# grid = read_input.read_all_lines("test_values.txt")

# Dimensions de la grille
H = len(grid)
W = len(grid[0])

# Trouver la position de départ S
start_col = grid[0].index("S")

# Dictionnaire :
# clé   = colonne
# valeur = nombre de timelines arrivant à cette colonne
current = {start_col: 1}

# On parcourt chaque ligne APRÈS celle contenant S
for r in range(1, H):

    # Contiendra les timelines de la ligne suivante
    next_positions = defaultdict(int)

    # Pour chaque colonne actuellement atteinte
    for c, ways in current.items():

        # Si on sort de la grille, on ignore
        if c < 0 or c >= W:
            continue

        cell = grid[r][c]

        # Cas 1 : espace vide
        # La particule continue tout droit
        if cell == ".":
            next_positions[c] += ways

        # Cas 2 : splitter
        # La timeline se divise en deux
        elif cell == "^":
            next_positions[c - 1] += ways
            next_positions[c + 1] += ways

    # Passer à la ligne suivante
    current = next_positions

# Le nombre total de timelines
answer = sum(current.values())

print(answer)





