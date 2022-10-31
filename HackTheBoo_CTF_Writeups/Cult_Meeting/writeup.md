# Challenge Info:

#### Challenge Name: Cult_Meeting

#### Challenge Description: After months of research, you're ready to attempt to infiltrate the meeting of a shadowy cult. Unfortunately, it looks like they've changed their password!

#### Files Provided: meeting

# Solution: 

#### In this challenge we are given a 64-bit binary which if ran, asks us to provide a password.

#### Opening this binary in Ghidra shows us the following code in main:

![image](https://user-images.githubusercontent.com/91157382/199040147-dbfd1b06-d347-4b92-81a2-17ee899dae1d.png)

#### We see that all the program is doing is simply prompting us for the password and comparing it with a string. If correct we get a shell! What's easy about this challenge is that the password they compare against is in plain-sight so we are able to take the password: `sup3r_s3cr3t_p455w0rd_f0r_u!`

#### Then we just spin up an instance and input the password. Once we have shell we can simply run `cat flag.txt` and get our flag.

## Flag: HTB{1nf1ltr4t1ng_4_cul7_0f_str1ng5}
