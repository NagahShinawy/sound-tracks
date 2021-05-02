"""
created by Nagaj at 02/05/2021
"""
from album import Album
from song import Song


class Artist:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.albums = []
        self.items = []

    def __repr__(self):
        return f"Artist-<{self.name}>"

    def __contains__(self, item):
        return item in self.songs

    def __getitem__(self, item):
        return self.albums[item]

    def add_album(self, album: Album):
        self.albums.append(album.to_json())

    def add_song(self, song: Song):
        self.songs.append(song.to_json())

    def add_song_to_album(self, song: Song, album: Album):
        album.songs.append(song.to_json())
        alb = album.to_json()
        if alb not in self.items:
            self.items.append(alb)

