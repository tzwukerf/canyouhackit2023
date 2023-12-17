This is the given code decompiled through Ghidra:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/a8602dd8-9071-4226-a84f-8538b35ddcc6)

When you go into get_influence_index (or read his notes), you can see what j is being set to, which is (13i + 7) mod 16. To break it down, what this code does is this:

```
i = 0
j = 7
while True:
  j = (i*13 + 7) % 16
  if list_ans[j].islower():
    list_ans[i] = list_ans[i].swapcase()
  if ord(list_ans[j]) & 1 == 1:
    list_ans[i] = list_ans[i].swapcase()
  if i == 13:
    break
  i = j
```

Note the j and i. If the character at j is lower, then you change the case of the character at i.

With this, we can write our unscrambler:

```
target = "quietrobotplease"
string = list(target)
answer = ""
j = 0
i = 13
while j != 7:
    if ord(string[j]) & 1 == 0:
        string[i] = string[i].swapcase()
    if string[j].isupper():
        string[i] = string[i].swapcase()
    j = i
    while (j - 7) % 13 != 0:
        j += 16
    
    i = int((j - 7) / 13)
    j = int(j % 16)

for i in string:
    answer += i

print("The answer is: ")
print(answer.swapcase())
```
After you run it, you can see the answer:

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/60155418-b6a0-437f-8b33-f855bb67c1ee)

The Python file, as well as the testing for correctness, are in dr.d_script.py

