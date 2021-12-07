from Room import Room

class Airlock(Room):

    def __init__(self):
        Room.__init__(self, (50, 83, 95), willSpawnEnemies = False)
        
