# Can You Hack It 2023
Current points: 815
Still need:
- Birthday, Secure OTP, Tiles*
- WPA2 Deauth
- Lonely Bot
- "Frequency Analysis", Hidden Pictures
- XOR, ENIGMA, Ransom
- Defeating Dr. D Bugg*, Sentence Bot, Debug Me
- Cross Site Scripting

Most of the challenges I've solved I already see writeups for except for Stack Overflow (Exploitation) and Defuse (Reverse Engineering). The two I have starred, Defeating Dr. D Buggs and Tiles, are the next things on my agenda that I will do a writeup on.

## Stack Overflow

## Defuse

Defuse was tougher simply because there were a lot more steps, but when you broke them down it becomes easier. Honestly the worst part was getting it to run on a 64-bit machine I had to go back to an old 32-bit VM I had.

When you put the binary through Ghidra, you see that this program is split up into 4 parts: phase_unlock, phase_disarm, phase_reverse, and phase_disposal. 

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/f7cea77e-17a7-4b54-bca7-fca847b032b9)

We'll focus on each step by step. First, we have to bypass the debugger check. Good thing the functions aren't stripped!
Open up gdb and set a breakpoint on check_debugger, then when it stops set $eip=*(main+83), a value you can get by looking at disas main.

Alright, now that that's out of the way, let's get to part 1: phase_unlock.

### phase_unlock

When you open up the function in Ghidra, you can see it compares your input with a preset string:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/61bfcbf8-b422-404f-ac5a-43e9bb7d3c59)

When you convert the hex to ASCII, you get your 12 letter code. For me however, the binary through Ghidra and through gdb was different (I had reloaded sessions). Since ASLR is not on, you can do x/10s 0x080eb26c to see the string.

### phase_disarm

When you get to this part, the bomb will explode after .1 seconds. Fortunately, Ghidra comes to the rescue. If you quickly pass in CTRL + Z, the timer is deactivated.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/f933bab0-94f0-4919-a9d3-76170d4d9193)

The second part is figuring out which sequence of wires to cut, and this is trickier. There is a stored location called wire_cut_sequence where it goes 1 4 3 0 2 6 5.

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/08181550-6da6-45b7-8352-b66e89330eaf)

Here is the code:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/b6fe3652-3999-4faa-acc5-9e4ece5f49e0)

You can see with the for loop at the end that the order of arr (a variable which I renamed)
