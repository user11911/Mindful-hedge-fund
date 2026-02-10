import requests
import math
import os



def avantage():
    key = "0ZVANKZ44YK77ALW"
vol = 0
def filetodata():
    a = []
    with open((os.getcwd()+ "\\brentcrude25101324.txt")) as f:
        for line in f:
            line = line.replace("\n","")
            if line.split(",")[0] == "price":
                continue
            splited = line.split(",")
            a.append([float(splited[0]), float(splited[1])])
    return a
a = filetodata()

def getVol(data, period0, period1):
    mean = getMean(data, period0, period1)
    vol = 0
    for i in range(1,len(data)):
        if data[i][1] <= period1 and data[i][1] >= period0:
            vol+= abs(mean - float(data[i][0]))/(len(data)*mean)
    vol*=math.sqrt(252)
    return vol
def getMean(data, period0, period1):
    mean = 0
    it = 0
    for i in range(1,len(data)):
        if data[i][1] <= period1 and data[i][1] >= period0:
            mean+= data[i][0]
            it+=1
        else:
            continue        
    return mean/len(data)
print(getVol(a, 1660313600, 1860441040))
    