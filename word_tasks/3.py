class Artist:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Song:
    def __init__(self, name, artist: list[Artist]):
        self.name = name
        self.artists = artist

    @property
    def artist(self):
        if len(self.artists) > 1:
            return 'Different artists'
        else:
            return '{}'.format(self.artists[0])


class Album:
    def __init__(self, name: str, songs: list[Song], artists: list[Artist] = []):
        self.name = name
        self.songs = songs

        self.artists = []
        self.artists.extend(artists)
        for song in self.songs:
            for artist in song.artists:
                if artist not in self.artists:
                    self.artists.append(artist)


class Playlist:
    def __init__(self, songs: list[Song] = []):
        self.songs = []
        self.songs.extend(songs)

    def add_song(self, song: Song):
        if song not in self.songs:
            self.songs.append(song)

    def show_playlist(self):
        for song in self.songs:
            print('{} - {} из альбома/ов {}'.format(song.name, song.artist, from_album(song)))


def from_album(song):
    albums_names = ''
    for album in albums:
        if song in album.songs:
            albums_names += '{}, '.format(album.name)

    return albums_names[:-2]


artist1 = Artist('Amogus')
artist2 = Artist("Avtobus")

song1 = Song('song1', [artist1])
song2 = Song('song2', [artist1])
song3 = Song('song3', [artist2])
song4 = Song('song4', [artist1, artist2])

album1 = Album('Amogus tribute', [song1, song2])
album2 = Album('Collab', [song2, song4, song3])
albums = [album1, album2]

playlist = Playlist()
playlist.add_song(song1)
playlist.show_playlist()

print('################')

playlist1 = Playlist()
playlist1.add_song(song2)
playlist1.add_song(song4)
playlist1.show_playlist()
