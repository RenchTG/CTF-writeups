ops = 'rrrreeeerrrrrreerrwwwwqqwwrrrrrrrrrrrreeeerreeeeeeeeeerrrreerreerreeqqeerreerrwwrrrrrreeeeeerreeeerrwwrrrreeeeeeeeqqwwqqeeeeeeqqqqqqeeeerrrrrrrrrrreeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
binary = ''
# r = a&2 > 0 and a is even
# e = a&2 == 0 and a is even
# w = a&2 == 0 and a is odd
# q = a&2 > 0 and a is odd

for i in ops[::-1]:
    if i == 'w':
        binary += '01'
    elif i == 'r':
        binary += '10'
    elif i == 'e':
        binary += '00'
    elif i == 'q':
        binary += '11'

print(int(binary,2))