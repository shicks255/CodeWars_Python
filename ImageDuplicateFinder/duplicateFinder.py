# !python3

import os
import sys
import gc
import datetime
from pathlib import Path
from typing import Dict, List, Tuple

from PIL import Image

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

def comparePixels(image1: Image, image2: Image):

    values1: List = list(image1.getdata())
    values2: List = list(image2.getdata())

    numberOfMisses:int = 0
    length1:int = len(values1)
    length2:int = len(values2)
    if length1 != length2:
        return False

    # 1/20th of the pixels are off
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
            return False

    del values1
    del values2
    return True

path: Path = Path('F:\\backgrounds_winter')
# path: Path = Path(os.getcwd())

print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' - Starting duplicate image finder in ' + str(path))
traversePath(path)

for fileName in map:
    collected: int = gc.collect()
    print('Garbage Collected ' + str(collected) + ' objects')
    img: Image = map[fileName];
    for fn in map:
        if fileName != fn:
            if comparePixels(img, map[fn]):
                print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' --Possible Match: ' + str(fileName) + ' and ' + str(fn))

print(datetime.datetime.now().strftime('\n%m-%d-%y %H:%M:%S:%f%p') + ' - Finished scanning images for duplicates')

