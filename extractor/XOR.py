import os
import tkinter as tk
from tkinter import filedialog
import re

def apply_xor_extractor(input_file, group_size):
    """
    Applique un extracteur XOR sur un fichier contenant des 0 et 1.
    Chaque `group_size` bits sont combinés via XOR pour produire un seul bit en sortie.

    :param input_file: Nom du fichier contenant des 0 et 1.
    :param group_size: Nombre de bits utilisés pour l'opération XOR (ex. 2, 5, 10).
    """
    # Vérification de l'existence du fichier
    if not os.path.exists(input_file[0]):
        print(f"Erreur : le fichier '{input_file[0]}' n'existe pas.")
        return
    
    # Création du nom du fichier de sortie
    base_name, ext = os.path.splitext(input_file[0])
    output_file = f"{base_name}_XOR{group_size}{ext}"

    # Lecture du fichier d'entrée
    with open(input_file[0], 'r') as f:
        data = f.read().strip()  # Suppression des espaces et sauts de ligne

    # Vérification du format (seulement 0 et 1 autorisés)
    if not all(bit in '01' for bit in data):
        print("Erreur : le fichier doit contenir uniquement des 0 et 1.")
        return

    # Application de l'XOR sur des groupes de `group_size` bits
    xor_result = []
    
    for i in range(0, len(data) - (len(data) % group_size), group_size):  # Ignore les bits restants
        group = data[i:i+group_size]
        xor_value = 0
        for bit in group:
            xor_value ^= int(bit)  # Application du XOR bit par bit
        xor_result.append(str(xor_value))

    # Écriture du résultat dans le fichier de sortie
    with open(output_file, 'w') as f:
        f.write(''.join(xor_result))

    print(f" XOR avec {group_size} bits terminé : {output_file}")
#interactive use 
def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Choisir un ou plusieurs fichiers de résultats",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )
    return file_paths
# Fichier à traiter
input_filename = select_files() # Remplace par le nom de ton fichier

# Boucle sur différentes tailles de groupes
for group_size in [2]:
    apply_xor_extractor(input_filename, group_size)
