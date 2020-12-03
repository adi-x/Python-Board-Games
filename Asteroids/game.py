# service
import random as r
class InvalidCoordinates(Exception):
    pass

class Validation:
    def CheckInt(self, nr):
        try:
            int(nr)
            return True
        except:
            return False
    def ValidateCoordinates(self, Coord):
        if Coord[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G'] or self.CheckInt(Coord[1]) == False or int(Coord[1]) not in range(1, 7 + 1):
            raise InvalidCoordinates

class Game:
    def __init__(self, grid):
        self.Grid = grid
        self.Validation = Validation()
    
    def CheckAdjacentAsteroids(self, x, y, code):
        di = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
        dj = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
        for k in range(9):
            i = di[k] + x
            j = dj[k] + y
            if i in range(0, 7) and j in range(0, 7) and self.Grid.Get(i, j) == code:
                return False
        return True

    def GetRingPositions(self, ring, All = False): # Puts all the coordinates from a ring in a list and returns it
        Positions = []
        for i in range(ring - 1, 7 - ring):
            Positions.append((ring - 1, i))
        for i in range(ring - 1, 7 - ring):
            Positions.append((i, 7 - ring))
        for i in range(ring - 1, 7 - ring + 1):
            Positions.append((7 - ring, i))
        for i in range(ring, 7 - ring):
            Positions.append((i, ring - 1))
        Positions2 = []
        for p in Positions:
            if self.Grid.Get(*p) == 0 or All == True:
                Positions2.append(p)
        return Positions2

    def GridSetup(self):
        # Placing the earth in the middle
        self.Grid.Set(3, 3, 1) 
        # Placing the asteroids
        Count = 0
        while Count < 8:
            x = r.randint(0, 6)
            y = r.randint(0, 6)
            if self.Grid.Get(x, y) != 1 and self.CheckAdjacentAsteroids(x, y, 2) == True:
                self.Grid.Set(x, y, 2)
                Count += 1
        # Placing the alien ships
        PossiblePositions = self.GetRingPositions(1)
        P1 = PossiblePositions.pop(r.randint(0, len(PossiblePositions) - 1))
        P2 = PossiblePositions.pop(r.randint(0, len(PossiblePositions) - 1))
        self.Grid.Set(*P1, 3)
        self.Grid.Set(*P2, 3)
        self.Grid.AlienShips.append([*P1, 1])
        self.Grid.AlienShips.append([*P2, 1])
    
    def Fire(self, Coordinates):
        # Input: Coordinates as a string
        # Output: A code which describes what was at those coords
        # Side effects:
        #  - > Might mark a position as fired upon
        #  - > Might remove a ship and mark a position as fired upon and remove the alien ship from the list of alien ships
        # Exceptions: InvalidCoordinates if the coordinates aren't how they're supposed to be
        # Description: Getting the element at said coordinates and comparing with possible elements
        self.Validation.ValidateCoordinates(Coordinates)
        y = ord(Coordinates[0]) - ord('A')
        x = int(Coordinates[1]) - 1
        Item = self.Grid.Get(x, y)
        if Item == 0: # Empty
            self.Grid.Set(x, y, 4)
            return 3
        if Item == 1: # Earth
            return 0
        if Item == 2: # Asteroid
            return 2
        if Item == 3: # Alien ship
            self.Grid.Set(x, y, 4)
            for Coord in self.Grid.AlienShips:
                if Coord[0] == x and Coord[1] == y:
                    self.Grid.AlienShips.remove(Coord)
                    break
            return 1
        if Item == 4: # Already fired there
            return 4 
    
    def Relocate(self):
        NewCoords = []
        PossiblePositionsRing1 = self.GetRingPositions(1)
        PossiblePositionsRing2 = self.GetRingPositions(2)
        PossiblePositionsRing3 = self.GetRingPositions(3)
        for C in self.Grid.AlienShips: # Placing new alien ships
            P = None
            Ring = 0
            PosV1 = None
            PosV2 = None
            if C[2] == 1: # Checking if the this AlienShip is on ring 1 or 2
                Ring = 1
                PosV1 = PossiblePositionsRing1
                PosV2 = PossiblePositionsRing2
            if C[2] == 2:
                Ring = 2
                PosV1 = PossiblePositionsRing2
                PosV2 = PossiblePositionsRing3
            if r.randint(1, 2) == 1:
                P = PosV1.pop(r.randint(0, len(PosV1) - 1))
            else:
                Ring += 1
                P = PosV2.pop(r.randint(0, len(PosV2) - 1))
            self.Grid.Set(*P, 3)
            NewCoords.append([*P, Ring])
        for Coords in self.Grid.AlienShips: # Removing old ships
            self.Grid.Set(Coords[0], Coords[1], 0)
        self.Grid.AlienShips = NewCoords

    def CheckWin(self):
        if self.Grid.AlienShipCount == 0:
            return 1
        Ring3 = self.GetRingPositions(3, True)
        #print(Ring3)
        for Coords in Ring3:
            if self.Grid.Get(*Coords) == 3:
                return -1
        return 0


