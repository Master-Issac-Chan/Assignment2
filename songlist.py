# create your SongList class in this file
import csv

class SongList:
    #songlist properties
    def __init__(self, title, artist, year, is_required, song_list=[]):
        super().__init__(title, artist, year, is_required)
        self.songs = song_list

    def __str__(self):
        if len(self.songs) > 0:
            #print songlist
            for song in self.songs:
                if song == self.songs[-1]:
                    return("{}\n".format(song))
                else:
                    print(song)
        else:
            print("Empty")

    def load_songs(self, song_file):



    pass
