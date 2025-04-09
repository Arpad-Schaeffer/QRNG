import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.stats import norm
import numpy as np

import matplotlib.pyplot as plt

# Ouvrir une fenêtre pour sélectionner le fichier CSV
# def select_file():
#     Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
#     file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
#     return file_path

# Charger les données et tracer la gaussienne
def plot_gaussian():
    file_path = "/Users/luluzaidat/Desktop/PSC Git/QRNG/real_data copie.csv"
    if not file_path:
        print("Aucun fichier sélectionné.")
        return

    # Charger les données du fichier CSV
    try:
        data = pd.read_csv(file_path)
        if data.shape[1] != 1:
            print("Le fichier CSV doit contenir une seule colonne de données.")
            return

        values = data.iloc[:, 0]

        # Tracer l'histogramme et ajuster une courbe gaussienne
        plt.hist(values, bins=30, density=True, alpha=0.6, color='g')

        # Ajouter une courbe gaussienne
        mean, std = norm.fit(values)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std)
        plt.plot(x, p, 'k', linewidth=2)

        title = f"Fit Gaussienne: μ = {mean:.2f}, σ = {std:.2f}"
        plt.title(title)
        plt.xlabel("Valeurs")
        plt.ylabel("Densité")
        plt.show()

    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

if __name__ == "__main__":
    plot_gaussian()