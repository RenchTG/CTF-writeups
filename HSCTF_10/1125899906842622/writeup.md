# Challenge Info:

* **Challenge Name:** 1125899906842622

* **Challenge Category:** rev

* **Challenge Author:** ewang

* **Challenge Description:** I found this credit card on the floor!

* **Files Provided:** 1125899906842622.py

# Recon: 

To begin we are given a very brief python script. Here it is in its entirety.

```python
a = int(input())
t = a
b = 1
c = 211403263193325564935177732039311880968900585239198162576891024013795244278301418972476576250867590357558453818398439943850378531849394935408437463406454857158521417008852225672729172355559636113821448436305733721716196982836937454125646725644730318942728101471045037112450682284520951847177283496341601551774254483030077823813188507483073118602703254303097147462068515767717772884466792302813549230305888885204253788392922886375194682180491793001343169832953298914716055094436911057598304954503449174775345984866214515917257380264516918145147739699677733412795896932349404893017733701969358911638491238857741665750286105099248045902976635536517481599121390996091651261500380029994399838070532595869706503571976725974716799639715490513609494565268488194
verified = False
while 1:
	if b == 4:
		verified = True
		break
	d = 2 + (1125899906842622 if a&2 else 0)
	if a&1:
		b //= d
	else:
		b *= d
	b += (b&c)*(1125899906842622)
	a //= 4
if verified:
	t %= (2**300)
	t ^= 1565959740202953194497459354306763253658344353764229118098024096752495734667310309613713367
	print(t)
```

So the program takes in a number from us which then determine what operations happen on the number b. The program looks at the last two bits of our input number a, and determines 4 possible operations to occur. The 4 are:
* Multiply b by 2
* Multiply b by 1125899906842624
* Divide b by 2
* Divide by by 1125899906842624

Using these 4 operations we are trying to get the number b, which starts at 1, to reach 4. The final and biggest obstacle is that after every one of our four operations, the result of b bitwise AND c is multiplied by 1125899906842622 and added back to b. This operation becomes very annoying as whenever b&c isn't equal to 0, b changes by an incredible amount and essentially becomes uncontrollable to be back on track to get to 4 with our limited operations. So, using our 4 operations we want b to reach 4 and avoid b&c equaling a nonzero number whenever possible.

From here if done right, the problem is solvable simply using something like dfs and pruning correctly to avoid times when b&c != 0, repeating moves, etc. However, I believe there is a more elegant solution that requires an important observation that may not be immediately obvious to some. At first the only additional thing I could come up with is that the other number that b can be multiplied/divided by of 1125899906842624 is actually 2^50. So now we have b which starts at 2^0=1, we want to reach 2^2=4, we can multiply and divide by 2^1 or 2^50 however we choose. Breaking it into powers of two is very important in understanding what is really happening in this challenge.

# Solution:

Eventually after being stuck for a while a teammate of mine said: "I think this is sort of similar to maze solving. We want to avoid the 'walls' of 1 bits because theyll screw up our b." This was the key observation I was missing in the challenge and it ties together the significance of the c constant and our powers of 2. If we imagine this problem purely in terms of binary we can see the maze described. Because we move along powers of 2 our number is always a single bit, it is just a matter of where it is shifted. Multiplying and dividing by 2 is the same operation as a bitwise shift to the left and right by 1 while multiplying and dividing by 1125899906842624 is a bitwise shift to the left and right by 50.

Our b value starts at a lowly 1 in binary. We need to eventually shift it to be 100, to be 4, however as said earlier the 'walls' of 1s in the constant c block us. If our singular bit ever lines up with a 1 bit in the c constant, the result of b&c will be nonzero, multiplied by 1125899906842622, and completely mess up our quest to reach 4. So, our goal is to shift our single bit around in a way to reach 4 and along its journey it can never line up with a 1 bit in the constant c.

To visualize this idea I made a simple game in python. I have included the file game.py in this folder if you would like to try for yourself, but for the purpose of the writeup I will just be showing screenshots. In the game our bit is marked by the 'X' character and has 4 possible moves, 'q', 'w', 'e', and 'r'. Our character can move 50 bits left, 1 bit left, 1 bit right, and 50 bits right respectively. The goal is to move our bit from its starting position as the last bit, to reach the third to last bit.

