import os
from tinytag import TinyTag, TinyTagException

def main():
    print("Start")

    tracks = []

    for root, dirs, files, in os.walk("/home/fingadumbledore/Musik/"):
        for name in files:
            if name.endswith((".mp3",".m4a","flac","alac")):
                tracks.append(name)
                try:
                    temp_track = TinyTag.get(root + "" + name)
                    print(temp_track.artist)
                    print(temp_track.title)
                    print(temp_track.samplerate)
                    print(temp_track.album)
                    print(temp_track.albumartist)
                    print(temp_track.audio_offset)
                    print(temp_track.disc_total)
                    print(temp_track.track)
                    print(temp_track.track_total)
                    print(temp_track.disc)
                    print(temp_track.filesize)
                
                except TinyTagException:
                    print("Error")    


main()