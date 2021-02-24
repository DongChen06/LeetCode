s = '[}'
length = len(s)
if length%2 == 0:
    flag = True
    for i in range(length//2):
        if s[length//(2*i)] != s[length//(2*i)]:
            flag=False
            break    
    print(flag)        
else:
    print(False)