# filepath: untitled:Untitled-1
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.stats import norm
import numpy as np

# Ouvrir une fenêtre pour sélectionner le fichier CSV
def select_file():
    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

# Charger le fichier CSV
csv_file = select_file() # Remplacez par le nom de votre fichier CSV

if csv_file:
    print(f"Chemin du fichier sélectionné : {csv_file}")
    try:
        # Vérifier si le fichier est vide
        with open(csv_file, 'r') as f:
            content = f.read().strip()
            if not content:
                print("Le fichier est vide.")
                exit()

        # Charger les données avec pandas
        df = pd.read_csv(csv_file, header=None, skip_blank_lines=True)

        # Extraire la première ligne comme une liste de nombres
        data = df.iloc[0].astype(float).tolist()

        plt.hist(data, bins=1000, density=True, alpha=0.6, color='g')

        # Ajouter une courbe gaussienne
        mean, std = norm.fit(data)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std)
        plt.plot(x, p, 'k', linewidth=2)

        title = f"Fit Gaussienne: μ = {mean:.18f}, σ = {std:.18f}"
        plt.title(title)
        plt.xlabel("Valeurs")
        plt.ylabel("Densité")
        plt.show()
        # Afficher l'histogramme
        plt.show()

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
else:
    print("Aucun fichier sélectionné.")