# Challenge Info:

#### Challenge Name: Evaluation_Deck

#### Challenge Description: A powerful demon has sent one of his ghost generals into our world to ruin the fun of Halloween. The ghost can only be defeated by luck. Are you lucky enough to draw the right cards to defeat him and save this Halloween?

# Solution:

#### Simply playing around with the website did not render anything useful. Killing the ghost multiple times changed nothing, so it seemed to me that the description of the challenge wouldn't be very helpful.

#### Looking into the code, however, was something interesting. In routes.py we could see that a flask blueprint was being created, one web and the other api.

![image](https://user-images.githubusercontent.com/91157382/199043471-cdecb36c-fe26-4ff7-a636-6541d914b844.png)

#### Here we can also see something very dangerous. The script compiles and then executes something using the three values of current_health, operator, and attack_power. So this looks like a code injection challenge. However, both current_health and attack_power get changed to ints, so it will be difficult to work with them. So, let's use the operator!

#### In my solution I sent all my requests with curl, but a lot of other tools would've worked. Firstly, the code in routes.py tells us we must be sending a POST request, but also it must be formatted in a proper JSON format. In curl this looked like:

`curl -X POST http://url/api/get_health -H 'Content-Type: application/json' -d "{"current_health":"5", "attack_power":"5", "operator":"+"}"`
#### *Note: url would be replaced with whatever url my spawned instance gives me*

#### Making this request does in fact return 5 + 5 and sets the ghost's health to 10. Now, time to craft our injection! In the end, I saw that this was all compiling in python so decided to use the os library, and then with it running a command to print the flag, which we know is at /flag.txt due to the Docerfile provided.
#### Eventually, I figured out I could simply put a comment at the end of my operator value, which would essentially ignore anything after my injection. With enough finnicking around I was able to create this:

`curl -s -X POST http://url/api/get_health -H 'Content-Type: application/json' -d "{\"current_health\":\"5\", \"attack_power\":\"5\", \"operator\":\"; import os; result=os.popen('cat /flag.txt').read(); # \"}"`

#### Additionally, because the whole point of the request is to create and set a variable called result, we can simply overwrite it with whatever the output of our os command is, in this case the flag. Also this command looks really ugly with escaping all the double quotes, this is why next time I would use a better tool for sending requests like Postman, rather than with curl.

#### Sending that request gives us the flag!

## Flag: HTB{c0d3_1nj3ct10ns_4r3_Gr3at!!}
