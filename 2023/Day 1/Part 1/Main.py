from pathlib import Path
import re

total = 0

p = Path(__file__).with_name('Input.txt')
with p.open('r') as f:
    splitList = f.read().split()
    for x in splitList:
        x = re.findall('\d+', x)
        x = ''.join(x)
        x = int(str(x[0])+str(x[-1]))
        print(x)
        total = total + x
    print(total)