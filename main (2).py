from PIL import Image
import os
import random

path = "photo"
size_one = (120, 80)

def select_from_a_folder():
    paths = []
    for directory, folder, files in os.walk(path):
        for i in files:
            paths.append(i)

    return paths

def photo_processing(size, path,file_path):
    print(file_path)
    images = Image.open(f"{path}/{file_path}")
    images.thumbnail(size=size)
    images.save(fp=f"miniatures/{size} {file_path}")
    print(f"{file_path} saved ({size})")

def main():
    paths_image = []
    for file_path in select_from_a_folder():
        paths_image.append(file_path)
    photo_processing((120,80),path,paths_image[0])
    photo_processing((350,250),path,paths_image[1])

if __name__ == "__main__":
    main()
