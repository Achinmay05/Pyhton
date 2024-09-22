def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word)) #strip the given word
        return n
        
    
l = ["chinmay", "somu", "shubhi", "chutuk"]
print(rem(l, "ay"))