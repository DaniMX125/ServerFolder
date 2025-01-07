import os

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

def get_valid_input(prompt, valid_options):
    """Richiede un input valido all'utente, accettando varianti flessibili."""
    valid_responses = {
        "yes": ["yes", "y", "sì", "si"],
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
        folders = ["Documenti", "Fatture", "Contratti"]
    elif folder_type == 's':
        folders = ["Progetti", "Codice", "Backup"]

    if not folders:
        print("Tipo di cartella non valido. Programma terminato.")
        return

    for folder in folders:
        response = get_valid_input(f"Vuoi creare la cartella '{folder}'? (yes/no): ", ["yes", "no"])
        if response == 'yes':
            create_folder(folder)
        elif response == 'no':
            print(f"{folder} non creata.")
        else:
            print(f"Non puoi saltare questa decisione! Riprova.")

def create_custom_folder():
    """Permette di creare una cartella con nome personalizzato."""
    while True:
        response = get_valid_input("Vuoi creare una cartella nominativo? (yes/no): ", ["yes", "no"])
        if response == 'no':
            print("Nessuna cartella nominativo creata. Programma terminato.")
            break
        elif response == 'yes':
            custom_name = input("Inserisci il nome della cartella: ").strip()
            if custom_name:
                create_folder(custom_name)
            else:
                print("Nome della cartella non valido. Riprova.")

def main():
    print("Benvenuto nel generatore di cartelle!")
    folder_type = get_valid_input(
        "Vuoi generare cartelle per documenti ('d') o software ('s')? ",
        ["d", "s"]
    )
    generate_folders(folder_type)
    create_custom_folder()

if __name__ == "__main__":
    main()
