import os

home = os.path.expanduser('~')
location = os.path.join(home, 'Downloads')


def directory_check(home, folder):
    # Joins the home directior to the users typed in folder
    folder_path = os.path.join(home,folder)
    # Checks to see if the folder exsists
    folder_check = os.path.isdir(folder_path)
    if folder_check is True:
        # print(folder_path + " +es un directorio valido.")
        return True
    else:
        # print(folder_path + "  is NOT a valid directory")
        return False

if directory_check(home,location):
    print(f'Directorio: {location}\n')

    lista_ficheros = os.listdir(location)
    for ifichero in lista_ficheros:
        print(ifichero)

