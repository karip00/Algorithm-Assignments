### Task 4 - working fine
import math
from queue import PriorityQueue

def ud_adjList(li):  #adjacent list for undirected graph
  result = {}
  for lists in li:
    if lists[1] == 0:    #if there is a single node in the graph and no edges (test case 1)
      result[lists[0]] = []
      result[lists[0]].append([None,lists[2]])
    else:
      if lists[0] not in result.keys(): #li[c][0] refers to the base/parent(?) nodes
        result[lists[0]] = []
      if lists[1] not in result.keys(): #li[c][1] refers to the neighbor nodes
        result[lists[1]] = []
      result[lists[0]].append([lists[1],lists[2]]) #{parent node: [neighbor node]}
      result[lists[1]].append([lists[0],lists[2]]) #{neighbor node: [parent node]} as it is undirected ##2nd part##
  return result

def dijkstra(graph, source, destination = None):
  
  visited = []
  dist = {}
  parentInfo = {} #stores the parent value for each node while traversing
  pQ = PriorityQueue()  #using priority queue library, takes 2 parameter in tuple or list format
  for node in graph.keys():
    dist[node] = math.inf  #initially setting the distance value of all nodes to infinty
    pQ.put([dist[node],node]) 
  
  while pQ.empty() == False: #while priority queue not empty
    u = pQ.get()[1] #returns the element, [0] for priority value, [1] for element
    visited.append(u)

    for nbr in graph[u]: #for the neighbors of u in the graph
      if u == source:
        dist[u] = 0 #setting source value to 0
      v = nbr[0]
      if v == None: #for single node/ no edge (test case 1)
        dist[u] = 0
        return dist, parentInfo

      alt = dist[u]+int(nbr[1]) #why called relaxation tho, sounds weird
      if alt < dist[v]:
        dist[v] = alt  #updating the dist values of v if condition is met
        pQ.put([dist[v],v]) #adding v with its priority value as its dist value
        parentInfo[v] = u #storing parent nodes
    
  return dist, parentInfo

def shortestPath(distances, source, destination, result):   #from dijkstra
  shortestPathInfo = distances[1]
  if shortestPathInfo == {}:
    result.append(source)
    return result

  else:
    if destination == source:
      result.append(source)
      #return result  #not working? why 
    else:
      result.append(destination)
      shortestPath(distances, source, shortestPathInfo[destination], result)
      result.reverse()
      return result

i4 = open('input4.txt','r')
fileInfo = i4.readlines()
i4.close()
allgraphInfo = []
for info in fileInfo:
  allgraphInfo.append(info.split())
impGraph = ud_adjList(allgraphInfo)
o4 = open('output4.txt','w')
shortestDistances = dijkstra(impGraph,'Motijheel')
x = shortestDistances[0]['MOGHBAZAR']
o4.write(f'Shortest Distance from Motijheel to Moghbazar: {x} \n')
fastestRoute = shortestPath(shortestDistances, 'Motijheel', 'MOGHBAZAR', [])
o4.write(f'Fastest Route: {fastestRoute}')
o4.close()