![image](https://github.com/RenchTG/CTF-writeups/assets/91157382/52903601-8053-434c-9534-fcb70039b257)

This is the starting position of our game. As you can see we can't simply go 1 bit to the right twice as the 1 blocks our way. However we can see there is a long sled of 0s that if reached would allow us to move left until we reached the third to last position. Also note the number in binary is reversed as it just seemed more logically to me when playing around with the game, but it is important to understand that realistically we start at the very end of the number.

So as our first move we are forced to move right 50:

![image](https://github.com/RenchTG/CTF-writeups/assets/91157382/c2f32da1-f942-4cc2-afec-86e87b6de4b4)

However we are again stuck between 1's and must move to the right by 50. This will repeat until you find pockets of 0's as shown below:

![image](https://github.com/RenchTG/CTF-writeups/assets/91157382/c6d87524-817d-4144-9b66-6e48efaa8f71)

However, this is where I realized winning this game manually was going to be a challenge. The first few moves are forced, but eventually the amount of paths branch out just like a maze and sometimes there are so many possible paths at once that keeping track of which ones continue and which ones end becomes impossible to manage. So time to write a script to solve it for us. However now this will be very easy to write as we understand exactly what is happening now that we've visualized it from the maze perspective.

For this I used dfs as I am familiar with it and it is very easy to implement.

```python
c = 211403263193325564935177732039311880968900585239198162576891024013795244278301418972476576250867590357558453818398439943850378531849394935408437463406454857158521417008852225672729172355559636113821448436305733721716196982836937454125646725644730318942728101471045037112450682284520951847177283496341601551774254483030077823813188507483073118602703254303097147462068515767717772884466792302813549230305888885204253788392922886375194682180491793001343169832953298914716055094436911057598304954503449174775345984866214515917257380264516918145147739699677733412795896932349404893017733701969358911638491238857741665750286105099248045902976635536517481599121390996091651261500380029994399838070532595869706503571976725974716799639715490513609494565268488194
maze = bin(c)[2:][::-1]+'x'*50

def dfs(pos,moves):
    inp = moves[-1]
    if inp == 'r':
        if (maze[pos+50]=='0'):
            pos+=50
        else:
            return
    elif inp == 'e':
        if (maze[pos+1]=='0'):
            pos+=1
        else:
            return
    elif inp == 'q':
        if (maze[pos-50]=='0'):
            pos-=50
        else:
            return
    elif inp == 'w':
        if (maze[pos-1]=='0'):
            pos-=1
        else:
            return
    
    if pos == 2:
        print(moves)
        return
    
    if inp != 'q':
        dfs(pos,moves+'r')
    if inp != 'w':
        dfs(pos,moves+'e')
    if inp != 'r':
        dfs(pos,moves+'q')
    if inp != 'e':
        dfs(pos,moves+'w')
    
dfs(0,'r')
```

There are 3 main sections of my dfs function. The first section checks the last move inputted and moves our bit accordingly if possible. If the move would result in colliding with a 1, the function immediately returns as this is not a possible move. The next section is our base case, if we have successfully reached our goal and our bit is in the second position, so 2^2 = 4 we print the moves used to reach there and return. The final section calles the function recursively with all 4 possible moves. I added additional if statements as after debugging I realized some branches would be stuck undoing the move just made so going left-right-left-... forever. These checks ensure that every iteration a new move must be made and no infinite loops occur.

Running this script gives me a solution to our maze almost insantly. The correct order of moves is: 

`rrrreeeerrrrrreerrwwwwqqwwrrrrrrrrrrrreeeerreeeeeeeeeerrrreerreerreeqqeerreerrwwrrrrrreeeeeerreeeerrwwrrrreeeeeeeeqqwwqqeeeeeeqqqqqqeeeerrrrrrrrrrreeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww`

However we must remember the script given takes in a number `a` as input and not instructions. This had me worried at first, but looking back at the script, at every iteration only the last two bits of our input number matter. The operation a&1 only checks if the last bit is 0 or 1 and a&2 does the same but for the second to last bit. Then, the 2 possibilites for the 2 if statments give us a total of 4 possible operations every iteration. Finally, after every iteration, the operation `a //= 4` occurs. However, if we remember to frame this problem in terms of binary, just like `b //= 1125899906842624` is equivalent to `b >> 50`, the operation `a //= 4` is equivalent to `a >> 2`. So, every iteration we check the last two bits of a then remove the last two bits of a, and this pattern repeats. This makes it very easy for us to reconstruct our input based off our moves given by our previous script.

To translate our game moves to a binary string I went back to the script to determine which bits have to be set to make which move and I ended up with the following:
* q = a&2 > 0 and a&1 > 0 = 11
* w = a&2 == 0 and a&1 > 0 = 01
* e = a&2 == 0 and a&1 == 0 = 00
* r = a&2 > 0 and a&1 == 0 = 10

I quickly implemented this into a script to generate our correct input a.
```python
ops = 'rrrreeeerrrrrreerrwwwwqqwwrrrrrrrrrrrreeeerreeeeeeeeeerrrreerreerreeqqeerreerrwwrrrrrreeeeeerreeeerrwwrrrreeeeeeeeqqwwqqeeeeeeqqqqqqeeeerrrrrrrrrrreeqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
binary = ''

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
```

This gave me the number:

`266389209626964670411229630383277269677501566076407503706285515444076594421701235243486016983041387987424513152591848742324465668841041551073869994`

Inputting this into the original script provided prints: `50937517511040739473747084954399628437899554758014667643591355768086908816264879291316093` and the program terminates. This means we have provided the correct input. I intially tried submitting this number as the flag, but it turned out to just need the good ol' l2b to finish the job.

![image](https://github.com/RenchTG/CTF-writeups/assets/91157382/4d8702dc-57dd-43d3-bad0-d2574eebad3f)

There's our flag! This was definitely a very fun challenge and although this could probably be solved naively with dfs from the start I think the binary maze perspective makes it a much more interesting solve.
