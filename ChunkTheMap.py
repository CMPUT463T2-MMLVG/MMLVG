def main():
    fileNum = 0
    ## get the file name or path 
    fileName = input("Please enter your file name/path: ")
    horN = int(input("Please enter the length of horizontal: "))
    verN = int(input("Please enter the length of vertical: "))
    F = open(fileName,"r")
    lines = F.readlines()
    #print(lines)
    LineCount = len(lines)
    
    #print(LineCount)
    LongestLine=0
    for char in (max(open(fileName, 'r'), key=len)): LongestLine +=1
    #print(LongestLine) 

    


    
    outputFile = open('chunk_%d.txt'%(fileNum),'w')
    C=0 
    preSet = 0
    i = 0
    
    while i < LineCount:
        chunkLine = ""
        for j in range(verN):
            line = lines[i]
            lineLen = len(line)
            #print(lineLen)
            if C+j < lineLen:
                #print("Here is C\n")
                #print(C)
                chunkLine += line[C+j]
            else:
                chunkLine += "@"
        chunkLine += "\n"
        outputFile.write(chunkLine)
        i+=1


        if (i+1)% horN == 0 or i+1 == LineCount:
            outputFile.close()
            fileNum+=1
            outputFile = open('chunk_%d.txt'%(fileNum),'w')
            C += verN
            print(preSet)
            i = preSet
            
        if C >= lineLen:
            C = 0 
            if (preSet + horN) <LineCount:
                preSet += horN
            else:
                break


            
main()
