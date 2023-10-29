### Task 5

import math
from queue import PriorityQueue

def d_adjList(li, lastNode, start): #adjacent list for directed graph
  result = {}
  if start not in result.keys():
    result[start] = []
  for lists in li:
    if lists[1] == 0:
      result[lists[0]] = []
      result[lists[0]].append([None,lists[2]])
    else:
      if lists[0] not in result.keys():
        result[lists[0]] = []
      if lists[1] not in result.keys():
        result[lists[1]] = []
      result[lists[0]].append([lists[1],lists[2]])
  return result

def weirdDijkstra(graph, source, destination = None): #might use for task 5?
  visited = []
  dist = {}
  pQ = PriorityQueue() 
  dist[source] = math.inf
  pQ.put([dist[source],source])
  for node in graph.keys():
    if node != source:
      dist[node] = -math.inf 
      pQ.put([dist[node],node]) 
  while pQ.empty() == False: 
    u = pQ.get()[1]
    visited.append(u)
    
    for nbr in graph[u]: 
      v = nbr[0]
      if v == None: 
        dist[u] = 0
        return dist

      alt = min(dist[u], nbr[1]) 
      if alt > dist[v]:
        dist[v] = alt  
        pQ.put([dist[v],v]) 
 
  if graph[source] == []:
    for node, nbr in graph.items():
      if nbr != [] and nbr[0][0] == source:
        dist[node] = -(nbr[0][1])
  if dist[source] == math.inf:
    dist[source] = 0

  return dist


i5 = open('input5.txt','r')
fileInfo = i5.readlines()
i5.close()
graphAmount = int(fileInfo[0])
source = int(fileInfo[-1])
allInfo = []
for info in fileInfo[1:]:
  allInfo.append(info.split())

for lists in allInfo:
  for i in range(len(lists)):
    lists[i] = int(lists[i])

c = 0
o5 = open('output5.txt','w')
for times in range(graphAmount):
  deviceAmount = allInfo[c][0]
  linkAmount = allInfo[c][1]
  source = allInfo[c+linkAmount+1][0]
  if deviceAmount == 1 and linkAmount == 0:
    tempInfo = [[1,0,0]]
  else:
    tempInfo = allInfo[c+1: c+linkAmount+1]
  tempInfo = d_adjList(tempInfo, deviceAmount, source)
  output = weirdDijkstra(tempInfo, source)
  orderedOutput = {}
  for item in sorted(output):
    orderedOutput[item] = output[item]
  for val in orderedOutput.values():
    o5.write(f'{val} ')
  o5.write('\n')
  c += linkAmount + 2