import numpy as np

# on crée une matrice de nombres aléatoires
data = np.random.random(1000).reshape(100, 10)

if n_col := data.shape[1] > 10:
    print("Nombre de colonnes : {}".format(n_col))
elif n_col == 10:
    print("On a bien 10 colonnes")

print(n_col)
