import csv

fileMatrix=[]
file=open("2008.csv","rt",encoding="UTF8")

lineContent=file.readline()

while (lineContent!=""):
    fileMatrix.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()

# ----------공통 속성-------------
commonL=fileMatrix[0][4:]   #공통된 att

for i in range(2009,2017):
    tempL=[]
    file=open(str(i)+".csv","rt",encoding="UTF8")

    list2=file.readline() #첫줄만 읽음

    file.close()
    
    for j in range(len(commonL)):
        if commonL[j] in list2:
            tempL.append(commonL[j])
    commonL=tempL[:]


# ----------공통 지역-------------
locationL=[]
for i in range(1,len(fileMatrix)):
    locationL.append(fileMatrix[i][3])

for i in range(2009,2017):
    tempAll=[]
    tempLocationL=[]
    tempL2=[]
    file=open(str(i)+".csv","rt",encoding="UTF8")

    otherYearLine=file.readline()
    while(otherYearLine!=''):
        tempAll.append(otherYearLine.strip("\n").split(","))
        otherYearLine=file.readline()

    file.close()

    for j in range(1,len(tempAll)):
        tempLocationL.append(tempAll[j][3])

    for j in range(len(locationL)):
        if locationL[j] in tempLocationL:
            tempL2.append(locationL[j])
    locationL=tempL2[:]


#----공통된 지역,속성으로 리스트 만들기------

myL=[ [0 for i in range(len(commonL)+1)] for i in range(len(locationL)+1) ]
myL[0][0]="지역"
for i in range(len(commonL)):
    myL[0][i+1]=commonL[i]

for i in range(len(locationL)):
    myL[i+1][0]=locationL[i]




#-----합치기-----

for i in range(2008,2017):
    fileMatrix=[]
    file=open(str(i)+".csv","rt",encoding="UTF8")

    lineContent=file.readline()

    while (lineContent!=""):
        fileMatrix.append(lineContent.strip("\n").split(','))
        lineContent=file.readline()

    for a in range(1,len(myL)):
        find=False
        for b in range(1,len(fileMatrix)):
            if find==True:
                break
            elif fileMatrix[b][3]==myL[a][0]:
                find=True
                for c in range(1,len(myL[0])):
                    for d in range(4,len(fileMatrix[0])):
                        if fileMatrix[0][d]==myL[0][c]:
                            try:
                                myL[a][c]+=float(fileMatrix[b][d])
                            except:
                                pass
                            break


   

# 파일쓰기
file=open("sum_to_one.csv","w",newline="",encoding='utf-8-sig')

fileW=csv.writer(file)

for i in range(len(myL)):
    fileW.writerow(myL[i])

file.close()







