
import pandas as pd

with open("reportData.txt" ,'r') as f:
    data = f.readlines()

websiteList = []
proxyList = []
sleepTimeList = []
totalTimeList = []
for item in data:
    if item != "\n":
        listItem = item.split(',')
        print(listItem)
        websiteList.append(listItem[0])
        proxyList.append(listItem[1])
        sleepTimeList.append(listItem[2])
        totalTimeList.append(listItem[3])
df = pd.DataFrame({"Website": websiteList, "Proxy": proxyList, "Sleep Time": sleepTimeList, "Total Time": totalTimeList})
df.to_excel("Report2.xlsx")