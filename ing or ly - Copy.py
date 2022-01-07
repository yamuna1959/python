strl=input("Enter a String:")
length=len(strl)
if length>2:
    if strl[-3:]=='ing':
        strl+='ly'
    else:
        strl+='ing'
print("New String:",strl)
