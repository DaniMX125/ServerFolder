import os
import re
from config_ini import read_folders_from_ini, read_base_path_from_ini

def create_folder(base_path, folder_name):    
    """
    Crea una cartella se non esiste.

    Args:
        base_path (str): Il percorso base dove creare la cartella.
        folder_name (str): Il nome della cartella da creare.
    """
    full_path = os.path.join(base_path, folder_name)
    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Cartella '{full_path}' creata con successo.")
        else:
            print(f"La cartella '{full_path}' esiste già.")
    except Exception as e:
        print(f"Errore durante la creazione della cartella '{full_path}': {e}")

def get_valid_folder_type(prompt):
    """
    Richiede un tipo di cartella valido all'utente.

    Args:
        prompt (str): Il messaggio da mostrare all'utente.

    Returns:
        str: Il tipo di cartella valido ('d' per documenti, 's' per software).
    """
    valid_types = {
        "documenti": ["d", "documenti"],
        "software": ["s", "software"]
    }

    while True:
        response = input(prompt).strip().lower()
        for key, variants in valid_types.items():
            if response in variants:
                return key[0]
        print(f"Input non valido. Rispondi con una delle opzioni: {', '.join(sum(valid_types.values(), []))}")

def get_valid_response(prompt):
    """
    Richiede una risposta valida all'utente, accettando varianti flessibili.

    Args:
        prompt (str): Il messaggio da mostrare all'utente.

    Returns:
        str: La risposta valida ('yes' o 'no').
    """
    valid_responses = {
        "yes": ["yes", "y", "sì", "si", "s"],
        "no": ["no", "n"]
    }

    while True:
        response = input(prompt).strip().lower()
        for key, variants in valid_responses.items():
            if response in variants:
                return key
        print(f"Input non valido. Rispondi con una delle opzioni: {', '.join(sum(valid_responses.values(), []))}")

def generate_folders(folder_type, base_path, folders_documenti, folders_software):
    """
    Genera le cartelle in base al tipo (documenti o software).

    Args:
        folder_type (str): Il tipo di cartella ('d' per documenti, 's' per software).
        base_path (str): Il percorso base dove creare le cartelle.
        folders_documenti (list): La lista delle cartelle per documenti.
        folders_software (list): La lista delle cartelle per software.
    """
    folders = []
    if folder_type == 'd':
        folders = folders_documenti
    elif folder_type == 's':
        folders = folders_software
    if not folders:
        print("Tipo di cartella non valido. Programma terminato.")
        return

    for folder in folders:
        response = get_valid_response(f"Vuoi creare la cartella '{folder}'? (yes/no): ")
        if response == 'yes':
            create_folder(base_path, folder)
        elif response == 'no':
            print(f"{folder} non creata.")
        else:
            print(f"Non puoi saltare questa decisione! Riprova.")

def is_valid_folder_name(folder_name):
    """
    Verifica se il nome della cartella è valido per Windows.

    Args:
        folder_name (str): Il nome della cartella da verificare.

    Returns:
        tuple: Un booleano che indica se il nome è valido e un messaggio di errore in caso contrario.
    """
    if not folder_name:
        return False, "Nome della cartella non valido."
    if not re.match(r'^[^<>:"/\\|?*]+$', folder_name):
        return False, "Nome della cartella contiene caratteri non validi."
    if len(folder_name) > 255:
        return False, "Nome della cartella troppo lungo."
    if folder_name in ["CON", "PRN", "AUX", "NUL"] or re.match(r"^(COM[1-9]|LPT[1-9])$", folder_name):
        return False, "Nome della cartella è un nome riservato."
    if folder_name.endswith(' ') or folder_name.endswith('.'):
        return False, "Nome della cartella non può terminare con uno spazio o un punto."
    return True, ""

def create_custom_folder(base_path):
    """
    Permette di creare una cartella con nome personalizzato.

    Args:
        base_path (str): Il percorso base dove creare la cartella.
    """
    while True:
        response = get_valid_response("Vuoi creare un'altra cartella? (yes/no): ")
        if response == 'no':
            print("Nessuna altra cartella creata. Programma terminato.")
            break
        elif response == 'yes':
            custom_name = input("Inserisci il nome della cartella: ").strip()
            is_valid, error_message = is_valid_folder_name(custom_name)
            if is_valid:
                create_folder(base_path, custom_name)
            else:
                print(error_message)

def main():
    """
    Funzione principale del programma. Legge le configurazioni, richiede input all'utente e crea le cartelle.
    """
    print("Benvenuto nel generatore di cartelle!")
    folders_documenti, folders_software = read_folders_from_ini()
    base_path = read_base_path_from_ini()
    if not base_path:
        print("Percorso base non configurato correttamente. Programma terminato.")
        return
   
    folder_type = get_valid_folder_type(f"Vuoi generare cartelle per documenti ('d') o software ('s')? ")
    generate_folders(folder_type, base_path, folders_documenti, folders_software)
    create_custom_folder(base_path)

if __name__ == "__main__":
    main()
