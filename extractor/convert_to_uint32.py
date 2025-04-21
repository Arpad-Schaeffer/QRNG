def convert_bits_to_uint32(input_file, output_file):
    with open(input_file, 'r') as f:
        bits = ''.join(c for c in f.read() if c in '01')
    with open(output_file, 'w') as out:
        for i in range(0, len(bits), 32):
            chunk = bits[i:i+32].ljust(32, '0')  # complète si < 32 bits
            out.write(f"{int(chunk, 2)}\n")

# ==== UTILISATION INTERACTIVE ====
def select_file():
    """
    Ouvre une boîte de dialogue pour permettre à l'utilisateur de sélectionner
    un fichier texte.

    Returns:
        str: Chemin du fichier sélectionné ou une chaîne vide si aucun fichier
        n'est sélectionné.
    """
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = askopenfilename(filetypes=[("txt files", "*.txt")])
    return file_path


input_file = select_file()  # Utiliser la fonction de sélection de fichier
if not input_file:  # Vérifie si un fichier a été sélectionné
    print("Aucun fichier sélectionné.")
    exit()

# Construire le nom du fichier de sortie automatiquement
if '.' in input_file:
    output_file = input_file.rsplit('.', 1)[0] + "_converted.txt"
else:
    output_file = input_file + "_converted.txt"

convert_bits_to_uint32(input_file, output_file)

print(f"Conversion terminée : fichier généré → {output_file}")

