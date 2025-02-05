import os
import sys
#import re
import config_ini as ci
#from config_ini import read_folders_from_ini, read_base_path_from_ini
import manage_folder as mf


def create_folders(base_path, nome_commessa, suffix, folders):
    commessa_path = os.path.join(base_path, f"{nome_commessa}")
    name_folder_in_commessa = f"{nome_commessa}{suffix}"
    if mf.check_subfolders_exist(commessa_path, [name_folder_in_commessa]):
        print(f"La cartella '{name_folder_in_commessa}' esiste nella commessa '{nome_commessa}'.")
        # Crea le cartelle presenti in folders
        path_folder_in_commessa = os.path.join(commessa_path, name_folder_in_commessa)
        mf.create_folders(path_folder_in_commessa, folders)
        print(f"Cartelle in '{name_folder_in_commessa}' create in '{name_folder_in_commessa}'.")
    else:
        print(f"La cartella '{name_folder_in_commessa}' non esiste nella commessa '{nome_commessa}'.")


def main():
    """
    Funzione principale del programma. Legge le configurazioni, richiede input all'utente e crea le cartelle.
    """
    print("Benvenuto nel generatore di cartelle!")
    
    # Ottieni il percorso della directory dell'eseguibile
    if getattr(sys, 'frozen', False):
        # Se il programma è stato congelato con PyInstaller
        current_dir = os.path.dirname(sys.executable)
    else:
        # Se il programma è in esecuzione come script Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
    # Lettura del percorso base e delle cartelle da settings.ini
    base_path = ci.read_base_path_from_ini(current_dir)
    if not base_path:
        print(f"Percorso '{base_path}' non configurato correttamente. Programma terminato.")
        #print("Percorso base non configurato correttamente. Programma terminato.")
        return
    
    folders_documenti, folders_software = ci.read_folders_from_ini(current_dir)
    
    # Chiedi all'utente il NomeCommessa e verifica se esiste
    commessa_folders = mf.get_commessa_folders(base_path)
    while True:
        nome_commessa = input("Inserisci il NomeCommessa: ")
        if mf.check_commessa_exists(commessa_folders, nome_commessa):
            print(f"Commessa '{nome_commessa}' trovata.")
            break
        else:
            print(f"Commessa '{nome_commessa}' non trovata. Riprova.")   
   
    # Crea le cartelle per i documenti 
    create_folders(base_path, nome_commessa, "DC000", folders_documenti)
    # Crea le cartelle per il software
    create_folders(base_path, nome_commessa, "SW000", folders_software)
    
    input("Premi un tasto per uscire...")
    return 

if __name__ == "__main__":
    main()
