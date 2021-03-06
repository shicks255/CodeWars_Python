# !python3

import os
import sys
import datetime
from pathlib import Path
from typing import Dict, List, Tuple

from PIL import Image
from PIL import ImageStat

map: Dict[str, Image.Image] = {}

def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def traversePath(path: Path):
    for file in path.iterdir():
        if (file.is_dir()):
            traversePath(file)
        if (file.is_file()):
            filename_data: Tuple[str, str] = os.path.splitext(file)
            # filename, ext = os.path.splitext(file)
            ext: str = filename_data[1]
            filename: str = filename_data[0]
            if ext.lower() == '.jpg' or ext.lower() == '.jpeg' or ext.lower() == '.png':
                try:
                    img: Image = Image.open(file)
                    map[filename] = img
                    # values: List = list(img.getdata())
                    # print(get_size(values))
                    # map[filename] = values
                    # print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' - adding file ' + filename)
                except IOError as err:
                    print(err)
                    pass

def comparePixels2(image1: Image, image2: Image):
    stat1: ImageStat = ImageStat.Stat(image1)
    stat2: ImageStat = ImageStat.Stat(image2)

    sum1: Tuple[int, int, int] = stat1.sum
    sum2: Tuple[int, int, int] = stat2.sum

    dif1: int = abs(sum1[0] - sum2[0])
    dif2: int = abs(sum1[1] - sum2[1])
    dif3: int = abs(sum1[2] - sum2[2])

    if dif1 > 100_000:
        del sum1
        del sum2
        return False
    if dif2 > 100_000:
        del sum1
        del sum2
        return False
    if dif3 > 100_000:
        del sum1
        del sum2
        return False

    del sum1
    del sum2
    return True

def comparePixels(image1: Image, image2: Image):

    values1: List = list(image1.getdata())
    values2: List = list(image2.getdata())

    numberOfMisses:int = 0
    length1:int = len(values1)
    length2:int = len(values2)

    if length1 != length2:
        yield False
        # return False

    missThreshhold:int = length1//50

    for x in range(length1):
        rgb1:Tuple[int,int,int] = values1[x]
        rgb2:Tuple[int,int,int] = values2[x]
        pixelValue1:int = rgb1[0] + rgb1[1] + rgb1[2]
        pixelValue2:int = rgb2[0] + rgb2[1] + rgb2[2]
        pixelDifference:int = pixelValue1 - pixelValue2
        if pixelDifference < 0:
            pixelDifference = -pixelDifference

        if pixelDifference > 100:
            numberOfMisses += 1
        if numberOfMisses > missThreshhold:
            del values1
            del values2
            yield False
            # return False

    del values1
    del values2
    # return True
    yield True

# path = Path(os.getcwd())
path = Path("F:\\backgrounds_winter")
print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' - Starting duplicate image finder in ' + str(path))
traversePath(path)

for fileItem in map:
    pixelValues = map[fileItem]
    for fi in map:
        if fileItem != fi:
            a = comparePixels(pixelValues, map[fi])
            if next(a):
                print('Possible Match: ' + str(fileItem) + ' and ' + str(fi))
            # if comparePixels2(pixelValues, map[fi]):

print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' - Finished scanning images for duplicates')

