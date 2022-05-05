from Room import Room
from MissionAccomplished import MissionAccomplished


class Airlock(Room):

    def __init__(self):
        Room.__init__(self, (50, 83, 95), willSpawnEnemies = False)

    def on_update(self):
        self.dataDriveGroup.update()
        self.doors.update()
        self.activeSprites.update()
        self.player.update()

        if self.MainMapManager.dir.UIandStatsManager.drivesCollected == 3:
            self.MainMapManager.dir.UIandStatsManager.playerHealth = 4
            self.MainMapManager.dir.UIandStatsManager.numberOfBullets = 10
            self.MainMapManager.dir.unpaused = True
            self.MainMapManager.dir.ingame = False
            self.MainMapManager.dir.renderUI = False
            self.MainMapManager.dir.changeScene(MissionAccomplished(self.MainMapManager.dir), None)
