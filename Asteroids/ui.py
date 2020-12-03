from game import InvalidCoordinates
class UserInterface:
    def __init__(self, grid, gameserv):
        self.Grid = grid
        self.GameService = gameserv

    def ReadInput(self):
        Input = input("> ")
        Input = Input.upper()
        Options = Input.split()
        if len(Options) == 0:
            return [0]
        return Options
    
    def FireMessages(self, Answer):
        # Input: Answer code from the Fire command in the GameService
        # Output: Code representing whether this move will count or not + visual output on the console
        if Answer == 0:
            print("You cannot fire upon earth!")
        elif Answer == 1:
            print("Alien ship destroyed!")
        elif Answer == 2:
            print("You cannot destroy asteroids!")
            return 0
        elif Answer == 3:
            print("Missed!")
        elif Answer == 4:
            print("You have already fired there!")
            return 0
        return 1
    
    def CheatShow(self):
        self.Grid.Cheat()
        print(self.Grid)
        self.Grid.Cheat()
        return 0

    def Start(self):
        while True:
            try:
                print(self.Grid)
                Options = self.ReadInput()
                if Options[0] == "FIRE" and len(Options) == 2:
                    Coords = Options[1]
                    Answer = self.GameService.Fire(Coords) # Executes the command
                    FinalAnswer = self.FireMessages(Answer) # Shows information related to ran command
                    if FinalAnswer == 0:
                        continue
                elif Options[0] == "CHEAT" and len(Options) == 1:
                    self.CheatShow()
                    continue
                else:
                    print("Command not found!")
                    continue
                self.GameService.Relocate()
                Winner = self.GameService.CheckWin()
                if Winner == -1:
                    print("The aliens have won")
                    break
                elif Winner == 1:
                    print("You have won")
                    break
            except InvalidCoordinates:
                print("Invalid coordinates!")
                