def extract_column_data(file_path):
    column_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#') and ',' in line:
                time_tag, channel = line.split(',')
                channel = channel.strip()
                if channel in ('1', '4'):
                    column_data.append(channel)
    return column_data

def transform_column_data(column_data):
    transformed_data = []
    for channel in column_data:
        n = int(channel)
        if n == 4:
            k=1
        else:
            k=0
        transformed_data.append(k)
    return transformed_data


file_path = 'data/longue.txt'
column_data = extract_column_data(file_path)
transformed_data = transform_column_data(column_data)
#print(transformed_data[1:10])
new_file_name = input("Enter the name of the new file to save the data: ")
new_file_name_vonNeumann = input("Enter the name of the new extracted file to save the data: ")

with open(new_file_name, "w", encoding="utf-8") as fichier:
    # Écrire des données dans le fichier
    for i in transformed_data:
        fichier.write(str(i))

def von_neumann_extractor(input_file, output_file):
    """
    Reads a file containing a string of 0s and 1s (on one line),
    applies the Von Neumann debiasing algorithm, and writes the output to a new file.
    """
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

von_neumann_extractor(file_path, new_file_name_vonNeumann)  # Call the function 

