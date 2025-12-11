from pathlib import Path

path = Path(__file__).parent / "input.txt"

def check_range(start: int, end: int) -> int:

    aux = 0
    
    for i in range(start, end+1):
        
        size = len(str(i).strip())
        num = str(i).strip()
        valid = False
        
        if size%2 == 0:
            for j in range(0, ((size)//2)):
                if (num[j] != num[((size)//2) +j ]):
                    valid = True
        
        else: valid = True
    
        if valid == False:
            print(num)
            aux+=i
    
    return aux


if __name__ == '__main__':
    
    f = open(path, "r")
    count = 0
    text = f.read()
    
    for id_range in text.split(','):
        
        limits = id_range.split('-')
        count += check_range(int(limits[0]), int(limits[1]))
    
    print(count)
    f.close()