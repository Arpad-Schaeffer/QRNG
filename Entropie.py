import matplotlib.pyplot as plt
import tkinter as Tk
from tkinter.filedialog import askopenfilenames
import re
import os
import numpy as np
import math
from collections import Counter
import plotgausiienne as plotgausiienne
import pandas as pd
from scipy.stats import norm

def select_file():
    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_paths = askopenfilenames(filetypes=[("CSV files", "*.csv")])
    return file_paths


def entropy_from_bin_distribution(bin_indices, k):
    """
    Calcule l'entropie directement à partir de l'indice des bins (0 à k-1).
    """
    total = len(bin_indices)
    freqs = Counter(bin_indices)
    entropy = -sum((count / total) * math.log2(count / total) for count in freqs.values())
    return entropy

def plot_histogram_and_entropy(k):
    file_paths = select_file()  # Demander à l'utilisateur de sélectionner un ou plusieurs fichiers texte
    if not file_paths:
        print("Aucun fichier sélectionné.")
        return

    plt.figure(figsize=(12, 6))  # Créer une seule figure pour tous les fichiers

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
                if not content:
                    print(f"Le fichier {file_path} est vide.")
                    continue

            # Charger les données avec pandas
            df = pd.read_csv(file_path, header=None, skip_blank_lines=True)

            # Extraire la première ligne comme une liste de nombres
            values = df.iloc[0].astype(float).tolist()

            # Calcul des paramètres de la gaussienne
            mean, std = norm.fit(values)
            entropies = []  # Liste pour stocker les entropies pour ce fichier

            # Calculer les entropies pour chaque découpage
            for i in range(1, k + 1):  # Parcourir les découpages de 1 à k
                limites = plotgausiienne.decoupe_gaussienne(mean, std, i)  # Découper la gaussienne
                bin_indices = plotgausiienne.assigner_valeurs_binaires(values, limites, i)[1]  # Obtenir les indices des bins
                entropy = entropy_from_bin_distribution(bin_indices, i)  # Calculer l'entropie
                entropies.append(entropy)  # Ajouter l'entropie à la liste

            # Tracer les entropies pour ce fichier
            plt.plot(range(1, k + 1), entropies, marker='o', linestyle='-', label=os.path.basename(file_path))

        except Exception as e:
            print(f"Erreur lors du traitement du fichier {file_path}: {e}")

    # Ajouter la légende et les labels
    plt.legend()
    plt.title("Entropies pour différents fichiers")
    plt.xlabel("Nombre d'intervalles (k)")
    plt.ylabel("Entropie")
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Afficher le graphique
    plt.tight_layout()
    plt.show()

