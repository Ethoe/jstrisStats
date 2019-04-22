import requests
import re
import datetime
import matplotlib.pyplot as plt

name = "jammburger"
url = "https://jstris.jezevec10.com/u/" + name + "/stats?mode=1&displayAll=true"
regex = '"x":(\d+),"y":(\d+.\d+)'
parser = re.compile(regex)
content = requests.get(url).content.decode('utf-8')

sprints = parser.findall(content)
count = 0
time = 0
lowest = 1000000.0
highest = 0.0
for item in sprints:
    print(item)
    count += 1
    time += float(item[1])
    if float(item[1]) < lowest:
        lowest = float(item[1])
    if float(item[1]) > highest:
        highest = float(item[1])

totalTime = str(datetime.timedelta(seconds=int(time)))

print(name + " has played sprint 40 lines " + str(count) + " times!")
print("With the average sprint time of " + str(time/count) + " seconds.")
print("Personal best being " + str(lowest) + " seconds.")
print("Personal worst being " + str(highest) + " seconds.")
print("and spent " + totalTime)
