def compress(chars):
    s = ""
    
    if len(chars) == 1:
        return 1 
    
    diff_char = []
    for char in chars:
        if char not in diff_char:
            diff_char.append(char)
            
    for current_char in diff_char:
        count = 0
        s += current_char
        for char in chars:
            if char == current_char:
                count += 1
        if count == 1:
            s += "1"
        else:
            s += "{}".format(count)
    
    chars = []
    for i in s:
        chars.append(i)
    
    return chars
        
            
chars = ["a","a","b","b","c","c","c"]
print(compress(chars))