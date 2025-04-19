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

def decoupe_gaussienne(mu, sigma, k):
    """
    Découpe une gaussienne de moyenne mu et d'écart-type sigma en k intervalles d'aires égales.
    """
    quantiles = np.linspace(0, 1, k + 1)
    limites = norm.ppf(quantiles, loc=mu, scale=sigma)
    limites[0], limites[-1] = -np.inf, np.inf
    return limites

def assigner_valeurs_binaires(values, limites, k):
    """
    Assigne des valeurs binaires à chaque valeur en fonction des intervalles définis.
    """
    binary_values = []
    binary_indices = []
    for value in values:
        for i in range(k):
            if limites[i] <= value < limites[i + 1]:
                binary_values.append(format(i, f'0{k.bit_length() - 1}b'))  # Valeur binaire
                binary_indices.append(i)  # Indice de l'intervalle
                break
    return binary_values, binary_indices

def plot_gaussian_and_save_binary(k):
    csv_file = select_file()  # Demander à l'utilisateur de sélectionner un fichier CSV
    
    if not csv_file:
        print("Aucun fichier sélectionné.")
        return

    try:
        with open(csv_file, 'r') as f:
            content = f.read().strip()
            if not content:
                print("Le fichier est vide.")
                exit()

        # Charger les données avec pandas
        df = pd.read_csv(csv_file, header=None, skip_blank_lines=True)

        # Extraire la première ligne comme une liste de nombres
        values = df.iloc[0].astype(float).tolist()

        # Calcul des paramètres de la gaussienne
        mean, std = norm.fit(values)

        # Découper la gaussienne en k intervalles
        limites = decoupe_gaussienne(mean, std, k)

        # Assigner des valeurs binaires
        binary_values = assigner_valeurs_binaires(values, limites, k)

        # Sauvegarder les valeurs binaires dans un fichier texte
        output_file = f"decoupage{k}.txt"
        with open(output_file, "w") as f:
            f.write("".join(binary_values))
        print(f"Fichier binaire sauvegardé sous le nom : {output_file}")

        # Tracer l'histogramme et la gaussienne
        plt.hist(values, bins=100, density=True, alpha=0.6, color='g')
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std)
        plt.plot(x, p, 'k', linewidth=2)

        # Ajouter les lignes de découpe
        for limite in limites[1:-1]:
            plt.axvline(limite, color='red', linestyle='--', alpha=0.7)

        title = f"Fit Gaussienne: μ = {mean:.10f}, σ = {std:.10f}"
        plt.title(title)
        plt.xlabel("Valeurs")
        plt.ylabel("Densité")
        plt.show()

    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

if __name__ == "__main__":
    #k = int(input("Entrez le nombre de découpes (k) : "))
    k=16
    plot_gaussian_and_save_binary(k)