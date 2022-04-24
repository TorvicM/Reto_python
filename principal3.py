import os
from pathlib import Path
config_dir = ".config/diogenes"



def crearDirConfiguracion(directorio_crear Path):
    print("crearDirConfiguracion()")
    os.mkdir(directorio_crear)

def existeConfiguracion():
    if os.name == 'nt':
        print(f"Home: {os.path.expanduser('~')}")
        ruta = Path(os.path.join(os.path.expanduser('~'), config_dir))
        if ruta.is_dir():
            print(f"Exite: {ruta}")
        else:
            print(f"NO Existe: {ruta}")
            crearDirConfiguracion(ruta)

def main():
    print("Main")
    existeConfiguracion()



if __name__ == "__main__":
    main()