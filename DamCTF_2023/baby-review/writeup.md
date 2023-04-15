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

