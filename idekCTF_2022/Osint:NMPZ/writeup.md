# Challenge Info:

* **Challenge Name:** NMPZ

* **Challenge Author:** jazzzooo

* **Challenge Description:** Are you as good as Rainbolt at GeoGuessr? Prove your skills by geo-guessing these 17 countries.

# Intro: 

To begin I'd like to say this was a very creative and enjoyable challenge so thank you to the author, jazzzooo. I know a lot of people had fun with it, but also there was a lot of frustration which is why I wanted to make this writeup. Additionally, jazzzooo was kind enough to let me include some of his info here. After the CTF ended he went through every image explaining his solution and answering questions. I'd like to include his notes alongside my own solutions to provide additional tricks that I thought were very clever. Jazzzooo's info will be labeled as (Chal Author Notes) as I do not want to take credit for his work. Anyways, I hope you enjoy the writeup!

# Resources:

Before getting into the images, I'd like to talk about some important resources that are key to solving this challenge and ones I will be referencing throughout the writeup. I didn't know about any of the following resources (except Google Lens) before I started this challenge and I think one thing that helped me find these was having a GeoGuessr perspective going into the challenge rather than a CTF Osint perspective. There are many resources specifically made for GeoGuessr because of the popularity of the game and the insane lengths people go to study for it, so I think utilizing said resources is a must. Anyways here's the list:
* https://geohints.com/ : This website has a lot of images for different categories of objects you can find in images. It is also very easy to use and well organized, so I highly recommend.
* https://somerandomstuff1.wordpress.com/2019/02/08/geoguessr-the-top-tips-tricks-and-techniques/ : This site is not as nicely organized, but contains an extremely large amount of info. Ctrl+F definitely helps :wink:
* http://www.worldlicenseplates.com/ : Very detailed site, but only for license plates. However, I believe these are some of the most common and helpful clues when going through these types of images.
* https://www.google.com/ : Finally without Google Lens/Search By Image this challenge would be near impossible. There are also many other reverse image searchers online which work well, but I prefer Google Lens because of how reliable and accessible it is.
* https://geotips.net/ : Another resource made for GeoGuessr that someone linked in discord after the CTF. Goes in-depth on every country individually and just very helpful in general.

Finally, if you don't know the rules for creating the flag they are the following:
```Figure out in which country each image was taken.
The first letter of every country's name will create the flag.
Countries with over 10 million inhabitants will have a capital letter.
Countries with less than one million inhabitants become an underscore.
```

Now let's GeoGuessr some images!

# Solution:

### Image 1:

