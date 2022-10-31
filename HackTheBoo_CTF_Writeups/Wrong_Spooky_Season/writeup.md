# Challenge Info:

#### Challenge Name: Wrong Spooky Season

#### Challenge Description: "I told them it was too soon and in the wrong season to deploy such a website, but they assured me that theming it properly would be enough to stop the ghosts from haunting us. I was wrong." Now there is an internal breach in the Spooky Network and you need to find out what happened. Analyze the the network traffic and find how the scary ghosts got in and what they did.

#### Files Provided: capture.pcap

# Solution: 

#### This file gave us a simple pcap file with many tcp and http requests. I first extracted http objects and saw many different images, scripts, html documents, etc. Everything that would make a good and simple website. However, I also saw three data files that looked like commands run on a shell. The commands were whoami, id, and an installation of socat.
#### It seemed to me by looking at the http objects and packets that someone connected to the website, exploited some vulnerability to gain a shell, and then opened port 1337 on the server thus creating a direct connection to the server.
#### *Quick note: The vulnerability exploited on the site seems to be Spring4Shell, which I thought was pretty interesting. The flag also references it!*

#### One thing that is also important to note here. At the beginning, most of the TCP packets are handshakes and such between the user and the website. They also don't contain much important data. All the important data is sent through http packets.
#### However, once the user gets a shell and creates a connection with socat, no more http packets are sent and instead the TCP packets have all the important information and commands being run.

#### Looking through all of the http packets showed nothing interesting, other than the context for what happened and what was exploited. However the TCP packets at the end of the file contain many of the commands that are run on the server. In one of them we see:

![image](https://user-images.githubusercontent.com/91157382/199054256-c4f64024-4947-4060-9405-9f3ca67e4108.png)

#### That looks like base64 to me. Sure enough if we reverse the string and decode it from base64, we get the flag.

## Flag: HTB{j4v4_5pr1ng_just_b3c4m3_j4v4_sp00ky!!}
