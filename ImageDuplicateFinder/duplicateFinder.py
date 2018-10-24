# !python3

import os
from pathlib import Path

from PIL import Image


def traversePath(path):
    for file in path.iterdir():
        if (file.is_dir()):
            traversePath(file)
        if (file.is_file()):
            filename, ext = os.path.splitext(file)
            if ext.lower() == '.jpg' or ext.lower() == '.jpeg':
                try:
                    img = Image.open(file)
                    print(img)
                except IOError as err:
                    print(err)
                    pass


path = Path(os.getcwd())
print(path)
traversePath(path)



