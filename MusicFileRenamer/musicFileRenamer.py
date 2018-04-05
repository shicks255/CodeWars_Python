# !python 3

import os
import sys
from mutagen.id3 import ID3
from mutagen.id3 import TextFrame
import mutagen
from pathlib import Path


# os.chdir("D:\\music\\Owen\\2001 - Owen\\")
# mutagen.File("01 That Which Wasn't Said.mp3")

# file = ID3("01 That Which Wasn't Said.mp3")

def doSomething(path):
    for x in path.iterdir():
        # if its directory, use recursion
        if (x.is_dir()):
            doSomething(x)
        if (x.is_file()):
            musicFile = mutagen.File(Path.absolute(x))
            if (musicFile):
                values = musicFile.values()
                track = ''
                title = ''
                if ('TRCK' in musicFile.keys()):
                    track = mutagen.id3.TRCK(musicFile.get('TRCK'))
                if ('TIT2' in musicFile.keys()):
                    title = mutagen.id3.TIT2(musicFile.get('TIT2'))
                # if ('TPE1' in musicFile.keys()):
                #     artist = mutagen.id3.TPE1(musicFile.get('TPE1'))

                if (track and title):
                    newTitle = track.text[0] + " - " + title.text[0];
                    print(newTitle)

print(sys.path[0])

path = Path('.');
doSomething(path)



