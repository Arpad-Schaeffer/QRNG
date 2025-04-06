import matplotlib.pyplot as plt
import numpy as np

# Nom du fichier
file_name = "longue_binary.txt"

# Dictionnaire des tests avec leurs p-values
test_results = {
    "01. Frequency (Monobit) Test": 0.10183958739609647,
    "02. Frequency Test within a Block": 0.9560474279814061,
    "03. Runs Test": 6.0803830718111e-45,
    "04. Test for the Longest Run of Ones": 0.7114498016153308,
    "05. Binary Matrix Rank Test": 0.0468451759076384,
    "06. Discrete Fourier Transform (Spectral)": 0.027637697885514758,
    "07. Non-overlapping Template Matching": 0.010828811149849914,
    "08. Overlapping Template Matching": 0.012483580670010931,
    "09. Maurer’s \"Universal Statistical\" Test": 0.3751624567424922,
    "10. Linear Complexity Test": 0.9730421082780204,
    "12. Approximate Entropy Test": 0.013763466821581558,
    "13. Cumulative Sums Test (Forward)": 0.10259803943191198,
    "14. Cumulative Sums Test (Backward)": 0.20367733459510035,
    "15. Random Excursions Test (Chi²)": 0.22064300793671066
}

# Extraction des noms des tests et des valeurs
tests = list(test_results.keys())
p_values = list(test_results.values())

# Création du graphe
plt.figure(figsize=(12, 6))
bars = plt.bar(tests, p_values, color='skyblue', edgecolor='black')

# Ajout des valeurs au centre réel des colonnes
for bar, p_val in zip(bars, p_values):
    height = bar.get_height()
    center_y = 10e-23
    plt.text(bar.get_x() + bar.get_width() / 2, center_y, f'{p_val:.2e}',  # Position verticale ajustée
             ha='center', va='center', fontsize=8, color='black')

# Échelle logarithmique sur l'axe y
plt.yscale('log')

# Ligne de seuil critique
plt.axhline(0.01, color='red', linestyle='--', label="Seuil critique (0.01)")

# Ajustement des étiquettes
plt.xlabel("Test")
plt.ylabel("p-value (échelle log)")
plt.title(f"Résultats des tests NIST pour {file_name}")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# Affichage
plt.show()
