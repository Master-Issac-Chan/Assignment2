# create your SongList class in this file
import csv

class SongList:
    #songlist variables
    def __init__(self, title, artist, year, is_required, song_list=[]):
        super().__init__(title, artist, year, is_required)
        self.songs = song_list

    def __str__(self):
        if len(self.songs) > 0:
            #print songlist contents
            for song in self.songs:
                if song == self.songs[-1]:
                    return("{}\n".format(song))
                else:
                    print(song)
        else:
            print("Empty")

    def load_songs(self, song_file=''):
        song_list = []
        song_file = open("songs.csv", "r")
        for element in song_file:
            self.songs.append(element.split(','))
        for i in self.songs:
            i[3] = i[3].strip('\n')
        song_list.append(self.songs)
        print(song_list)
        song_file.close()

    def song_sort(self, sort_by=''):
        if sort_by = 'title':
            self.songs.sort(key=lambda song: song.title)
        elif sort_by = 'artist':
            self.songs.sort(key=lambda song: song.artist)
        elif sort_by = "year":
            self.songs.sort(key=lambda song: song.year)

    def song_add(self, new_song):


    pass
