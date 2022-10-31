import os
os.system("steghide extract -sf stegosaurus.jpg -xf info.txt -p " +  'I love you')
with open("rockyou.txt", "r") as my_file:
	for line in my_file:
		os.system("steghide extract -sf stegosaurus.jpg -xf info.txt -p " + "\"" + line + "\"")

