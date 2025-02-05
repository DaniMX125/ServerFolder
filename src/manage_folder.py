import os

def get_commessa_folders(base_path):
    """
    Restituisce l'elenco delle cartelle di commessa nel percorso base.
    """
    return [folder for folder in os.listdir(base_path)]

def check_commessa_exists(commessa_folders, nome_commessa):
    """
    Verifica se una cartella di commessa esiste nell'elenco delle cartelle.
    """
    return any(folder == f"{nome_commessa}" for folder in commessa_folders)

def check_subfolders_exist(commessa_path, subfolders):
    """
    Verifica se le sottocartelle esistono all'interno della cartella di commessa.
    """
    return all(os.path.exists(os.path.join(commessa_path, subfolder)) for subfolder in subfolders)

def create_folders(base_path, folders):
    """
    Crea le cartelle specificate nel percorso base.
    """
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                print(f"Cartella '{folder_path}' creata con successo.")
            else:
                print(f"La cartella '{folder_path}' esiste già.")
        except Exception as e:
            print(f"Errore durante la creazione della cartella '{folder_path}': {e}")
