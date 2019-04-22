import requests
import re
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

name = "Explo"
url = "https://jstris.jezevec10.com/u/" + name + "/stats?mode=1&displayAll=true"
regex = '"x":(\d+),"y":(\d+.\d+)'
parser = re.compile(regex)
content = requests.get(url).content.decode('utf-8')

sprints = parser.findall(content)
count = 0
time = 0
lowest = 1000000.0
highest = 0.0
Xtime = []
Ytime = []
meanTime = []
keep = []
sprints.sort(key=lambda tup: tup[0])
currentDay = sprints[0][0]
for item in sprints:
    if float(item[1]) < 600.0:
        if currentDay != datetime.date.fromtimestamp(int(item[0])):
            if len(keep) != 0:
                meanTime.append((currentDay, sum(keep)/len(keep)))
            currentDay = datetime.date.fromtimestamp(int(item[0]))
            keep = []
        print(item)
        count += 1
        time += float(item[1])
        if float(item[1]) < lowest:
            lowest = float(item[1])
        if float(item[1]) > highest:
            highest = float(item[1])
        Xtime.append(int(item[0]))
        Ytime.append(float(item[1]))
        keep.append(float(item[1]))


totalTime = str(datetime.timedelta(seconds=int(time)))

print(name + " has finished sprint 40 lines " + str(count) + " times!")
print("With the average sprint time in the last day of play at " + str(meanTime[-1][1]) + " seconds.")
print("Personal best being " + str(lowest) + " seconds.")
print("Personal worst being " + str(highest) + " seconds.")
print("and spent " + totalTime)


xFix = []
for number in Xtime:
    xFix.append(datetime.date.fromtimestamp(number))
plt.plot(xFix, Ytime, 'ro')
x, y = zip(*meanTime)
plt.plot(x, y)
plt.ylim(10, 120)
plt.xlabel("Date")
plt.ylabel("Time")
plt.title(name)
plt.show()

