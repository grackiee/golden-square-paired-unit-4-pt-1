class MusicHistory:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.tracks = [] #listening history
    
    def add_tracks(self, track):
        if type(track) != str:
            raise TypeError("Error: invalid type")
        if track == "":
            raise Exception("Error: cannot add empty string as track")
        self.tracks.append(track)

    def list_tracks(self):
        return self.tracks