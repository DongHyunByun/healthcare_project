import csv

fileMatrix=[]
file=open("sum_to_oneW.csv","rt",encoding="UTF8")

lineContent=file.readline()

while (lineContent!=""):
    fileMatrix.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()

fileMatrix[0].extend(["당뇨병진단경험률_0816_표준화율","이상지질혈증진단경험률_1116_표준화율","고혈압진단경험률_0816_표준화율"])

#당뇨병
diaL=[]
file=open("dia0816.csv","rt")

lineContent=file.readline()

while (lineContent!=""):
    diaL.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()

for i in range(1,len(fileMatrix)):
    for j in range(1,len(diaL[0])):
        if (fileMatrix[i][0]==diaL[0][j]):
            fileMatrix[i].extend([diaL[10][j]])
            break


#이상지질혈증
dysL=[]
file=open("dys1116.csv","rt")

lineContent=file.readline()

while (lineContent!=""):
    dysL.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()

for i in range(1,len(fileMatrix)):
    for j in range(1,len(dysL[0])):
        if (fileMatrix[i][0]==dysL[0][j]):
            fileMatrix[i].extend([dysL[7][j]])
            break


#고혈압
hbpL=[]
file=open("hbp0816.csv","rt")

lineContent=file.readline()

while (lineContent!=""):
    hbpL.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()

for i in range(1,len(fileMatrix)):
    for j in range(1,len(hbpL[0])):
        if (fileMatrix[i][0]==hbpL[0][j]):
            fileMatrix[i].extend([hbpL[11][j]])
            break




#파일쓰기
file=open("finalTable.csv","w",newline="",encoding='utf-8-sig')
fileW=csv.writer(file)


for i in range(len(fileMatrix)):
    fileW.writerow(fileMatrix[i])

file.close()

