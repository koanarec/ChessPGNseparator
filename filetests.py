f = open("chessdatamess.pgn","r")
x = open("chess0.txt","a")

contents = f.readlines()

c = len(contents)
print(c)
asd = 0
lcv3 = 1
lcvtitle = 0
n = 1
while asd != (c-1):
    
##    [Event "Rated Classical game"]
    if (contents[asd]) == '\n':
        n= n + 1
        if n == 3:
            lcvtitle = lcvtitle + 1
            x.close
            temp =  "chess" + str(lcvtitle) + ".txt"
            x = open(temp , "a")
            n = 1
    x.write(contents[asd])
    lcv3 = lcv3 + 1
    asd = asd + 1
            
        
    
        


x.close
