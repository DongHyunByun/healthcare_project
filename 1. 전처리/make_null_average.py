import csv

#2008년부터17은 19부터
#2012년부터16은 20부터

for f in range(2012,2017):
    fileMatrix=[]
    averageL=["코드","시도","시군구","지역","CHS"]

    file=open(str(f)+".csv",  'rt', encoding='UTF8')

    lineContent=file.readline()

    while(lineContent!=""):
        fileMatrix.append(lineContent.strip("\n").split(','))
        lineContent=file.readline()

    file.close()



    for i in range(4,len(fileMatrix[0])):
        sum=0
        n=0
        for j in range(19,len(fileMatrix)):                
                try:
                    sum+=float(fileMatrix[j][i])
                    n+=1
                except:
                    fileMatrix[j][i]="N"

        if n==0 :
            averageL.append(0)
        else :
            averageL.append(sum/n)


    for i in range(19,len(fileMatrix)):
        for j in range(len(fileMatrix[0])):
            if fileMatrix[i][j]=="N":
                fileMatrix[i][j]=averageL[j]




    file=open(str(f)+"w.csv","w",newline="",encoding='utf-8-sig')
   
    fileW=csv.writer(file)

    fileW.writerow(fileMatrix[0])
    for i in range(19,len(fileMatrix)):
        fileW.writerow(fileMatrix[i])

    file.close()


