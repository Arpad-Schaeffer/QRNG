from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Fonction pour extraire les données d'une colonne spécifique dans un fichier CSV
def extract_column_data(file_path):
    """
    Lit un fichier CSV et extrait les données de la colonne 'channel' 
    si elles correspondent aux valeurs '1' ou '4'.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        list: Liste des valeurs extraites de la colonne 'channel'.
    """
    column_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Supprime les espaces inutiles
            # Ignore les lignes vides, les commentaires et les lignes sans virgule
            if line and not line.startswith('#') and ',' in line:
                time_tag, channel = line.split(',')  # Sépare les colonnes
                channel = channel.strip()  # Nettoie la valeur de la colonne 'channel'
                if channel in ('1', '4'):  # Filtre les valeurs intéressantes
                    column_data.append(channel)
    return column_data

# Fonction pour transformer les données extraites
def transform_column_data(column_data):
    """
    Transforme les données extraites en remplaçant '4' par 1 et tout autre
    valeur par 0.

    Args:
        column_data (list): Liste des valeurs extraites.

    Returns:
        list: Liste des valeurs transformées.
    """
    transformed_data = []
    for channel in column_data:
        n = int(channel)
        k = 1 if n == 4 else 0  # Transformation conditionnelle
        transformed_data.append(k)
    return transformed_data

# Fonction pour ouvrir une boîte de dialogue et sélectionner un fichier
def select_file():
    """
    Ouvre une boîte de dialogue pour permettre à l'utilisateur de sélectionner
    un fichier CSV.

    Returns:
        str: Chemin du fichier sélectionné ou une chaîne vide si aucun fichier
        n'est sélectionné.
    """
    Tk().withdraw()  # Cacher la fenêtre principale de Tkinter
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

# Point d'entrée principal du script
if __name__ == "__main__":
    # Demander à l'utilisateur de sélectionner un fichier CSV
    file_path = select_file()
    if not file_path:  # Vérifie si un fichier a été sélectionné
        print("Aucun fichier sélectionné.")
        exit()

    # Extraire et transformer les données
    column_data = extract_column_data(file_path)
    transformed_data = transform_column_data(column_data)

    # Générer un nouveau nom de fichier pour les données transformées
    new_file_name = file_path.replace('.csv', '_extracted.txt')

    # Écrire les données transformées dans un nouveau fichier
    with open(new_file_name, "w", encoding="utf-8") as fichier:
        for value in transformed_data:
            fichier.write(str(value) + '\n')  # Ajoute un saut de ligne pour chaque valeur

    print(f"Les données transformées ont été enregistrées dans : {new_file_name}")


