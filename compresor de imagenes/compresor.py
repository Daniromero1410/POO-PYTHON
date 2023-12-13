from PIL import Image

import os

downloadsFolder = "direccion de la carpeta a la que quieres ir a buscar los elementos"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name,extension = os.path.splitext(downloadsFolder+filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+"Comprimida_"+filename,optimize=True, quality= 60)
