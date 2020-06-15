class Song():
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.points = 0

    def getName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points
