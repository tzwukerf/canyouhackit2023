I am pretty sure you can brute force this challenge (which is why I'm guessing why it's been solved 250+ times) if you run ./sentencebot --setseed={brute forced number} but I wanted to challenge myself by looking through the binary.

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

You can see "the" is at address 0049b75e. When you double click ARTICLES, it starts at 004c9900. Since 
