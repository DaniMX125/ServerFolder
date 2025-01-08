# Uso del progetto ServerFolder

## Eseguire il progetto
1. Assicurati di avere Python 3.7 o superiore installato sul tuo sistema.
2. Clona il repository del progetto (se non lo hai già fatto):
   ```bash
   git clone <url-del-repository>
   cd ServerFolder
   ```

3. Esegui lo script principale:
   ```bash
   python src/main.py
   ```

## Funzionalità principali
- **Generazione di cartelle predefinite:**
  - Se scegli "documenti", lo script creerà cartelle come `Documenti`, `Fatture`, e `Contratti`.
  - Se scegli "software", lo script creerà cartelle come `Progetti`, `Codice`, e `Backup`.

- **Creazione di cartelle personalizzate:**
  - Dopo aver completato la generazione di cartelle predefinite, lo script ti chiederà se desideri creare una cartella con un nome personalizzato.

## Creazione di un eseguibile
Per distribuire il progetto come un unico file eseguibile:
1. Installa **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. Crea l'eseguibile con il seguente comando:
   ```bash
   pyinstaller --onefile src/main.py
   ```

3. Troverai l'eseguibile nella directory `dist/` del progetto.

## Errori comuni
- **Python non trovato:** Assicurati che Python sia installato e aggiunto al `PATH` di sistema.
- **Dipendenze mancanti:** Verifica di aver installato le dipendenze elencate in `requirements.txt` (se presenti).
- **Problemi con i permessi:** Assicurati di avere i permessi necessari per creare cartelle nella directory in cui viene eseguito lo script.

## Suggerimenti
- Per testare il progetto in un ambiente isolato, utilizza un ambiente virtuale:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Su Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

- Modifica i nomi delle cartelle predefinite modificando le liste all'interno del file `src/main.py`.

# Usage

## Creazione di un eseguibile

Per creare un singolo file eseguibile chiamato `ServerFolder.exe` utilizzando `pyinstaller`, esegui il seguente comando nel terminale:

```sh
pyinstaller --onefile --name ServerFolder src/main.py
```

Parametri utilizzati:
--onefile: Crea un singolo file eseguibile.
--name ServerFolder: Specifica il nome dell'eseguibile risultante.
main.py: Il percorso del file principale del tuo progetto.

Assicurati di eseguire questo comando nella directory principale del tuo progetto, dove si trova la cartella

Se hai bisogno di ulteriori informazioni, consulta il file `README.md`.
