class SizeClass: # Simple class which holds the Size of the board
    def __init__(self, w, h):
        self.__Width = w
        self.__Height = h
        
    @property
    def Width(self):
        return self.__Width
    
    @property
    def Height(self):
        return self.__Height

class Board:
    def __init__(self, W = None, H = None):
        self.__Data = []
        self.Moves = []
        self.__Size = SizeClass(W or 15, H or 15)
        for _ in range(self.Size.Width * self.Size.Height):
            self.__Data.append(0)
    
    def Get(self, x, y): # Gets the piece at A(x, y)
        if x not in range(0, self.Size.Height) or y not in range(0, self.Size.Width):
            return None
        return self.__Data[x * self.Size.Height + y]
    
    def Set(self, x, y, v, Force = False): # Sets the piece at A(x, y) and stores it in the Moves array (optimization)
        #print(str(x) + " " +str(y))
        if Force == False and self.Get(x, y) != 0:
            raise ValueError
        if v != 0:
            self.Moves.append([x, y, v])
        else:
            self.Moves.remove([x, y, self.__Data[x * self.Size.Height + y]])
        self.__Data[x * self.Size.Height + y] = v
    
    @property
    def Size(self):
        return self.__Size