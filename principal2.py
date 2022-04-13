import os
import re
from pathlib import Path
import mimetypes

mimetypes.init()

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def main():
     try:
         #con la ruta creamos un objeto del tipo Path
         directorio_down = Path(get_download_path())
         print(f'\nDirectorio: {directorio_down}\n')
         #patron de expresión regular.
         patron = r".*[0-9].*"
         # Si es un directorio entonces miramos su contenido.
         if directorio_down.is_dir():
             for index, unfichero in enumerate(directorio_down.iterdir()):
                 if unfichero.is_file():
                    if re.match(patron, unfichero.name):
                        nombre = unfichero.name.lower()
                    else:
                        nombre = unfichero.name.upper()
                    # esto se puede poner en una sola linea.
                    # nombre = nombre = unfichero.name.lower() if re.match(patron, unfichero.name) else nombre = unfichero.name.upper()
                    if mimetypes.guess_type(unfichero)[0] =='image/jpeg':
                        if index % 2 == 0:
                            print (index, f"=> \"{nombre}\"")
                        else:
                            print(index, nombre)

     except Exception as exception:
         print(exception)


if __name__ == "__main__":
    main()

