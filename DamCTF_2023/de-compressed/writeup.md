# Challenge Info:

* **Challenge Name:** De-compressed

* **Challenge Category:** Misc

* **Challenge Author:** Perchik

* **Challenge Description:** As an elite cyber security expert, you've been tasked with uncovering the secrets hidden within a message intercepted from a notorious spy. We suspect there may be more to this message than meets the eye. Can you use your skills in steganography to uncover whatever else might be hiding? The fate of national security is in your hands.

* **Files Provided:** message.zip

# Solution:

To start off I unzipped the provided file and received README.txt which reads:
```
Dear Sylvia,

I wanted to let you know that I have decided to resign from the team, effective immediately. I have been offered a better opportunity elsewhere and I believe it is in my best interest to pursue it.

Please do not be concerned about the success of the mission. I have confidence in the remaining members of the team, and I am sure they will be able to complete it without any problems.

I apologize for any inconvenience my departure may cause, and I hope you will understand my decision.

Sincerely,

Twilight
```
This isn't really helpful to us and opening this file in a hex editor doesn't show anything out of the ordinary. I go back to the zip file and open it with a hex editor to see that there are in fact two files inside, README.txt and secret.txt. Running binwalk also gave me a similar result:

![image](https://user-images.githubusercontent.com/91157382/231617684-071bc372-a338-4890-adae-5560ea4e0fa9.png)

However normal extraction methods were not retrieving secret.txt. I figured there were probably some zip repair tools that could help me fix the zip rather than editing it manually. Eventually, I stumbled upon the built-in feature to the zip command using the flag -FF. So I ran:
```
zip -FF message.zip --out fixed.zip
```
Unzipping this new zip file did give secret.txt. When I printed its contents I could see some readable words, but in between them were strange gaps. At first I thought this could be whitespace stegonography, but once I opened it in a text editor I could see that there were unicode characters scattered all throughout the file.

![image](https://user-images.githubusercontent.com/91157382/231618624-55e45880-d05d-47a8-a4a4-d03325594d49.png)

However, some of the characters were still displayed as unknown so I just decided to open the file in a hex editor and I realized the following series of bytes repeated frequently throughout the file and weren't part of the readable text.
* e2808c
* e2808d
* e280ac
* efbbbf

After doing a bit of research, I found that these were all different unicode characters. I then used this list: https://www.utf8-chartable.de/unicode-utf8-table.pl to identify what each unicode character was, and so I updated my list.
* e2808c = Zero Width Non Joiner [U+200C]
* e2808d = Zero Width Joiner [U+200D]
* e280ac = Pop Directional Formatting [U+202C]
* efbbbf = Byte Order Mark [U+FEFF]

These unicode characters are commonly used to encode messages using Zero-Width Stegonography. Eventually I stumbled upon a similar writeup here: https://ctftime.org/writeup/11321 which linked to an amazing tool found here: https://330k.github.io/misc_tools/unicode_steganography.html. The list of possible zero width characters had all of the four I found in secret.txt, but the website was a bit finnicky and I opted to just use the JS library they link at the top.

Eventually, I created a simple JS script to decode the flag, copying the text directly from secret.txt and only removing the newlines:
```js
const stego = require("./unicode_steganography.js").unicodeSteganographer;
stego.setUseChars('\u200c\u200d\u202c\ufeff');
var text = "‌‌‌‌‍‌‍‌I ‌‌‌‌‍‬‬‍read‌‌‌‌‍﻿‌﻿ ‌‌‌‌‍﻿‌‬between ‌‌‌‌‍‬‍‍‌‌‌‌‍‬‍﻿the‌‌‌‌‍‬‌‍‌‌‌‌‍﻿‌‬ lines, my ‌‌‌‌‍‬‍‌vision'‌‌‌‌‌‬‌‌s ‌‌‌‌‍﻿‍‌‌‌‌‌‍‬‬‌‌‌‌‌‍‬‍‍clear‌‌‌‌‌‬‌‌ and‌‌‌‌‍‍‌‬ keen‌‌‌‌‍‌‍‍ I‌‌‌‌‍‌‌‍ ‌‌‌‌‍‌‍‌see ‌‌‌‌‍‌﻿‍the hidden‌‌‌‌‍‌‍‍ ‌‌‌‌‌‬﻿‌meanings, ‌‌‌‌‌‬‌‌the truths ‌‌‌‌‍‌‬‍that‌‌‌‌‌‬‌‌‌‌‌‌‍‬‌‍ ‌‌‌‌‍‬﻿‍are unseen ‌‌‌‌‌‬‌‌I don'‌‌‌‌‍﻿‌﻿t ‌‌‌‌‍﻿‍‌‌‌‌‌‍‬‬‍‌‌‌‌‍‬﻿‌just‌‌‌‌‍‬﻿‌‌‌‌‌‌‬‌‌‌‌‌‌‍‬﻿﻿‌‌‌‌‍‬﻿‬‌‌‌‌‌‬‌‌ take ‌‌‌‌‍﻿‍‌things ‌‌‌‌‍‬‬‌at ‌‌‌‌‍‬‍‍face value,‌‌‌‌‌‬‌‌‌‌‌‌‍﻿‍‌ ‌‌‌‌‍‬‍‍that‌‌‌‌‍‬‌‍‌‌‌‌‍‬﻿‍‌‌‌‌‌‬﻿‬'s not‌‌‌‌‌‌‬‬ my‌‌‌‌‍‬‍‌‌‌‌‌‍‬‌‍ ‌‌‌‌‍‬﻿‍style I ‌‌‌‌‍﻿‬﻿‌‌‌‌‍﻿‍‌dig‌‌‌‌‌﻿‌‍‌‌‌‌‍‬﻿‍ ‌‌‌‌‌﻿‌﻿deep and I uncover‌‌‌‌‍‍﻿﻿‌‌‌‌‍﻿‍‌, the ‌‌‌‌‌﻿‌‌hidden‌‌‌‌‍‍﻿﻿ ‌‌‌‌‍‬‬﻿‌‌‌‌‍‬‬‍treasures‌‌‌‌‍‬‌﻿ ‌‌‌‌‍‬‬﻿that‌‌‌‌‍‍﻿﻿‌‌‌‌‍‬‌‬‌‌‌‌‌﻿‍‌‌‌‌‌‍‬‌﻿ ‌‌‌‌‍‬‬﻿‌‌‌‌‍‍﻿﻿are‌‌‌‌‌﻿‍‌ compiled‌‌‌‌‍‬﻿‬ ‌‌‌‌‍‬‍‌‌‌‌‌‍‍﻿﻿‌‌‌‌‍﻿‌‬‌‌‌‌‌﻿‌﻿‌‌‌‌‍‬﻿‌‌‌‌‌‌﻿‍‌‌‌‌‌‍﻿‬‌‌‌‌‌‍﻿﻿‍";
console.log(stego.decodeText(text));
```
Running this script gave me the flag!
![image](https://user-images.githubusercontent.com/91157382/231627614-cdcec425-5e9d-45a6-84ce-54359cc84ad9.png)

