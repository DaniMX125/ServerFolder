# SERVER FOLDER

**ServerFolder** è un progetto Python che permette di generare cartelle per documenti o software in modo interattivo.

## Funzionalità
- Creazione di cartelle predefinite (documenti o software).
- Possibilità di creare cartelle con nomi personalizzati.
- Struttura modulare e ottimizzata per PyInstaller.

## Come eseguire il progetto
1. Clona il repository:
   ```bash
   git clone <url-del-repository>
   cd ServerFolder
   ```

2. Installa le dipendenze (se necessarie):
   ```bash
   pip install -r requirements.txt
   ```

3. Esegui lo script:
   ```bash
   python src/main.py
   ```

## Creazione di un eseguibile con PyInstaller
1. Installa PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Crea l'eseguibile:
   ```bash
   pyinstaller --onefile src/main.py
   ```

3. L'eseguibile sarà generato nella directory `dist/`.

## Struttura del progetto
```
ServerFolder/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── docs/
    └── usage.md
