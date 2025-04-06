def convert_bits_to_uint32(input_file, output_file):
    with open(input_file, 'r') as f:
        bits = ''.join(c for c in f.read() if c in '01')
    with open(output_file, 'w') as out:
        for i in range(0, len(bits), 32):
            chunk = bits[i:i+32].ljust(32, '0')  # complète si < 32 bits
            out.write(f"{int(chunk, 2)}\n")

# ==== UTILISATION INTERACTIVE ====
#input_file = input("Entrez le nom du fichier contenant les bits (ex: input.txt) : ").strip()
input_file = 'longue_binary.txt'

# Construire le nom du fichier de sortie automatiquement
if '.' in input_file:
    output_file = input_file.rsplit('.', 1)[0] + "_converted.txt"
else:
    output_file = input_file + "_converted.txt"

convert_bits_to_uint32(input_file, output_file)

print(f"Conversion terminée : fichier généré → {output_file}")

