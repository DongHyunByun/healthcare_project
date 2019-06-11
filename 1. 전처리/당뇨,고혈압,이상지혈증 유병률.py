import csv

di=["당뇨","고혈압","이상지질혈증"]

dia=open(di[0]+"W.csv", 'w',newline='') 
diaW=csv.writer(dia)
    

high=open(di[1]+"W.csv", 'w',newline='') 
highW=csv.writer(high)

ex=open(di[2]+"W.csv", 'w',newline='') 
exW=csv.writer(ex)


#파일이름 입력
filename=input()

while(filename!="종료"):
    fileMatrix=[]
    dindex=[0,0,0] #인덱스번호
    localL=[["n"]*269,["n"]*269,["n"]*269]



    file = open(filename+'.csv',  'rt', encoding='UTF8')

    lineContent = file.readline()

    while lineContent!='':
        fileMatrix.append(lineContent.strip('\n').split(','))
        lineContent = file.readline()

    file.close()



    # dindex[0]:당뇨인덱스, 1:고혈압 인덱스, 2:이상지질혈증 인덱스
    for i in range(len(fileMatrix[0])):
        if ("당뇨병진단경험률_"+filename+"_표준화율" in fileMatrix[0][i]):
            dindex[0]=i
        elif ("고혈압진단경험률_"+filename+"_표준화율" in fileMatrix[0][i]):
            dindex[1]=i
        elif ("이상지질혈증진단경험률_"+filename+"_표준화율" in fileMatrix[0][i]):
            dindex[2]=i

    #loname : 지역저장 (268개+1, 2008년기준)

    if(filename=="2008"):
        loname=[]
        lonum=[]
        for i in range(18,len(fileMatrix)):
            loname.append(fileMatrix[i][3])
            lonum.append(fileMatrix[i][4])

        loname=["병명"]+loname
        lonum=["지역코드"]+lonum

        diaW.writerow(loname)
        diaW.writerow(lonum)

        highW.writerow(loname)
        highW.writerow(lonum)

        exW.writerow(loname)
        exW.writerow(lonum)


    #localL : 유병률저장 (268개)

    for row in range(18,len(fileMatrix)):
        for j in range(269):
            if (fileMatrix[row][3]==loname[j]):
                
                for di in range(3):
                    localL[di][j]=fileMatrix[row][dindex[di]]

                break

    for i in range(3):
        localL[i][0]=filename

    diaW.writerow(localL[0])
    highW.writerow(localL[1])
    exW.writerow(localL[2])

    filename=input()

dia.close()
high.close()
ex.close()

    








