s = '[[}'
length = len(s)
if length%2 == 0:
    flag = True
    for i in range(length//2):
        if (s[i] == '{' and s[length-i-1] =='}') or (s[i] == '[' and s[length-i-1] ==']') or (s[i] == '(' and s[length-i-1] ==')'):
            continue
        else:
            flag=False
            break    
    print(flag)        
else:
    print(False)