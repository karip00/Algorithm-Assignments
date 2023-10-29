#Task 3
inputFile = open('input3.txt','r')
N = int(inputFile.readline())
id = inputFile.readline().split()
marks = inputFile.readline().split()
inputFile.close()

for s in range(N):
  id[s] = int(id[s])
  marks[s] = int(marks[s])

dict1 = {}
for i in range(N):
  dict1[id[i]] = marks[i]


def insertionSort(A, n):
  for i in range(n-1):
    temp = A[i+1]
    j = i
    while j >= 0:
      if A[j] < temp:
        A[j+1] = A[j]
      else:
        break
      j = j-1
    A[j+1] = temp
  return A

rankedMarks = insertionSort(marks, N)
rankedID=[]

for mark in rankedMarks:
  for key,value in dict1.items():
    if mark == value:
      if key in rankedID:
        pass
      else:
        rankedID.append(key)

outFile = open('output3.txt','w')
for i in rankedID:
  outFile.write(str(i)+' ')
outFile.close()