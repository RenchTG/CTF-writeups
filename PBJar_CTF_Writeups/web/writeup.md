# Challenge Info:

#### Challenge Name: web

#### Challenge Author: eyangch

#### Challenge Description: I downloaded this program back when the version number was still v1. It's been a long time... I heard the most recent update has the flag in it. Download: http://147.182.172.217:42100/v1

#### Files Provided: none

# TLDR:

#### - Find the outer limits of the possible versions by just adding 0's.
#### - Use a binary search method to keep finding numbers between your limits until you get the newest version.
#### - Find the flag in the downloaded flag file.

# In-Depth Solution: 

#### So to start off we go to the website on the link provided and a weird file is downloaded. It has a bunch of non-readable text on it, but some is readable. On it though we can find a link that takes us to download version 2. Once we click the link to version 2 we download another file and in there we get a link to version 3. This will repeat over and over again. Our goal as the description states is to find the newest one. I start off by playing around with the url and I realize that I can change the url to get whatever version number I put in. I then proceed to find the limits of the version by just adding zeroes. Eventually I get the url:

#### `http://147.182.172.217:42100/v100000000`

#### to download a file for me. However, the next url with one more zero: `http://147.182.172.217:42100/v1000000000` would give me the message:

#### `version not found`

#### After that I decided a write a script for me to perform a sort of binary search to find the number that is in between the two limits that I have set. I thought about automating this process so that I would send a web request with my script and based on the response I change my limits. However of course I was too lazy so I kept inputting the version my program spit out by hand into the url and would change the variables myself accordingly. Pretty much the general idea is that if we do get a version back and it downloads a file, that is the new `min_limit` and if the website responds with 'version not found' we update the `max_limit`. 

```python
min_limit = 100000000
max_limit = 1000000000
halfway = int(((max_limit - min_limit) / 2) + min_limit)
print(halfway)
```

####  This is the short script that I use to get my middle number. After that I just go the website and replace the version in the url with the number my program prints, check what response I get from the website and update min and max limit accordingly, and just rinse and repeat. Eventually the version number `133791021` downloaded a file called `flag`. Then just run strings or cat on it like this:

#### `strings flag` or `cat flag`

#### And boom, our flag is in there. There's definitely a much more optimized way to do this especially if you can automate updating the max and min limits, but this method works and got me the flag which is what matters. Anyways here's the flag, enjoy!

## Flag: flag{h0w_l0ng_wher3_y0u_g0ne_f0r_3910512832}

# Full Script:

```python
min_limit = 133791015
max_limit = 133791027

halfway = int(((max_limit - min_limit) / 2) + min_limit)

print("Version can be: " + str(min_limit))
print("Version can't be: " + str(max_limit))
print("In the middle: " + str(halfway))
```
