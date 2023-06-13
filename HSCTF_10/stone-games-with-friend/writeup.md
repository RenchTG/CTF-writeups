# Challenge Info:

* **Challenge Name:** stone-games-with-friend

* **Challenge Category:** algo

* **Challenge Author:** Jaysu

* **Challenge Description:** Flag is the output for `input.txt`, wrapped in the flag format.

* **Files Provided:** input.txt, stone-games.pdf

# Research: 

To begin we of course read the pdf provided. The general premise of the problem is that two players play a series of 30 games. In each game there are N piles of stones. Every turn, a player may remove anywhere from 1 to floor(sqrt(a)) stones, where a is the number of stones currently in that pile. This will continue until all piles reach 0 stones and the first player that has no stones to take anymore loses. Both players play optimally and player 0 goes first. For each of the 30 games we are given the amount of piles N and the amount of stones in each of the N piles. The flag will be an integer made up of the bits based on which player wins each game.

My competitive programming skills are not that strong, so I relied heavily on research to get me through this challenge. It is quickly obvious that this challenge is a variation of the popular game Nim. The only difference is that instead of being able to take any amount of stones > 1 as is in traditional nim, we are limited by the floor(sqrt(a)) rule described earlier. There are plently of resources and similar problems online, but throughout my time I really only ended up using two very valuable resources that explained everything I needed to know for this.
* https://codeforces.com/blog/entry/66040
* https://math.stackexchange.com/questions/704870/winning-a-restricted-game-of-nim

If you are curious you can read each individually, but I will reference the most important points of each. I knew I was on the right track with the CF blog as they even said, "A common tweak is putting a limitation on the number of stones you can get from a pile." This is exactly what our challenge is, so I knew this was on the right track. All of the Nim-related games described in the blog are called impartial games, this means that the games are decided purely by how the game is setup, in our case the number of stones in each pile, and which player goes first. There is a lot of studied game theory on impartial games, but we really only need to reference the basics.

Another important quote from the blog was, "these games are equivalent to playing Nim, but instead of getting the Nim-sum by taking the XOR of the piles, we take the XOR of their Grundy numbers." So really the tl;dr solution for these problems is to split the game into individual piles and calculate the Grundy numbers for each one and XOR all of them, if the result is nonzero one player will win, if the result is zero the other player wins. Throughout my solution I won't specifically reference when player 0 or 1 wins as it doesn't really matter until we construct our flag at the end and we can always simply flip our bits if our flag is incorrect.

So, we know how to get the solution, but what are Grundy numbers? These were explained in the CF blog, but I was really just looking for an easy method to write a script to calculate them and the CF blog didn't do that as well. Enter the math stackexchange question. There the question describes a Nim variation where you can take only 1 or 2 objects from the pile every turn. After reading the top answer this is how I understood calculating Grundy numbers:

To calculate the Grundy number for a pile of size N, first find all possible positions that can be reached after one player's turn. In our case, the possible positions range from N-1 to N-floor(sqrt(N)). Now that we have our possible positions, calculate the Grundy numbers for all of those positions and then take the minimum excludant (mex) of those. The result of that will be our Grundy number. Quick note: if you are unfamiliar with the mex function it is essentially the first nonnegative integer in a set, basically start at 0 and keep incrementing until you can't find that number in your set and that will be your mex.

So we now know how to calculate Grundy numbers, but one issue that becomes quickly apparent is the recursive nature of this "Grundy function". Given a very large N value we will essentially need to calculate the Grundy value for every number 0 to N. This is because the Grundy for N is reliant on N-1, N-2, ... N-floor(sqrt(N)), and then N-1 is reliant on N-2, N-3, ... and you get the idea. But this is no problem right, python can do recursion. Time to write our solution!

# Solution:

I quickly wrote a python script that would recursively find Grundy numbers and store them in a large array. By the way one thing I may have left out is the Grundy of 0 is simply 0 which acts as our base case for recursion. This worked great and I was able to generate the Grundy numbers up to 1,000, 10,000, 100,000 and oh this is taking a while. It very quickly became apparent that this program was going to be very very slow. But not to fret, we are given input.txt so it is ok if our solution is very long. But checking the pdf again, the piles can go up to sizes of 1e9. If my script took an hour to calculate the Grundy for 1 million, 1 billion was never going to happen.

