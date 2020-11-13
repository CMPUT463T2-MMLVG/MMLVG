import os
import config



def getRidMidNull(fileName,fileNum):
    F = open(fileName)
    FreeNullName = "Generated Levels/FreeNullFile%d.txt"%(fileNum)
    FreeNullFile = open(FreeNullName,"w")
    newFileName = "Generated Levels/Semi_graph/out_SEMI_chun%d.txt"%(fileNum)
    OutFile = open(newFileName,"w")
    lines = F.readlines()
    for line in lines:
        #print(line)
        for c in range(len(line)):
            if  line[c] == "@":
                FreeNullFile.write(line[:c])
                OutFile.write(line[c:])
                break
        OutFile.write("\n")
        FreeNullFile.write("\n")
    OutFile.close()
    FreeNullFile.close()
    if os.stat(newFileName).st_size == 0:
        return
    else:
        Fname = getRidFrontNull(newFileName)
        Fname2 = getRidBackNull(Fname)
        Fname3 = seperateMidNull(Fname2)
        config.shareFilenum+=1
        startChunk(Fname3,0,config.shareFilenum)
        config.shareFilenum+=1
        startChunk(FreeNullName,0,config.shareFilenum)
        getRidMidNull(Fname2,fileNum+1)


    

def startChunk(fileName,chunckedNum,fileNum):
    F = open(fileName,"r")
    lines = F.readlines()
    checkSpace  = F.read().split('\n')
    if checkSpace == "" or checkSpace == " ":
        return

    newFileName = "Generated Levels/Final_graph/out_chun%d.txt"%(fileNum)
    OutFile = open(newFileName,"a")
    
    while chunckedNum < len(lines):
        OutFile = open(newFileName,"a")
        if "@" in lines[chunckedNum] and os.stat(newFileName).st_size == 0:
            chunckedNum+=1
            
        elif "@" in lines[chunckedNum] and os.stat(newFileName).st_size != 0:
            OutFile.close()
            while "@" in lines[chunckedNum]:
                chunckedNum += 1
            config.shareFilenum+=1
            startChunk(fileName,chunckedNum-1,config.shareFilenum)
            return 
        else:
            if os.stat(newFileName).st_size == 0:
                OutFile.write(lines[chunckedNum])
                chunckedNum +=1
                OutFile.close()
            elif os.stat(newFileName).st_size != 0 and len(lines[chunckedNum]) == len(lines[chunckedNum-1]):
                OutFile.write(lines[chunckedNum])
                chunckedNum +=1
                OutFile.close()
            elif os.stat(newFileName).st_size != 0 and len(lines[chunckedNum]) != len(lines[chunckedNum-1]):
                OutFile.close()
                config.shareFilenum+=1
                startChunk(fileName,chunckedNum,config.shareFilenum)
                return 
    return 
            


def seperateMidNull(fileName):
    inFile = open(fileName,"r")
    inLines = inFile.readlines()
    outFile = open(fileName,"w")
    noMidNull = open("Generated Levels/noMidNull.txt","w")
    for i in range(0,len(inLines)):
        if '@' not in inLines[i]:
            noMidNull.write(inLines[i])
            outFile.write("\n")
        else:
            noMidNull.write("@\n")
            outFile.write(inLines[i])
    outFile.close()
    noMidNull.close()
    return "Generated Levels/noMidNull.txt"
    

    
            
def getRidBackNull(fileName):
    outerFile = open(fileName,"r")
    outerlines = outerFile.readlines()
    AfterNullFile = open("Generated Levels/noNull.txt","w")
    for line in outerlines:
        #print(line)
        for j in reversed(range(len(line))):

            #print(line[j])
            if line[j] == "@" or line[j] == "\n":
                pass
            else:
                
                AfterNullFile.write(line[:j+1]+"\n")
                break
    AfterNullFile.close()
    return "Generated Levels/noNull.txt"
    
    
def getRidFrontNull(fileName):
    F = open(fileName,"r")
    lines = F.readlines()
    PreNullFile = open("Generated Levels/noOuterNull.txt","w")
    for line in lines:
        for r in range(len(line)):
            if line[r] == "@":
                pass
            else:
                PreNullFile.write(line[r:])
                break
    PreNullFile.close()
    ######################################
    return "Generated Levels/noOuterNull.txt"
    



def main():
    fileName = input("Please enter your file name/path: ")
    Fname = getRidFrontNull(fileName)
    Fname2 = getRidBackNull(Fname)
    Fname3 = seperateMidNull(Fname2)
    config.shareFilenum = 0 
    startChunk(Fname3,0,config.shareFilenum)
    getRidMidNull(Fname2,0)

main()





