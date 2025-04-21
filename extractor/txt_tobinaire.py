def select_files():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(title="Select files", filetypes=[("Text files", "*.txt")])
    return file_paths

def convert_bits_txt_to_binfile(bits_txt, bin_out):
    with open(bits_txt, 'r') as f:
        bits = ''.join(c for c in f.read() if c in '01')  # ne garde que les 0 et 1

    with open(bin_out, 'wb') as out:
        for i in range(0, len(bits), 32):
            chunk = bits[i:i+32].ljust(32, '0')  # complète avec des zéros si < 32 bits
            uint32_val = int(chunk, 2)
            out.write(uint32_val.to_bytes(4, byteorder='little', signed=False))

    print(f"Fichier binaire généré : {bin_out}")

if __name__ == "__main__":
    txt_files = select_files()
    if txt_files:
        for txt_file in txt_files:
            bin_file = txt_file.replace('.txt', '.bin')
            convert_bits_txt_to_binfile(txt_file, bin_file)
            print(f"Converted {txt_file} to {bin_file}")
    else:
        print("No files selected.")
