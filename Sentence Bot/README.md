I am pretty sure you can brute force this challenge (which is why I'm guessing why it's been solved 250+ times) if you run ./sentencebot --setseed={brute forced number} but I wanted to challenge myself by looking through the binary. What I did is also brute forcing, but where my method shines is that if the program ever consisted of a small delay (let's say 3-10 seconds) then the other method is completely inefficient. For this program though, there is no difference. Choose whatever you prefer.

When you look through getFlag(), you see this:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/3374674b-06df-45d7-8408-ea879bc8348c)

Firstly, you need to set your MAC address to de:ad:be:ef. Since I am using WSL2 for Linux, I had to set it through Windows' Device Management. You can verify your MAC address by doing ./sentencebot --debug:

There are two methods for doing the next part. You can run a bash script in which you try all seeds from 0 to max seed value and record whichever value gives you "You win!"

I wanted to challenge myself by reading through the decompiler.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/bffb1013-7d1b-4465-bcd4-251ec817b665)

As you can see, based on your seed, it calls rand() and adds that value modded with a number times 8 to an address. In other words, let's say rand() gives you 3, it will do (3 % 6) * 8 and add it to the memory address of where ARTICLES is stored.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/7b5ab520-da86-4c46-bef4-136daff20149)

Based in this line, we have to get the article to be "the", the noun to be "flag", and the verb to be "is". You can search for these strings in Ghidra.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/8018a972-d15a-44e4-9479-cdeb6a2fd0b5)

You can see "the" is at address 0049b75e. When you double click ARTICLES, it starts at 0x004c9900. Since you saw the type was *(char **) ARTICLES + ..., this means that whatever is stored at ARTICLES + offset is going to be a pointer to "the". So we look at whatever is going to be 004975e.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/d3a43dd6-2fc7-4161-ba10-2a96359fa94c)

You can see it is at 0x004c9928 (because it stores the pointer to "the"). We find the difference between 0x4c9928 and 0x4c9900, which is 40, which means we need an x such that x % 6 = 5. You repeat this for the others.

(The values for NOUNS: 00495c0, VERBS: 004c95c0. "is": 0049b746, "flag": 0049b274. Pointer to "is": 004c98e0, pointer to "flag": 004c9420.)

The results of this is that we need a seed such that on the first call to rand() gives us a number such that modded with 6 gives us 5, on the second rand() call y % 101 = 100, on the third rand() call z % 101 = 100. We can do this by iterating over all the seeds and printing this number. This gets us the seed we need, which is 19016, and prints out the flag for us.

