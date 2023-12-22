# creation de differentes fonctions
def creer_grille(data):
    grid = []
    for i in range(9): # indice ligne
        grid.append([])
        for j in range(9): # indice colonne
            grid[i].append(int(data[i*9+j]))
    return grid

def imprimer_grille(g):
    print('*'*22)
    for i in range(9):
        print('|', end='')
        for j in range(9):
            if g[i][j] > 0:
                print(g[i][j], end=' ')
            else:
                print(' ', end= ' ')
            if (j+1) % 3 == 0:
                print('|', end='')
        print('') 
        if (i+1) % 3 == 0:
            print('*'*22)

def check_row(valeur, row):
    for j in range(9):
        if g[row][j] == valeur:
            return False
    return True

def check_col(valeur, col):
    for i in range(9):
        if g[i][col] == valeur:
            return False
    return True

def check_square(valeur, row, col):
    for i in range((row//3)*3, (row//3)*3 + 3):
        for j in range((col//3)*3, (col//3)*3 + 3):
            if g[i][j] == valeur:
                return False
    return True

def check_value(valeur, row, col):
    test1 = check_row(valeur, row)
    test2 = check_col(valeur, col)
    test3 = check_square(valeur, row, col)
    test4 = (valeur > 0) and (valeur < 10) 
    if test1 and test2 and test3 and test4:
        return True
    else:
        if test1 is False:
            print('valeur deja sur la ligne')
        if test2 is False:
            print('valeur deja sur la colonne')
        if test3 is False:
            print('valeur deja sur le carre') 

def check_win():
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return False
    return True

# utilisation des fonctions
data = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
g = creer_grille(data)
jai_gagne = False
while jai_gagne is False:
    imprimer_grille(g) 
    row = int(input('Ligne?')) - 1 
    col = int(input('Colonne?')) - 1 
    if g[row][col] == 0:
        val = int(input('Valeur?'))
        if check_value(val, row, col):
            g[row][col] = val
    else:
        print('deja pris')

    jai_gagne = check_win() 






