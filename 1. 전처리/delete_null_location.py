import csv

fileMatrix=[]
file=open("sum_to_one.csv","rt",encoding="UTF8")

lineContent=file.readline()

while (lineContent!=""):
    fileMatrix.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()



fileMatrix2=[]
file=open("dys1116.csv","rt")

lineContent=file.readline()

while (lineContent!=""):
    fileMatrix2.append(lineContent.strip("\n").split(','))
    lineContent=file.readline()

file.close()


notInLocation=[]

for i in range(1,len(fileMatrix)):
    if (fileMatrix[i][0] not in fileMatrix2[0]):
        notInLocation.append(fileMatrix[i][0])


for i in notInLocation:
    for j in range(len(fileMatrix)):
        if (i==fileMatrix[j][0]):
            del fileMatrix[j]
            break



file=open("sum_to_oneW.csv","w",newline="",encoding='utf-8-sig')

fileW=csv.writer(file)

for i in range(len(fileMatrix)):
    fileW.writerow(fileMatrix[i])

file.close()
