import os
import re

FOLDERS_DOCUMENTI = ["Elettrico", "KickOff", "Layout", "Materiali", "Progettazione", "Disegni 3D"]
FOLDERS_SOFTWARE = ["Reti", "Plc", "Hmi", "Controller", "Inverter", "Safety", "Camera", "Fielbus", "Firmware"]

def create_folder(folder_name):
    """Crea una cartella se non esiste."""
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Cartella '{folder_name}' creata con successo.")
        else:
            print(f"La cartella '{folder_name}' esiste già.")
    except Exception as e:
        print(f"Errore durante la creazione della cartella '{folder_name}': {e}")

def get_valid_folder_type(prompt):
    """Richiede un tipo di cartella valido all'utente."""
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
    """Richiede un risposta valida all'utente, accettando varianti flessibili."""
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

def generate_folders(folder_type):
    """Genera le cartelle in base al tipo (documenti o software)."""
    folders = []
    if folder_type == 'd':
        folders = FOLDERS_DOCUMENTI
    elif folder_type == 's':
        folders = FOLDERS_SOFTWARE

    if not folders:
        print("Tipo di cartella non valido. Programma terminato.")
        return

    for folder in folders:
        response = get_valid_response(f"Vuoi creare la cartella '{folder}'? (yes/no): ")
        if response == 'yes':
            create_folder(folder)
        elif response == 'no':
            print(f"{folder} non creata.")
        else:
            print(f"Non puoi saltare questa decisione! Riprova.")

def is_valid_folder_name(folder_name):
    """Verifica se il nome della cartella è valido per Windows."""
    if not folder_name:
        return False, "Nome della cartella non valido."
    if not re.match(r'^[^<>:"/\\|?*]+$', folder_name):
        return False, "Nome della cartella contiene caratteri non validi."
    if len(folder_name) > 255:
        return False, "Nome della cartella troppo lungo."
    return True, ""

def create_custom_folder():
    """Permette di creare una cartella con nome personalizzato."""
    while True:
        response = get_valid_response("Vuoi creare una cartella nominativo? (yes/no): ")
        if response == 'no':
            print("Nessuna cartella nominativo creata. Programma terminato.")
            break
        elif response == 'yes':
            custom_name = input("Inserisci il nome della cartella: ").strip()
            is_valid, error_message = is_valid_folder_name(custom_name)
            if is_valid:
                create_folder(custom_name)
            else:
                print(error_message)


def main():
    print("Benvenuto nel generatore di cartelle!")
    folder_type = get_valid_folder_type(f"Vuoi generare cartelle per documenti ('d') o software ('s')? ")
    generate_folders(folder_type)
    create_custom_folder()

if __name__ == "__main__":
    main()
