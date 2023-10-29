#COMPLETE
from queue import PriorityQueue

i1 = open('input1.txt', 'r')
fileInfo = i1.readlines()
i1.close()
allInfo = []
for info in fileInfo:
  x = info.split()
  for i in range(len(x)):
    x[i] = int(x[i])
  allInfo.append(x)
N = allInfo[0][0] 
allInfo = allInfo[1:]

pQ = PriorityQueue()
for lists in allInfo:
  pQ.put([lists[1], lists])


sortedArr = []
for i in range(len(allInfo)):
  time = pQ.get()[1]
  sortedArr.append(time)

o1 = open('output1.txt','w')
count = 0
result = []
for i in range(len(sortedArr)):
  if i == 0:
    f = sortedArr[i][0]
    result.append(f"{sortedArr[i][0]} {sortedArr[i][1]} \n")
    count += 1
  elif sortedArr[i][0] >= f:
    f = sortedArr[i][1]
    result.append(f"{sortedArr[i][0]} {sortedArr[i][1]} \n")
    count += 1
o1.write(f'{count} \n')
for line in result:
  o1.write(line)
o1.close()