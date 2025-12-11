from pathlib import Path
import textwrap

path = Path(__file__).parent / "input.txt"

def check_range(start: int, end: int) -> int:

    aux = 0
    
    for i in range(start, end+1):
        num = str(i).strip()
        size = len(num)
        
        for j in range(1, (size//2)+1):
            if True:
                num_list = textwrap.wrap(num, j)
                total = 0
                for pattern in num_list:
                    if pattern == num_list[0]:
                        total += 1

                if total == size/j: 
                    print(total, ", ", j)
                    print(i)
                    aux += i
                    break
            
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