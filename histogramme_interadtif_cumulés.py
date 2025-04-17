import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import re
import os
import numpy as np

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Choisir un ou plusieurs fichiers de résultats (jusqu'à 4)",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )
    return file_paths

def extract_pvalues_from_file(file_path):
    pvalues = {}
    current_test = None
    serial_counter = 1
    test_15_state_1_pvalue = None
    test_16_state_1_pvalue = None

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Cas standard : Test 01 à 14
            match = re.match(r"^(\d+)\.\s+(.+?)\s{2,}([0-9.eE+-]+)\s+(Random|Non-Random)", line)
            if match:
                test_number = match.group(1)
                test_name = f"{test_number}. {match.group(2).strip()}"
                pval = float(match.group(3))
                pvalues[test_name] = pval
                continue

            # Détection des tests composés
            if line.startswith("11. Serial Test:"):
                current_test = "Serial Test"
                serial_counter = 1
                continue

            if line.startswith("15. Random Excursions Test:"):
                current_test = "15. Random Excursions Test:"
                continue

            if line.startswith("16. Random Excursions Variant Test:"):
                current_test = "16. Random Excursions Variant Test:"
                continue
            
            # Tests Serial (suite)
            if current_test == "Serial Test" and re.match(r"^[0-9.eE+-]+\s+(Random|Non-Random)", line):
                pval = float(line.split()[0])
                test_name = f"11.Serial Test {serial_counter}"
                serial_counter += 1
                pvalues[test_name] = pval
                continue

            # Extraction des p-values pour les states +1 des tests 15 et 16
            if line.startswith("+1") and current_test == "15. Random Excursions Test:":
                test_15_state_1_pvalue = float(line.split()[2])
                continue

            if line.startswith("+1") and current_test == "16. Random Excursions Variant Test:":
                test_16_state_1_pvalue = float(line.split()[2])
                continue

    # Renommer les deux dernières clés avec les valeurs des states +1
    if test_15_state_1_pvalue is not None and test_16_state_1_pvalue is not None:
        pvalues["15. Random Excursions Test: (state =1)"] = test_15_state_1_pvalue
        pvalues["16. Random Excursions Variant Test: (state = 1)"] = test_16_state_1_pvalue

    return pvalues

def plot_pvalues_comparison(pvalues_dict, file_names):
    tests = sorted(set(test for pvalues in pvalues_dict.values() for test in pvalues.keys()))
    x = np.arange(len(tests))  # Position des tests sur l'axe x
    width = 0.2  # Largeur des barres
    colors = ['skyblue', 'orange', 'green', 'purple']  # Couleurs pour chaque fichier
    seuil_critique = 0.01  # Seuil critique pour les tests réussis

    plt.figure(figsize=(14, 7))

    # Calcul du nombre de tests réussis pour chaque fichier
    success_counts = {}
    for i, (file_name, pvalues) in enumerate(pvalues_dict.items()):
        values = [pvalues.get(test, 0) for test in tests]  # Obtenir les p-values pour chaque test
        plt.bar(x + i * width, values, width, label=file_name, color=colors[i % len(colors)], edgecolor='black')
        success_counts[file_name] = sum(1 for pval in values if pval > seuil_critique)

    plt.axhline(seuil_critique, color='red', linestyle='--', label=f"Seuil critique ({seuil_critique})")
    plt.xticks(x + width * (len(pvalues_dict) - 1) / 2, tests, rotation=45, ha='right')
    plt.yscale('log')
    plt.ylabel('p-value (log)')
    
    # Ajouter le nombre de tests réussis dans le titre
    success_summary = ", ".join([f"{file}: {count} tests réussis" for file, count in success_counts.items()])
    plt.title(f"Comparaison des résultats des tests NIST\n{success_summary}")
    
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# --- Main execution ---

if __name__ == "__main__":
    files = select_files()
    if not files:
        print("Aucun fichier sélectionné.")
    elif len(files) > 4:
        print("Veuillez sélectionner jusqu'à 4 fichiers uniquement.")
    else:
        pvalues_dict = {}
        for file_path in files:
            pvalues = extract_pvalues_from_file(file_path)
            filename = os.path.basename(file_path)
            pvalues_dict[filename] = pvalues

        plot_pvalues_comparison(pvalues_dict, list(pvalues_dict.keys()))


