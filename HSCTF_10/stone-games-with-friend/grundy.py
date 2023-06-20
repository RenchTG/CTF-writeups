import math

def perfect(n):
   sq_root = int(math.sqrt(n))
   if (sq_root*sq_root) == n:
       return sq_root
   else:
       return -1

games = []
f = open('input.txt','r')
g = int(f.readline().strip())
for i in range (g):
    game = f.readline().strip().split()
    n = game[0]
    game.pop(0)
    game = list(map(int,game))
    
    for j in game:
        games.append(j)
games.sort()

out = "["
newgrundys = [0,1]
pattern = [0,1]
index = 0
for i in range (2,1000000000):
    sq_root = perfect(i)
    if sq_root == -1:
        newgrundys.append(pattern[index])
    else:
        newgrundys.append(sq_root)
        if index == 0:
            pattern.insert(len(pattern),sq_root)
            index -= 1
        else:
            pattern.insert(index,sq_root)
    index += 1
    index %= len(pattern)
    if i == games[0]:
        out += '(' + str(i) + ',' + str(newgrundys[i]) + '),'
        games.pop(0)
out = out[:-1:]
out += ']'
print(out)