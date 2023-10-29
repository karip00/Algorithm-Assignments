#COMPLETE
from queue import PriorityQueue

i3 = open('input3.txt', 'r')
noOfTasks = int(i3.readline())

time = i3.readline().split()
for i in range(len(time)):
  time[i] = int(time[i])  #1 4 2 3
sortedTime = sorted(time) #1 2 3 4
Jack = []

calls = i3.readline()
jackSum = 0
jillSum = 0
o4 = open('output3.txt','w')
for call in calls:
  if call == 'J':
    jackSum += sortedTime[0]
    o4.write(f'{sortedTime[0]}')
    Jack.append(sortedTime[0])
    sortedTime.remove(sortedTime[0])
  else:
    jillSum += max(Jack)
    j = max(Jack)
    Jack.remove(j)
    o4.write(f'{j}')

o4.write('\n')
o4.write(f'Jack will work for {jackSum} hours \n')
o4.write(f'Jack will work for {jillSum} hours')
o4.close()