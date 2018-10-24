# !python3

import os
from pathlib import Path

from PIL import Image

map = {}

def traversePath(path):
    for file in path.iterdir():
        if (file.is_dir()):
            traversePath(file)
        if (file.is_file()):
            filename, ext = os.path.splitext(file)
            if ext.lower() == '.jpg' or ext.lower() == '.jpeg' or ext.lower() == '.png':
                try:
                    img = Image.open(file)
                    values = list(img.getdata())
                    map[file] = values
                except IOError as err:
                    print(err)
                    pass

def comparePixels(pixelList1, pixelList2):
    numberOfMisses = 0
    length1 = len(pixelList1)
    length2 = len(pixelList2)
    if length1 != length2:
        return False

    # 1/20th of the pixels are off
    missThreshhold = int(length1/50)
    for x in range(length1):
        rgb1 = pixelList1[x]
        rgb2 = pixelList2[x]
        pixelValue1 = rgb1[0] + rgb1[1] + rgb1[2]
        pixelValue2 = rgb2[0] + rgb2[1] + rgb2[2]
        pixelDifference = pixelValue1 - pixelValue2
        if pixelDifference < 0:
            pixelDifference = -pixelDifference

        if pixelDifference > 100:
            numberOfMisses += 1
        if numberOfMisses > missThreshhold:
            return False
    return True

path = Path(os.getcwd())
print('Starting duplicate image finder in ' + str(path))
traversePath(path)

for fileItem in map:
    pixelValues = map[fileItem];
    for fi in map:
        if fileItem != fi:
            if comparePixels(pixelValues, map[fi]):
                print('Possible Match: ' + str(fileItem) + ' and ' + str(fi))



