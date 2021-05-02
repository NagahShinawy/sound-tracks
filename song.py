"""
created by Nagaj at 02/05/2021
"""


class Song:

    def __init__(self, song_name, author, album):
        self.song_name = song_name
        self.author = author
        self.album = album

    def __repr__(self):
        return f"<{self.song_name}>-<{self.author}>"

    def to_json(self):
        return {"song": self.song_name, "album": self.album, "author": self.author}