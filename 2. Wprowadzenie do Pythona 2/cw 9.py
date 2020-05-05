from file_manager import FileManager

plik = FileManager("text.txt")

FileManager.read_file(plik)
FileManager.update_file(plik, " i dopisany tekst")
FileManager.read_file(plik)
