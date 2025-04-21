import os
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def select_file():
    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def plot_gaussian_and_save_binary():
    csv_file_1 = select_file()  # Demander à l'utilisateur de sélectionner un fichier CSV
    csv_file_2 = select_file()  # Demander à l'utilisateur de sélectionner un fichier CSV

    if not csv_file_1 or not csv_file_2:
        print("Aucun fichier sélectionné.")
        return

    try:
        # Obtenir les noms des fichiers pour la légende
        file_name_1 = os.path.basename(csv_file_1)
        file_name_2 = os.path.basename(csv_file_2)

        # Charger les données avec pandas
        df = pd.read_csv(csv_file_1, header=None, skip_blank_lines=True)
        values_1 = df.iloc[0].astype(float).tolist()

        df_2 = pd.read_csv(csv_file_2, header=None, skip_blank_lines=True)
        values_2 = df_2.iloc[0].astype(float).tolist()

        # Calcul des paramètres de la gaussienne pour le premier fichier
        mean_1, std_1 = norm.fit(values_1)

        # Calcul des paramètres de la gaussienne pour le second fichier
        mean_2, std_2 = norm.fit(values_2)

        # Tracer les histogrammes et les gaussiennes
        plt.hist(values_1, bins=100, density=True, alpha=0.6, color='g', label=f"{file_name_1} (μ={mean_1:.2f}, σ={std_1:.2f})")
        plt.hist(values_2, bins=100, density=True, alpha=0.6, color='r', label=f"{file_name_2} (μ={mean_2:.2f}, σ={std_2:.2f})")

        # Tracer les courbes de densité
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p1 = norm.pdf(x, mean_1, std_1)
        p2 = norm.pdf(x, mean_2, std_2)
        plt.plot(x, p1, 'k', linewidth=2, label=f"Gaussienne {file_name_1}")
        plt.plot(x, p2, 'b', linewidth=2, label=f"Gaussienne {file_name_2}")

        # Ajouter la légende
        plt.legend()

        # Ajouter les titres et les labels
        plt.title("Comparaison des deux gaussiennes")
        plt.xlabel("Valeurs")
        plt.ylabel("Densité")
        plt.show()

    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

if __name__ == "__main__":
    plot_gaussian_and_save_binary()