I referenced the CF blog again and they even say: "The complexity in these kinds of programming problems in contests usually then comes down to finding some efficient formula for the Grundy numbers." And this was the exact problem I had run into. After a lot of head banging I eventually made a key observation when I looked at the first 100 Grundy numbers that my script generated:

`[0, 1, 0, 1, 2, 0, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 5, 2, 4, 0, 3, 1, 5, 2, 4, 0, 3, 6, 1, 5, 2, 4, 0, 3, 6, 1, 5, 2, 4, 0, 7, 3, 6, 1, 5, 2, 4, 0, 7, 3, 6, 1, 5, 2, 4, 8, 0, 7, 3, 6, 1, 5, 2, 4, 8, 0, 7, 3, 6, 1, 5, 2, 9, 4, 8, 0, 7, 3, 6, 1, 5, 2, 9, 4, 8, 0, 7, 3, 6, 1, 5]`

If you look closely at these a pattern begins to emerge. The pattern does have some complexity to it, but it was definitely something I could script. I'm not sure if this is the best way of describing it, but this is how I ended up thinking about the pattern myself and how I wrote my script later. Rule #1 is that as we are generating our list of Grundy numbers we want to keep track of our "subpattern" I'll call it. When we first start our subpattern is simply [0]. So if we generated just using rule 1 we'd get [0,0,0,0,0,...]. Enter Rule #2: at any index that is a perfect square, add the squareroot of that index to our subpattern from rule 1 and continue.

To explain it better I'll walk through the first couple of grundy numbers.
* Index: 0, Subpattern: [0], Add 0 to array.
* Index: 1, Perfect Square!, Subpattern: [0,1], Add 1 to array.
* Index: 2, Subpattern: [0,1], Add 0 to array.
* Index: 3, Subpattern: [0,1], Add 1 to array.
* Index: 4, Perfect Square!, Subpattern: [0,1,2], Add 2 to array.
* ...
* Index: 9, Perfect Square!, Subpattern: [0,3,1,2], Add 3 to array.
* ...
* Index: 16, Perfect Square!, Subpattern: [0,3,1,2,4], Add 4 to array.

So we are essentially continuously cycling through our subpattern and appending numbers to our main array, until we reach an index that is a perfect square. If a perfect square index is hit, the subpattern has a new number inserted at whichever index was last appended to the main array. This continues forever and works in linear time and is thus able to calculate all Grundy numbers up to 1e9 very quickly. This is how I implemented this idea into my Grundy generation script.

```python
grundys = [0,1]
subpattern = [0,1]
index = 0
for i in range (2,1000000000):
    sq_root = perfect(i)
    if sq_root == -1:
        grundys.append(subpattern[index])
    else:
        grundys.append(sq_root)
        if index == 0:
            subpattern.insert(len(subpattern),sq_root)
            index -= 1
        else:
            subpattern.insert(index,sq_root)
    index += 1
    index %= len(subpattern)
```

It took some trial and error, but eventually this script was generating an array of Grundy numbers identical to my recursive solution, but significantly faster. I made some minor tweaks to this base script to only print out Grundy numbers I needed, those being all of the pile sizes in input.txt, as I didn't want to print out 1 billion Grundy numbers. You can find the full script grundy.py in the same folder as this writeup. Once I had all the Grundy numbers I needed, it was just a matter of XOR'ing them and checking if the result was zero or non-zero.

```python
#grundy = [Very large array generated by grundy.py, not shown here]
out = ""
f = open('input.txt','r')
g = int(f.readline().strip())
for i in range (g):
    game = f.readline().strip().split()
    n = game[0]
    game.pop(0)
    game = list(map(int,game))
    
    xor = 0
    for j in game:
        num = -1
        for h in grundy:
            if h[0] == j:
                num = h[1]
                break
        if num != -1:
            xor ^= num
        else:
            print("AHHH")
    if (xor != 0):
        out = '0' + out
    else:
        out = '1' + out
print(int(out,2))
```

This took more trial and error and rereading the pdf to know the exact input and output specifications, but eventually I had my flag!

`flag{67643916}`

This was a very fun challenge and well-designed as CTF players like me who aren't as familiar with algo are able to have plenty of resources available, yet still have some challenge ahead of them. Thanks Jaysu!






















