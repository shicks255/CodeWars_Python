# !python 3

import os
import sys
from mutagen.id3 import ID3
import mutagen
from pathlib import Path


# os.chdir("D:\\music\\Owen\\2001 - Owen\\")
# mutagen.File("01 That Which Wasn't Said.mp3")

# file = ID3("01 That Which Wasn't Said.mp3")

def cleanUpTrackNumber(track):
    if ('/' in track):
        track = track[0:track.index('/')]
        if (int(track) < 10 and track[0] != '0'):
            track = '0' + track
    if (len(track) < 2):
        track = '0' + track
    if ('(' in track):
        track = track.replace('(', '')
        track = track.replace(')', '')
        track = track[0:track.index(',')]
        return cleanUpTrackNumber(track)

    return track

def doSomething(path):
    for x in path.iterdir():
        # if its directory, use recursion
        if (x.is_dir()):
            doSomething(x)
        if (x.is_file()):
            musicFile = mutagen.File(Path.absolute(x))
            if (musicFile and type(musicFile) == mutagen.mp3.MP3):
                values = musicFile.values()
                track = ''
                title = ''
                if ('TRCK' in musicFile.keys()):
                    track = mutagen.id3.TRCK(musicFile.get('TRCK'))
                    track = str(track[0])
                    track = cleanUpTrackNumber(track)

                if ('TIT2' in musicFile.keys()):
                    title = mutagen.id3.TIT2(musicFile.get('TIT2'))
                    title = str(title[0])
                # if ('TPE1' in musicFile.keys()):
                #     artist = mutagen.id3.TPE1(musicFile.get('TPE1'))

                if (track and title):
                    newTitle = track + " - " + title;
                    print(newTitle)

            if (musicFile and type(musicFile) == mutagen.mp4.MP4):
                track = ''
                title = ''
                if ('trkn' in musicFile.keys()):
                    track = musicFile.get('trkn')[0]
                    track = str(track)
                    track = cleanUpTrackNumber(track)
                if ('©nam' in musicFile.keys()):
                    title = musicFile.get('©nam')[0]

                if (track and title):
                    newTitle = str(track) + " - " + str(title)
                    print(newTitle)

            if (musicFile and type(musicFile) == mutagen.asf.ASF):
                if ('WM/TrackNumber' in musicFile.keys()):
                    track = str(musicFile.get('WM/TrackNumber')[0])
                    track = cleanUpTrackNumber(track)
                if ('Title' in musicFile.keys()):
                    title = str(musicFile.get('Title')[0])

                if (track and title):
                    newTitle = track + " - " + title
                    print(newTitle)


path = Path('D:\\Music\\');
print(sys.path[0])
doSomething(path)



