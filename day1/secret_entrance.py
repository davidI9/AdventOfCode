from pathlib import Path

path = Path(__file__).parent / "input.txt"

class Entrance:
    def __init__(self):
        self.dial = 50
    
    def Right(self, clicks: int) -> int:
        self.dial += clicks
        self.dial = self.dial % 100
        if self.dial == 0:
            return 1
        return 0

    def Left(self, clicks: int) -> int:
        self.dial -= clicks
        self.dial = self.dial % 100
        if self.dial == 0:
            return 1
        return 0
        

if __name__ == '__main__':
    f = open(path, "r")
    line = None
    count = 0
    entrance = Entrance()

    while(line != ""):
        line = str(f.readline())
        if line != "":
            print(line[0])
        
            if str(line)[0] == 'R':
                count += entrance.Right(int(line.split('R')[1]))
            else:
                count += entrance.Left(int(line.split('L')[1]))
        
    
    f.close()
    print(count)