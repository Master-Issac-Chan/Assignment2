# create your SongList class in this file
from song import Song
import csv
from operator import itemgetter

class SongList:
    songs = []
    #songlist variables
    def __init__(self):
        pass

    # def __str__(self):
    #     if len(self.songs) > 0:
    #     #print songlist contents
    #         tmp_lst = []
    #         for song in self.songs:
    #             tmp_lst.append(song)
    #         return tmp_lst
    #     else:
    #         return str("Empty")

    def load_songs(self):
    #opens songs file in read mode and stores them into a temporary list
        temporary_list = []
        songRead = open("songs.csv", "r")
        for element in songRead:
            temporary_list.append(element.split(','))
        song_listing = []
        #puts contents from temporary list into another list
        for i in temporary_list:
            i[3] = i[3].strip('\n')
            song_listing.append(i)
        # print(self.songs)
        songRead.close()
        self.songs = song_listing
        return song_listing

    def song_add(self, new_song):
    #adds new songs and stores them
        new_song = new_song + '\n'
        append_file = open('songs.csv','a')
        new_song.write(append_file)

    def on_change(self, sort_by=''):
    #sorts the songs by title, artist or year using itemgetter function
        self.load_songs()
        if sort_by == 'title':
            key = 0
        elif sort_by == 'artist':
            key = 1
        else:
            key = 2
        print(str(key))
        test = sorted(self.songs, key = itemgetter(key))
        return test

    def song_learned_count(self, learn_count = 0):
    #songs learn counter
        for song in self.songs:
            if song[3] == "y":
                learn_count += 1
        print("{} songs learned".format(learn_count))

    def song_not_learned_count(self, not_learned_count):
    #songs not learned counter
        for song in self.songs:
            if song[3] == "n":
                not_learned_count += 1
        print("{} songs yet to learn.".format(not_learned_count))

    def song_saver(self, title, artist, year, is_required):
    #saves the songs when entered (input)
        song_edit = open("songs.csv", "a")
        format_line = title+","+artist+","+year+","+is_required+"\n"
        song_edit.write(format_line)
        song_edit.close()

    def song_marked_learned(self,index_song):
    #marks songs as learned
        list_song = self.load_songs()
        new_song = list_song[index_song]
        new_song[3] = 'y'
        list_song[index_song]= new_song
        songWrite = open("songs.csv", "w+")
        songWrite.truncate()
        for e in list_song:
            format_string = str(e[0] + ',' + e[1] + ',' + e[2] + ',' + e[3]+ '\n')
            songWrite.writelines(format_string)



