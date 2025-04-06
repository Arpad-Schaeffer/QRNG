import os

def von_neumann_extractor(input_file):
    """
    Reads a file containing a string of 0s and 1s (on one line),
    applies the Von Neumann debiasing algorithm, and writes the output to a new file.
    """

    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}_VonNeumann{ext}"

    with open(input_file, 'r') as file:
        bitstring = file.read().strip()  # Read the entire line and remove extra spaces/newlines

    extracted_bits = []  # List to store unbiased bits

    # Process bits in pairs
    for i in range(0, len(bitstring) - 1, 2):  # Step by 2 to get pairs
        pair = bitstring[i:i+2]  # Take two consecutive bits
        
        if pair == "01":
            extracted_bits.append("0")  # Keep as 0
        elif pair == "10":
            extracted_bits.append("1")  # Keep as 1

    # Write the output to a file
    with open(output_file, 'w') as file:
        file.write("".join(extracted_bits)) 
        print(f"Extracted {len(extracted_bits)} unbiased bits. Output saved to {output_file}")

# Interactive use
#file_path = input("Enter the path of the file to extract the data: ")
#new_file_name_vonNeumann = input("Enter the name of the new extracted file to save the data: ")
input_filename = "longue_binary_XOR10.txt"  # Remplace par le nom de ton fichier


von_neumann_extractor(input_filename)  # Call the function 