myNum = [1,2,3]

for x in myNum:
    for y in myNum:
        for z in myNum:
            if y != x:
                if z != y:
                    print(x,y,z)


#loop through list x
    #loop through list y, ignore x
        #loop through list z, ignore x and y