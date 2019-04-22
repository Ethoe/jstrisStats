import requests
import re
import datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from scipy import stats
import math

name = "Ethoe"
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
sprints.sort(key=lambda tup: tup[0])
for item in sprints:
    if count > 2:
        tDist = stats.t.ppf((1 - .01) / 2, count - 1)
        mean = time/count
        stdCount = 0
        for number in Ytime:
            stdCount += (number - mean) * (number - mean)
        std = math.sqrt((1/count) * stdCount)
        high = (tDist * (std/math.sqrt(count))) + mean
    else:
        high = 10000.0

    if float(item[1]) < high:
        print(item)
        count += 1
        time += float(item[1])
        if float(item[1]) < lowest:
            lowest = float(item[1])
        if float(item[1]) > highest:
            highest = float(item[1])
        Xtime.append(int(item[0]))
        Ytime.append(float(item[1]))


totalTime = str(datetime.timedelta(seconds=int(time)))

print(name + " has played sprint 40 lines " + str(count) + " times!")
print("With the average sprint time of " + str(time/count) + " seconds.")
print("Personal best being " + str(lowest) + " seconds.")
print("Personal worst being " + str(highest) + " seconds.")
print("and spent " + totalTime)

plt.plot(Xtime, Ytime)
plt.show()

