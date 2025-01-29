import configparser
import os

def read_folders_from_ini():
    """
    Legge le liste di cartelle dal file settings.ini.

    Restituisce due liste: una per le cartelle dei documenti e una per le cartelle del software.
    Se il file settings.ini non esiste o non è scritto correttamente, restituisce due liste vuote.

    Returns:
        tuple: Due liste contenenti i nomi delle cartelle per documenti e software.
    """
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.path.dirname(__file__), 'settings.ini')
    
    if not os.path.exists(ini_path):
        return [], []

    config.read(ini_path)
    
    try:
        documenti = config.get('folders', 'documenti').split(', ')
        software = config.get('folders', 'software').split(', ')
    except (configparser.NoSectionError, configparser.NoOptionError):
        return [], []
    
    return documenti, software


def read_base_path_from_ini():
    """
    Legge il percorso base dal file settings.ini.

    Restituisce il percorso base come stringa.
    Se il file settings.ini non esiste o non è scritto correttamente, restituisce una stringa vuota.

    Returns:
        str: Il percorso base per creare le cartelle.
    """
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.path.dirname(__file__), 'settings.ini')
    
    if not os.path.exists(ini_path):
        return ""

    config.read(ini_path)
    
    try:
        base_path = config.get('path', 'base_path')
    except (configparser.NoSectionError, configparser.NoOptionError):
        return ""
    
    return base_path