"""
Name: Issac Chan
Date: 30 December 2018
Brief Project Description: CP1404 Assignment 2
GitHub URL: https://github.com/Master-Issac-Chan/Assignment2
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
# Create your main program in this file, using the SongsToLearnApp class

from songlist import SongList

class SongsToLearnApp(App):

    def build(self):
        #GUI creation
        self.title = "Songs To Learn version 1"
        self.root = Builder.load_file('app.kv')
        self.sort_by = "Title"
        self.create_kv_buttons()

        #self.root.ids.bottom_text.text = 'bottom kek m8'
        # Above builds the general GUI and starting sort by method.
        return self.root


    def create_kv_buttons(self, tr_lst=[]):
        self.root.ids.kv_buttons.clear_widgets()
        lst=[]
        lst = self.display_list()
        if tr_lst != []:
            print(tr_lst)
            lst = tr_lst
        uButton = Button
        learned = 0
        not_learned = 0
        for song in lst:
            if song[3] == 'n':
                not_learned += 1
                uButton = Button(text='"{}" by {} ({})'.format(song[0], song[1], song[2]))
                uButton.bind(on_release=self.learned)
            if song[3] == 'y':
                learned += 1
                uButton = Button(text='"{}" by {} ({}) (learned)'.format(song[0], song[1], song[2]))
                uButton.state = 'down'
                uButton.bind(on_release=self.learned)

            self.root.ids.top_text.text = 'Songs Learned: {0}, Not Learned: {1}'.format(learned,not_learned)


            # builds button for each song based on if song is learned.
            self.root.ids.kv_buttons.add_widget(uButton)
            # add the button to the "kv_buttons" using add_widget()

    def add_new_song(self, title, artist, year, is_required):
        #song adding
        songlist = SongList()
        # new_song = title+","+artist+","+year+","+is_required
        songlist.song_saver(title, artist, year, is_required)
        print(title+","+artist+","+year+","+is_required)
        self.create_kv_buttons()

    def input_song(self):
        #song details input
        title = self.root.ids.kv_song_title.text
        artist = self.root.ids.kv_song_artist.text
        year = self.root.ids.kv_song_year.text
        self.add_new_song(title,artist,year,is_required='n')

        #error check


    def clear_input(self):
        #clear input function
        self.root.ids.kv_song_title.text = ''
        self.root.ids.kv_song_artist.text = ''
        self.root.ids.kv_song_year.text = ''
        # title = ''
        # artist = ''
        # year = ''

    def display_list(self):
        #displays current song list
        tmp_var = SongList().load_songs()
        return tmp_var

    def sort_by(self):
        pass

    def change_sorting(self, on_change_atr):
        obj = SongList()
        var1 = obj.on_change(on_change_atr)
        self.create_kv_buttons(var1)

    def learned(self, test_arg):
        #marks songs as learnt
        test_arg.state = 'down'
        song_list = SongList().load_songs()
        index = 0
        loop_counter = 0
        if '(learned)' in test_arg.text:
            self.root.ids.bottom_text.text = 'song already learned'
        else:
            self.root.ids.bottom_text.text = 'song learned'

        #searches through list for songs
        for song in song_list:
            format_string = str('"'+song[0]+'" by '+song[1]+' ('+song[2]+')')
            print(test_arg.text)
            print(format_string)
            if test_arg.text in format_string:
                index = loop_counter
            loop_counter += 1
        SongList().song_marked_learned(index)


        print(str(index))

SongsToLearnApp().run()
