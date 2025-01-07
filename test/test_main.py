import unittest
from src.main import create_folder

class TestMain(unittest.TestCase):
    def test_create_folder(self):
        # Test per verificare che la funzione non generi errori
        folder_name = "test_folder"
        create_folder(folder_name)
        self.assertTrue(os.path.exists(folder_name))
        # Pulizia: rimuove la cartella creata durante il test
        if os.path.exists(folder_name):
            os.rmdir(folder_name)

if __name__ == "__main__":
    unittest.main()
