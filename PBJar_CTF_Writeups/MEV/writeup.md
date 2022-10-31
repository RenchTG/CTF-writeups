# Challenge Info:

#### Challenge Name: MEV

#### Challenge Author: bruh.#0766

#### Challenge Description: The miner of Block #12983883 on the Ethereum Blockchain partakes in the common practice of MEV. What is the exact amount of Ether that was transfered to the miner as a bribe from the transaction that was included first in this block? Info about MEV: https://ethereum.org/en/developers/docs/mev/ Flag format: flag{0.006942069420}

#### Files Provided: none

# TLDR:

#### - Go on etherscan.io and find the block provided in the challenge description.
#### - Find the first transaction on that block.
#### - Copy the exact amount transferred to the MEV bot and that's the flag.

# In-Depth Solution: 

#### This challenge is surprsingly the second to least solved challenge in the misc category *excluding survey* which I thought was kind of weird as I had less trouble with it than some of the other misc challenges. Anyways I digress, here's my solution.

#### In the description we are given a block # that is in fact on the etherium blockchain so no ropsten this time. Then we are told a little about the practice of MEV and given a link to learn about it. However, reading is lame so let's just go right into it. We fire up etherscan.io, put in the name of the block, and now we must find as the challenge states: "the exact amount of Ether that was transfered to the miner as a bribe from the transaction that was included first in this block". Now that last part is the most important in regards to where to look. We now know we can find it in the first transaction included in this block. First I clicked the:

`145 transactions`

#### link and was taken to this page: https://etherscan.io/txs?block=12983883. I went to the very first transaction, but I don't see any sketchy bribing here 👀. Then I go back and click the:

`26 contract internal transactions`

#### link and was taken to this page: https://etherscan.io/txsInternal?block=12983883. Scrollarooni down to the bottom and wow there cowboy, `MEV Bot: 0x4d2...2d3` and `Wrapped Ether` should be exactly what we're looking for. We know this is something to do with MEV as the ether was transferred to an MEV bot and the wrapped ether must of course be the bribe payment. We can also see that both have identical ether values of 0.009672680170055 Ether.

#### Submit that number and it's the flag. In my opinion this challenge should have had much more solves as it really only entailed looking at a block's first transaction but whatever. Enjoy your flag!

## Flag: flag{0.009672680170055}
