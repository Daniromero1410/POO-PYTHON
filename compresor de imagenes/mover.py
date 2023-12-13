from PIL import Image

import os

downloadsFolder = "/Users/57310/Downloads/"
carpeta_de_Img = "/Users/57310/Pictures/"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name,extension = os.path.splitext(downloadsFolder+filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(downloadsFolder+filename)
            picture.save(carpeta_de_Img+"Comprimida_"+filename,optimize=True, quality= 60)
            os.remove(downloadsFolder+filename)
            print(name+":"+extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/57310/Music"
            os.rename(downloadsFolder+ filename, musicFolder+ filename)

        if extension in [".pdf"]:
            docsfolder = "/Users/57310/Documents/PDF"
            os.rename(downloadsFolder + filename, docsfolder + filename)






