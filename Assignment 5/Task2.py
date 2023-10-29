#COMPLETE
from queue import PriorityQueue

i2 = open('input2.txt', 'r')
fileInfo = i2.readlines()
i2.close()
allInfo = []
for info in fileInfo:
  x = info.split()
  for i in range(len(x)):
    x[i] = int(x[i])
  allInfo.append(x)
N = allInfo[0][0]
M = allInfo[0][1]
allInfo = allInfo[1:]
pQ = PriorityQueue()
for lists in allInfo:
  pQ.put([lists[1], lists])

sortedArr = []
for i in range(len(allInfo)):
  time = pQ.get()[1]
  sortedArr.append(time)


f = [0]*M
for i in range(M):
  f[i] = sortedArr[i][1]
count = M
for i in range(M, len(sortedArr)):
  for j in range(len(f)):
    if f[j] <= sortedArr[i][0]:
      f[j] = sortedArr[i][1]
      count += 1
      break

o2 = open('output2.txt','w')
o2.write(f'{count}')
o2.close()