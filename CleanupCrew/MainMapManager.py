import random
from Room import Room
from Airlock import Airlock


# The main purpose of the MMM is to host a collection of (room) scenes, and link them together

class MainMapManager:

    def __init__(self, numberOfRooms):
        self.airlock = Airlock() # Airlock room scene will go here
        self.airlock.MainMapManager = self
        self.bossRoom = None
        self.numberOfRooms = numberOfRooms
        self.numberOfDrives = 3
        self.GREY = (115, 115, 115)
        self.dir = None

        self.mapMatrices = []
        for row in range((numberOfRooms // 2) + 1):
            self.mapMatrices.append([0] * ((numberOfRooms // 2) + 1))
        # /// IMPORTANT NOTE ///
        # mapMatrices coordinates follow [row, column] or [y, x]
        self.mapMatrices[0][0] = self.airlock

        self.listOfRooms = []

        self.genRooms(self.numberOfRooms)
        self.connectMatrix()
        self.generateInRooms()

    def genRooms(self, numberOfRooms):
        totalRooms = 0
        while totalRooms < numberOfRooms - 1:
            currentScope = [random.randint(0, numberOfRooms // 2), random.randint(0, numberOfRooms // 2)]
            print(currentScope)
            if self.mapMatrices[currentScope[0]][currentScope[1]] == 0:
                if len(self.surroundingOpenRooms(currentScope[0], currentScope[1])) > 0:
                    self.mapMatrices[currentScope[0]][currentScope[1]] = Room((99, 27, 52), True)
                    totalRooms += 1
        print(self.mapMatrices)





    def surroundingOpenRooms(self, row, column):
        openRooms = []

        # Check above
        if row > 0 and self.mapMatrices[row - 1][column] != 0:
            openRooms.append([self.mapMatrices[row - 1][column], 'ABOVE'])

        # Check below
        if row < self.numberOfRooms // 2 and self.mapMatrices[row + 1][column] != 0:
            openRooms.append([self.mapMatrices[row + 1][column], 'BELOW'])

        # Check left
        if column > 0 and self.mapMatrices[row][column - 1] != 0:
            openRooms.append([self.mapMatrices[row][column - 1], 'LEFT'])

        # Check right
        if column < self.numberOfRooms // 2 and self.mapMatrices[row][column + 1] != 0:
            openRooms.append([self.mapMatrices[row][column + 1], 'RIGHT'])

        return openRooms


    def connectMatrix(self):
        # Scan through each room -- if there is a room next to it, connect it to its neighbor
        # EXCEPT if its an airlock -- only one enterance/exit to the right

        row = 0
        column = 0
        while row < len(self.mapMatrices):
            column = 0
            print('ROW = ' + str(row))

            while column < len(self.mapMatrices):
                print('COLUMN = ' + str(column))

                if row == 0 and column == 0:
                    # This room is the airlock
                    self.mapMatrices[row][column].assignRight(self.mapMatrices[row][column + 1])
                    self.mapMatrices[row][column + 1].assignLeft(self.mapMatrices[row][column])
                    self.mapMatrices[row][column].updateRender()

                if self.mapMatrices[row][column] != 0 and self.mapMatrices[row][column] != self.mapMatrices[0][0]:
                    currWorkingRoom = self.mapMatrices[row][column]
                    print('CURRENT WORKNG ROOM ---- ' + str(currWorkingRoom) + ' ' + str([row]) + ', ' + str([column]) )
                    for room in self.surroundingOpenRooms(row, column):
                        print(str(currWorkingRoom) + ' ' + str(self.surroundingOpenRooms(row, column)))
                        if room[0] != self.mapMatrices[0][0]:
                            if room[1] == 'ABOVE':
                                room[0].assignDown(currWorkingRoom)
                                currWorkingRoom.assignUp(room[0])
                            if room[1] == 'BELOW':
                                room[0].assignUp(currWorkingRoom)
                                currWorkingRoom.assignDown(room[0])
                            if room[1] == 'RIGHT':
                                room[0].assignLeft(currWorkingRoom)
                                currWorkingRoom.assignRight(room[0])
                            if room[1] == 'LEFT':
                                room[0].assignRight(currWorkingRoom)
                                currWorkingRoom.assignLeft(room[0])
                        currWorkingRoom.MainMapManager = self
                        self.listOfRooms.append(currWorkingRoom)
                        # currWorkingRoom.updateRender()
                column += 1
            row += 1
        print('DONE')

    def generateInRooms(self):
        currNumberOfDrives = 0
        while currNumberOfDrives < self.numberOfDrives:
            for room in self.listOfRooms:
                if random.randint(0, 75) == 7:
                    room.hasDataDrive = True
                    currNumberOfDrives += 1

        for room in self.listOfRooms:
            room.updateRender()



    def beginPlayer(self):
        return self.mapMatrices[0][0]


    def printMapMatrix(self):
        i = 0
        while i < len(self.mapMatrices):
            print(str(self.mapMatrices[i]) + '\n')
            i += 1
