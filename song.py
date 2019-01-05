# create your Song class in this file
class Song:
    #song.py properties
    def __init__(self, song_Title = '', song_Artist = '', song_Year = 0000, song_Required = False):
        self.title = song_Title
        self.artist = song_Artist
        self.year = song_Year
        self.is_required = song_Required

    def __str__(self):
        #indication of song input status
        if self.is_required == 'y':
            print ("{} by {} of year {} now learned.".format(self.title, self.artist, self.year))
        else:
            print ("{} by {} of year {} entered.".format(self.title, self.artist, self.year))

    # def mark_learned(self):
    #     #check on song 'learned' status
    #     if self.is_required == 'y':
    #         print("Song is already learnt.")
    #     else:
    #         self.is_required = 'y'

    pass
