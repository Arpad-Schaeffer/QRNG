import hashlib
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re

def select_file():
    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = askopenfilename(filetypes=[("txt files", "*.txt")])
    return file_path

file_name = select_file()  # Demander à l'utilisateur de sélectionner un fichier CSV
if not file_name:
    print("Aucun fichier sélectionné.")
    exit()
# Charger les bits depuis un fichier texte
with open(file_name, "r") as f:
    bitstream = f.read().strip()  # exemple: "011010101010..."

# Convertir en bytes (par paquets de 8 bits)
byte_array = bytearray(int(bitstream[i:i+8], 2) for i in range(0, len(bitstream), 8))

# Appliquer la fonction de hachage SHA512
hash_object = hashlib.sha512(byte_array)
hashed_bits = hash_object.digest()  # Résultat en bytes (64 octets = 512 bits)

# Facultatif : convertir en bits lisibles
hashed_bitstring = ''.join(f'{byte:08b}' for byte in hashed_bits)

# Demander à l'utilisateur de sélectionner un fichier texte
base_name, ext = os.path.splitext(file_name)

output_file = f"{base_name}_SHA512{ext}"
# Sauvegarder
with open(output_file, "w") as f:
    f.write(hashed_bitstring)
print(f"Fichier haché enregistré sous : {output_file}")