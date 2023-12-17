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


def test():
    list_ans = list(answer)
    test_answer = ""
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
        
    for p in list_ans:
        test_answer += p
    return test_answer

print("Testing for accuracy: ")
print(test())

#fun fact, to get all capitals after scrambling the string is:
# QUieTroBOtpLEaSe
        
