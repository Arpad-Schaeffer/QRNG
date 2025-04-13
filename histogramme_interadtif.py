import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import re
import os

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Choisir un ou plusieurs fichiers de résultats",
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
            match = re.match(r"^\d+\.\s+(.+?)\s{2,}([0-9.eE+-]+)\s+(Random|Non-Random)", line)
            if match:
                test_name = match.group(1).strip()
                pval = float(match.group(2))
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

def plot_pvalues(pvalues, title):
    tests = list(pvalues.keys())
    values = list(pvalues.values())

    # Calculer le nombre de tests réussis
    passed_tests = sum(1 for p_val in values if p_val >= 0.01)
    total_tests = len(values)

    # Ajouter le nombre de tests réussis au titre
    title += f" ({passed_tests}/{total_tests} tests réussis)"

    plt.figure(figsize=(12, 6))
    bars = plt.bar(tests, values, color='skyblue', edgecolor='black')

    for bar, p_val in zip(bars, values):
        # Définir la couleur du texte en fonction de la p-value
        color = 'green' if p_val >= 0.01 else 'red'
        # Afficher uniquement la valeur numérique de la p-value
        plt.text(bar.get_x() + bar.get_width()/2, 10e-23, f'{p_val:.2e}', 
                 ha='center', va='bottom', fontsize=8, color=color)

    plt.yscale('log')
    plt.axhline(0.01, color='red', linestyle='--', label="Seuil critique (0.01)")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('p-value (log)')
    plt.title(title)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Main execution ---

if __name__ == "__main__":
    files = select_files()
    if not files:
        print("Aucun fichier sélectionné.")
    else:
        for file_path in files:
            pvalues = extract_pvalues_from_file(file_path)
            filename = os.path.basename(file_path)
            plot_pvalues(pvalues, f"Résultats des tests NIST pour {filename}")


