from PIL import Image

import os

downloadsFolder = "direccion de la carpeta a la que quieres ir a buscar los elementos"
carpeta_de_Img = "direccion de la carpeta a la que quieres ir a buscar los elementos"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name,extension = os.path.splitext(downloadsFolder+filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(downloadsFolder+filename)
            picture.save(carpeta_de_Img+"Comprimida_"+filename,optimize=True, quality= 60)
            os.remove(downloadsFolder+filename)
            print(name+":"+extension)

        if extension in [".mp3"]:
            musicFolder = "direccion de la carpeta a la que quieres ir a buscar los elementos"
            os.rename(downloadsFolder+ filename, musicFolder+ filename)

        if extension in [".pdf"]:
            docsfolder = "/direccion de la carpeta a la que quieres ir a buscar los elementos"
            os.rename(downloadsFolder + filename, docsfolder + filename)






