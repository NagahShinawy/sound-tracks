"""
created by Nagaj at 02/05/2021
"""
from album import Album
from artist import Artist
from song import Song

if __name__ == '__main__':
    john = Artist("John")
    james = Artist("James")
    alb1 = Album("Alb", john)
    alb2 = Album("Alb2", john)
    song1 = Song("SONG1", john, alb1)
    song2 = Song("SONG2", john, alb1)
    song3 = Song("SONG3", john, alb1)
    song4 = Song("SONG4", john, alb1)

    # john.add_song(song1)
    # john.add_song(song2)
    # print(john.songs)
    # print("#" * 100)
    # john.add_album(alb1)
    # print(john.albums)
    john.add_song_to_album(song4, alb1)
    john.add_song_to_album(song3, alb1)
    john.add_song_to_album(song1, alb2)
    john.add_song_to_album(song2, alb2)
    print(john.items)
