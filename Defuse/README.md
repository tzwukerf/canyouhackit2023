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

You can see with the for loop at the end that the order of arr (a variable which I renamed). To simplify the code, what it is asking is that the order of the wires we're supposed to cut is the index of the wire_cut_sequence numbers from least to greatest. To illustrate:

wire_cut_seq: 1 4 3 0 2 6 5

index:        0 1 2 3 4 5 6

You can see that the lowest value for wire_cut_sequence is at index 3 with a value of 0, the second lowest is at index 0 with a value of 1, and so on. In the end, we get our solution, which is 3 0 4 2 1 6 5.

## phase_reverse

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/c9f943ff-dae7-4de5-a298-ce91d42040d6)

Because it only passes when your sum is -1 but you can't have any of your value be negative, this means we have to do an integer overflow. We have three numbers to work with. You can see by values at the top that all of our numbers are int, not unsigned int, meaning that our numbers are in two's complement. This means we want our result, -1, to be a lot of 1s (ffffff...)

We running a 32 bit program, meaning that the first bit (the most significant bit) can't be zero for any of our three values or else that would be a negative number. We have to come up with a solution like this:

1st: 0111...11
2nd: 0100...00
3rd: 0100...00

This way, we get our -1. The three numbers are 2147483647, 1073741824, 1073741824.

## phase_disposal

This section uses gets to get user input, a highly unsafe function. Good thing we're the ones exploiting it :)

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/52a38541-39b1-4d6e-a307-b74900693232)

You can see that input is right above check_light and dis_mode (dispatch mode) (For anyone confused, it believes you'll input 6 characters, so undefined4 + undefined2). You can also see the if conditions you want:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/5a1293a8-83d2-4f6f-be69-64c8dfb6ddff)

Inputting cache/EG should do the trick. If not (mine's didn't; it was cache.EG) then you can once again check x/20s 0x080eb27c in GDB.

Finally, you have all the inputs you need to defuse the bomb and solve the challenge.