![1](https://user-images.githubusercontent.com/91157382/212567949-e80f3b0e-138d-4131-9ab7-860d6fc2d911.png)

* I don't think there is much to explain here as this is the easiest image. In the center of the image is one of the world's most recognizable statues, Christ the Redeemer. I think it is also considered one of the Seven Wonders of the Modern World. Anyways this is a definitive icon of Rio de Janeiro and Brazil.
* Chal Author Notes: Self-explanatory
* Brazil = B

### Image 2:

![2](https://user-images.githubusercontent.com/91157382/212568115-e4750499-089a-4c50-9b06-efbbef4e076a.png)

* This is another very definitive image. In the center of the image is a beautiful cathedral. The distinct shapes on the cathedral are actually called Onion Domes. This is very typical of Russian Orthodox churches and Russian architecture in general. The Cyrillic on the sign to the left also confirms Russia. If you're still doubtful reverse image search will show you this is Saint Basil's Cathedral and on the right the Spasskaya Tower.
* Chal Author Notes: Self-explanatory
* Russia = R

### Image 3:

![3](https://user-images.githubusercontent.com/91157382/212568261-e44d6b90-369c-4cf3-9f32-9eea923f0476.png)

* At first this image is not as obvious as the first two however we see a brown sign with the word Kalamaja which when googled is a neighbourhood in Estonia. If you're still not convinced, reverse image searching the glass buildings on the right tells us it is the Office building of Tallink in Estonia.
* Chal Author Notes: You can see the famous soviet Linnahall in the background too, but Kalamaja ez.
* Estonia = e

### Image 4:

![4](https://user-images.githubusercontent.com/91157382/212568381-056ec9f3-e8d6-492c-8cb9-0d87148f743b.png)

* This image can seem very intimidating at first, however we are given more info than you may think. White sidelines helps narrow it down slightly but isn't enough. The skinny white bollard with a thin red strip in the middle narrows down our search even more. You can find a section for Bollards on geohints. Combine all of this with the red colored soil and landscape this is enough to say Australia. However, if you still aren't convinced, reverse image searching the tall plant in the middle of the image tells us it is a Eucalyptus ceracea which is I quote: "endemic to a small area in the north of Western Australia".
* Chal Author Notes: Bollard
* Australia = A

### Image 5:

![5](https://user-images.githubusercontent.com/91157382/212568599-a7caaa85-53ae-4282-8a6b-979dc9ea8004.png)

* This image is pretty deceiving. There seems to be an extremely large amount of clues and info, but this only fuels the deception. First of all we know we are in some Muslim or Arabic country. There is writing like Al-Siraad Plaza, Al-Furqan, Peri Peri Pizza, and Third Street but the names are actually generic enough to not be helpful (Correction: some people on discord were saying googling Peri Peri Pizza and Third Street was enough to find it). One thing that helps narrow it down quickly is driving on the left side. If you didn't notice this at first please look again. Cars are parked on the left side and driving left. Geohints gives us a nice map of countries that drive on the left. This takes away essentially the entire Middle East, but it could still be South Asian countries like Pakistan or East African countries. For me the final nail in the coffin is license plates. The yellow license plates in the back are very obvious, but one thing you may not have noticed is that license plates are actually white in the front. There is one car visible facing the camera in the middle of the screen and zooming in on the license plate shows all white and no yellow. Thus combining geohints's map of left driving side and world license plates the only country possible is Kenya. Kenya has white in the front yellow in the back, drives on the left side, and has a non negligible Muslim population. Again I think many here would be deceived and thought South Asian countries like Pakistan and Sri Lanka, but you can find such Islamic neighborhoods everywhere. Here the fine details are key.
* Chal Author Notes: Anyone who struggled with this please google "geoguessr snorkel". The Kenyan car is unique, also driving direction. I wanted snorkel in the image, but street name would ruin it, so i took the most generic street.
* Kenya = K

### Image 6:

![6](https://user-images.githubusercontent.com/91157382/212568872-47fd9b4f-706e-4220-a4a1-cbbf92f491e5.png)

* This is a pretty barren looking image, but quite easy. White lines in the middle plus yellow bollards with some white on the top can immediately lead you to Iceland. Combine this with the landscape and mountains in the background to confirm this. If you're still not convinced just reverse image search the whole thing and you'll get a very resounding Iceland.
* Chal Author Notes: Bollards are unique, and landscape yes.
* Iceland = _

### Image 7:

![7](https://user-images.githubusercontent.com/91157382/212569000-5538c099-b3a5-4e05-bf8c-0a59c2552135.png)

* This image shows a very small road, so we aren't really able to use bollards, lines, or driving directions. Instead the two biggest clues is architecture and the license plate visible with very few characters. By architecture, I mostly am referring to the two white yurts visible in the image. Reverse image searching these very quickly gives us Mongolia and geohints confirms this in their Architecture section. If you're still curious this is in Ulaanbaatar, the capital city of Mongolia. If you want to explore for yourself it is slightly North of the Khoroo 17 neighborhood.
* Chal Author Notes: The huts. This is Ulaanbaatar actually. Mongolia has a unique car, which is not visible on purpose.
* Mongolia = m

### Image 8:

![8](https://user-images.githubusercontent.com/91157382/212569196-6f6620ae-bbb0-4577-86a4-97a1df6f07ae.png)

* This is another extremely deceiving image. At first glance I was convinced this was Europe. The white houses with red roofs are just so characteristic. The only reliable method I ended up getting for this question was reverse image search. However, I didn't search the whole image. I cropped it as seen below and Google quickly gave me Swaziland. However, the country changed its name to Eswatini in 2018, so that is what we will be using.
![image](https://user-images.githubusercontent.com/91157382/212569271-e14518af-27a8-428c-a610-f27b5a343833.png)
* Chal Author Notes: Eswatini is extremely hard to get here. I have no idea how you'd get it tbh. I'd have loved break_my, but no country in geo starts with Y. E was the other best option.
* Eswatini = e

### Image 9:

![9](https://user-images.githubusercontent.com/91157382/212569398-10a269d6-6543-4198-b8cb-0be7f7fbdce3.png)

* This image actually isn't too bad. We can see the city is extremely distinct with skyscrapers and an elevated landscape in the background. However what caught my eye was this building shown below. It looked super distinct, so throw it into Google Lens and it will quickly spit out the Opéra de Stephen Monte-Carlo. This tells us it is in the waters of Monaco overlooking Monte-Carlo.
![image](https://user-images.githubusercontent.com/91157382/212569424-433cdd69-3aac-4134-871e-a80a13719b94.png)
* Chal Author Notes: Monaco is unique. Funny enough the Monaco is official google coverage, on a boat...
* Monaco = _

### Image 10:

![10](https://user-images.githubusercontent.com/91157382/212569494-4442bcfa-6b38-435a-851c-b7b815b34aea.png)

* This image can be done very quickly. Looking at the house to the left with green window covers we see two Swiss flags. If you're still not convinced just reverse image search and get Switzerland.
* Chal Author Notes: Theres a swiss flag aaaaaaaaaa. Also, buildings and landscape resemble Switzerland or Austria.
* Switzerland = s

### Image 11:

![11](https://user-images.githubusercontent.com/91157382/212569542-a737b9e4-c4e4-4264-821b-a57d889bda05.png)

* This image shows us a lot of road which is always nice. White sidelines and middle lines narrows it down quickly with geohints. Finally, the white and red bollards for me narrowed it down to either Ukraine or Poland. I was a little back and forth on this one for a while, but combined with Google Lens and me being a LudBud... "those trees look Polish" I was able to confirm Poland.
* Chal Author Notes: Bollards once again!
* Poland = P

### Image 12:

![12](https://user-images.githubusercontent.com/91157382/212569623-36130ad1-909c-4921-a4e8-ee39a3b2a36b.png)

* This image has a lot of visible writing. The red text on yellow signs shows us this must be German speaking. This could really only be Germany, Austria, or parts of Switzerland I believe. However, there is also a small red sign on the right side with white text as seen below. It is a little hard to read but it says: Nikolaus-Dumba-Straße, which googling that quickly gives us Austria.
![image](https://user-images.githubusercontent.com/91157382/212569657-bbc1b322-9bea-4e71-a3f1-7f44de35090d.png)
* Chal Author Notes: Street name. Germany doesn't do much google maps. If it was Germany it would mostly be blurred.
* Austria = a

### Image 13:

![13](https://user-images.githubusercontent.com/91157382/212569763-12955015-ff39-4913-9eb9-a8c3d111d901.png)

* This image can quickly be narrowed down by white sidelines and yellow middle lines. The landscape also reminded me a lot of North America. Reverse image searching this will give many results for Canada which is the answer. I could see this being confused with the Northern United States as well though.
* Chal Author Notes: Calgary, Canada. US has two yellow lines in the middle, Canada one. *Most of the time*
* Canada = C

### Image 14:

![14](https://user-images.githubusercontent.com/91157382/212569887-b0a392c0-c015-41ff-9086-0834cbebfe0f.png)

* From first glance this reminded me of South America or something like Indonesia. But we can actually see the truck is driving on the right side, so this must be South America. Additionally, the road name has an accented i that is seen in Spanish or Portuguese which further confirms South America. The black on yellow chevrons can help narrow it down even further with geohints. The final clue for me was the orange/red license plate that is mentioned in the random GeoGuessr tips and tricks article which tells us it must be Ecuador.
* Chal Author Notes: License plate, driving direction, nature. The red licence plate is a thing in Ecuador for utility vehicles. Chevron maps help as well.
* Ecuador = E

### Image 15:

![15](https://user-images.githubusercontent.com/91157382/212570061-332adf60-8978-49dc-80a9-a4c79d2fcd0d.png)

* So this is initially narrowed down greatly due to the Cyrillic writing on the KMA trash can. Then, the random GeoGuessr tips and tricks article says these trash cans are very typical for Bulgaria. Then, reverse image searching the building on the right gives a lot of Bulgarian results which confirms our answer.
* Chal Author Notes: EU snow coverage. Only Bulgaria and Hungary have snow in EU countries in google maps. Also the bins are super common in Bulgaria.
* Bulgaria = b

### Image 16:

![16](https://user-images.githubusercontent.com/91157382/212570295-cd5813a6-a3ac-41a7-b771-96b0db54c4b2.png)

* This image is actually much easier than it seems. White lines on the outside combined with the white on black chevron on geohints immediately narrows it down to basically only Albania or Switzerland. The clue that actually confirmed this for me was the rift that can be seen at the top of the image. Geohints has a section for rifts and going through it I could see Albania has very distinctive rifts that resemble what is seen in the image.
* Chal Author Notes: Chevrons and rift in camera. Camera rifts are in Albania, Montenegro, and Senegal.
* Albania = a

### Image 17:

![17](https://user-images.githubusercontent.com/91157382/212570310-80d6db81-55c6-4914-a1c3-61644b68f3b4.png)

* I will say this image is pretty tough. There weren't any distinctive clues I was able to use to find this. Basically I kept trying reverse image searching different parts and I was getting Russia a lot. I believe this is Yuzhno-Kurilsk, an urban locality in Russia. If you think this is a bit far-fetched guessing please read my conclusion for an important part of this challenge.
* Chal Author Notes: There is an obscure meta for the image that narrows it down to part of a country. The Sakhalin plant! This is a unique plant found in Sakhalin and Hokkaido and it's clearly not Japan.
* Russia = R

# Conclusion: 

* I do want to say an important part of this challenge was the flag that was being created while going through the images. One tactic that I think would help is compiling all of your guesses into a list and viewing your possible resulting flags. We were still unsure on about 4-5 countries at some point, but we had some guesses and my teammate said that: "Maybe it spells Break_my_spacebar". We laughed at the guess at first, but it ended up being only one letter off. So if you had situations like Ukraine vs Poland or Canada vs USA, compiling such a list and seeing words form can help you fill in any final gaps.
* Anyways I hope this writeup helped you. If you liked it or you see any issues with this writeup please dm me at Rench#9671 on Discord. Thanks for reading!

### Flag: idek{BReAK_me_sPaCEbaR}
