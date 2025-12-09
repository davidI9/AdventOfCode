from pathlib import Path

path = Path(__file__).parent / "input.txt"

class Entrance:
    def __init__(self):
        self.dial = 50
    
    def Right(self, clicks: int) -> int:
        aux = 0
        for i in range(0, clicks):
            self.dial += 1
            self.dial = self.dial % 100
            if self.dial == 0:
                aux+=1
        return aux

    def Left(self, clicks: int) -> int:
        aux = 0
        for i in range(0, clicks):
            self.dial -= 1
            self.dial = self.dial % 100
            if self.dial == 0:
                aux+=1
        return aux
        

if __name__ == '__main__':
    f = open(path, "r")
    line = None
    count = 0
    entrance = Entrance()

    while(line != ""):
        line = str(f.readline())
        if line != "":
            if str(line)[0] == 'R':
                count += entrance.Right(int(line.split('R')[1]))
            else:
                count += entrance.Left(int(line.split('L')[1]))
        
    
    f.close()
    print(count)