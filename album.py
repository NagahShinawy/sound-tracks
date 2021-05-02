"""
created by Nagaj at 02/05/2021
"""


class Album:

    def __init__(self, album_name, author):
        self.album_name = album_name
        self.author = author
        self.songs = []

    def __repr__(self):
        return f"<{self.album_name}>-{self.author}"

    def to_json(self):
        return {"album_name": self.album_name, "songs": self.songs, "author": self.author}
