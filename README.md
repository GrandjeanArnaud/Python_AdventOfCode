# 🎄 Advent of Code — Solutions en Python

Ce dépôt contient mes solutions en Python pour les défis annuels de l'**[Advent of Code](https://adventofcode.com/)**.

Chaque année est organisée dans son propre répertoire et contient les scripts de solution ainsi que les jeux de données d'entrée.

---

## 📂 Structure du Projet

Le projet est structuré par année :

```text
Python_AdventOfCode/
├── .gitignore
├── README.md
├── 2021/
│   ├── DataSets/
│   │   ├── 2021_11.txt
│   │   └── test_values.txt
│   ├── 11_1.py
│   └── read_input.py
└── 2025/
    ├── DataSets/
    │   └── 2025_1.txt
    ├── 1_1.py
    ├── 1_2.py
    │   ...
    └── read_input.py
```

- **`<Année>/`** : Contient les scripts pour une année spécifique (ex. `2021`, `2025`).
- **`DataSets/`** : Répertoire contenant les fichiers d'entrée (`.txt`) fournis par l'Advent of Code pour chaque défi.
- **`read_input.py`** : Module utilitaire pour lire et formater facilement les fichiers d'entrée depuis le sous-dossier `DataSets`.

---

## 🚀 Comment lancer une solution

Pour exécuter un script de solution (par exemple, le Jour 11 de l'année 2021) :

1. Ouvrez un terminal dans le répertoire de l'année concernée :
   ```bash
   cd 2021
   ```

2. Exécutez le script Python :
   ```bash
   python 11_1.py
   ```

---

## 🛠️ Utilitaire de lecture d'entrée (`read_input.py`)

Chaque dossier annuel dispose d'un module d'aide `read_input.py` pour charger les données d'entrée. Voici les principales fonctions disponibles :

| Fonction | Description | Retour |
| :--- | :--- | :--- |
| `read_multiple_lines(filename)` | Lit le fichier ligne par ligne en supprimant les espaces aux extrémités. | `Generator[str]` |
| `read_multiple_lines_no_backslash_n(filename)` | Lit le fichier ligne par ligne en supprimant uniquement le retour à la ligne (`\n`). | `Generator[str]` |
| `read_one_line(filename)` | Lit uniquement la première ligne du fichier. | `str` |
| `read_all_lines(filename)` | Lit l'intégralité du fichier sous forme de liste de lignes nettoyées. | `list[str]` |
| `read_all_lines_as_listlistint(filename)` | *(Disponible en 2021)* Lit une grille de chiffres et la convertit en matrice d'entiers à deux dimensions. | `list[list[int]]` |

### Exemple d'utilisation dans un script :

```python
import read_input

# Charger une grille de nombres (ex: Jour 11 de 2021)
grid = read_input.read_all_lines_as_listlistint("2021_11.txt")

# Ou lire ligne par ligne
for line in read_input.read_multiple_lines("2025_1.txt"):
    # traitement de la ligne...
    pass
```

---

## 🌟 Années Résolues

- [x] **[2021](file:///c:/Users/a.grandjean/Desktop/Python_AdventOfCode/2021)** (En cours 🏃‍♂️)
- [x] **[2025](file:///c:/Users/a.grandjean/Desktop/Python_AdventOfCode/2025)** (En cours 🏃‍♂️)
