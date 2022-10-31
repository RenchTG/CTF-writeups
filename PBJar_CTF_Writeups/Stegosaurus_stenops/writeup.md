# Challenge Info:

#### Challenge Name: Stegosaurus stenops

#### Challenge Author: ZeroDayTea

#### Challenge Description: This stenops swallowed the flag... and some unusually large rock

#### Files Provided: stegosaurus.jpg

# TLDR:

#### - Use some steg cracking tool like steghide or stegcracker to find hidden data in the file.
#### - Figure out that the hint 'rock' is leading you to the wordlist rockyou.txt.
#### - Write a script that brute forces the passphrase using words from rockyou.txt.

# In-Depth Solution: 

#### So when we first open up the image we just see a simple stegosaurus, but there must be more here 👀. The challenge is definitely something steganography related so I quickly googled common steganography tools. I ended up finding this tool called steghide where you can simply run a command in the terminal and it should extract the hidden data ... right?

`steghide extract -sf stegosaurus.jpg`

#### First I ran this command, however afterwords it asks me for a passphrase. I was a bit stumped at first but when I looked back at the challenge we are given a hint. From the description we can reasonably infer the author is pointing us towards 'rock'. After doing some research on common passphrases and 'rock' I came across this very neat file called rockyou.txt. Turns out this file is an extremely large assortment of the most common passwords that have been used over time. It is extremely big though and the passphrase can only be one of them. Let's make python do the heavy lifting. Also I downloaded rockyou.txt at this link: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

```python
with open("rockyou.txt", "r") as my_file:
	for line in my_file:
```

#### I started off with these lines of code and now I was able to read in the rockyou.txt file I downloaded and loop through each line of it. Now I just had to actually run the steghide command using the lines we take from the txt file.

```python
os.system("steghide extract -sf stegosaurus.jpg -xf info.txt -p " + "\"" + line + "\"")
```

#### After searching I found this neat module by the name of os, that I'm pretty sure is built into python so no installing is necessary, which allows you to run terminal commands from python. Eventually I was able to craft together that line shown above which will try to extract info from the image, put anything extracted into info.txt, and use the passphrase taken as we loop through rockyou.txt. The weird "\\"" on both sides of the variable `line` are just to make sure that if there are any spaces in one of the lines, such as 'I love you', the command will read it in as one string rather than spitting out something like: 

`Unknown argument "you"`

#### After that just let the terminal get spammed a bunch of times with something along the lines of:

`Unable to extract data with that passphrase`

#### Finally the nice thing of adding `-xf info.txt` into the command alows you to walk away from your computer in case the data extracted was just raw data as you could come back and it would be neatly saved in info.txt. ZeroDayTea set it up however to create a flag.txt file for you anyways so it didn't matter that much, but I think it still makes life much more convenient. 

#### Anyways enough blabbering here's the flag that was extracted!

## Flag: flag{ungulatus_better_than_stenops}

# Full Script: 

```python
import os

with open("rockyou.txt", "r") as my_file:
	for line in my_file:
		os.system("steghide extract -sf stegosaurus.jpg -xf info.txt -p " + "\"" + line + "\"")
```
