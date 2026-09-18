class playlists:

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"playlist '{self.name}' ('{self.genre}' genre) has been created.")

    # Step 2: Add a song to the playlist
    def add_song(self, song):
        self.song.append(song)
        print(f"'{song}' has been added to the playlist '{self.name}'.")

    # Step 3: Remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' has been removed from the playlist '{self.name}'.")

    # Step 4: Display the playlist details
    def display_playlist(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f" {i}. {song}")
        else:
            print(" The playlist is empty.")

    # Step 5: Destructor: runs automatically when the playlist object is deleted
    def __del__(self):
        print(f"playlist '{self.name}' has been deleted.")

    # Object creation (constructor fires here)
    my_playlist = Playlist ("Road Trip Mix", "Pop")
     
