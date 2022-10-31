# Challenge Info:

#### Challenge Name: Spookifier

#### Challenge Description: There's a new trend of an application that generates a spooky name for you. Users of that application later discovered that their real names were also magically changed, causing havoc in their life. Could you help bring down this application?

# Solution: 

#### The website given to us is pretty simple. A textbox and whenever text is entered, it gets changed into four different fonts. Looking at the source code provided we can see in util.py that all of the four fonts are created. What is interesting is that only the fourth font supports any meaningful characters that would allow us to perform some type of injection, so most likely we will be focusing on the fourth box.

#### Next, I wanted to know how our input was being processed, to help figure out how we can exploit it. Eventually I found in routes.py this:

![image](https://user-images.githubusercontent.com/91157382/199048755-21029b82-22a0-4822-bbcb-70e3d0488b0a.png)

#### `return render_template('index.html',output=converted)` This line is what caught my eye. Not knowing much I googled render_template vulnerabilities. I quickly found many sources that pointed to SSTI (server-side template injection).

![image](https://user-images.githubusercontent.com/91157382/199049879-31c9bf41-c2ac-4288-94c1-807439045afa.png)

#### For example the image above shows different injections you can test to figure out what is running on the server. The simplest one `${7*7}` did in fact work and the fourth textbox showed 49. So, we've identified the vulnerability.
#### Additionally, the source code already tells us which version of flask we are using, so we don't have to do all that testing! `from flask_mako import render_template` More googling eventually led me to this link: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md which has an incredible list of different SSTI injections. Going down to the mako section, we have a bunch of different ways to access the os module with our injection.

![image](https://user-images.githubusercontent.com/91157382/199051101-16160db1-b9db-4204-b22b-cb5d636eb339.png)

#### The very first injection provided seemed to be working and eventually I was able to get this input to work:

```${self.module.cache.util.os.popen("cat /flag.txt").read()}```

#### Then all I had to do was look at the fourth box and there was the flag!

## Flag: HTB{t3mpl4t3_1nj3ct10n_1s_$p00ky!!}
