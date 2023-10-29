#Task 2
inputFile = open('input2.txt','r')
info = inputFile.readline().split()
elements = inputFile.readline().split()
inputFile.close()

n = int(info[0])
m = int(info[1])

c = 0 
while c < len(elements):
  elements[c] = int(elements[c])
  c += 1


def selectionSort(A, length):
  for i in range(length):
    minIdx = i
    minVal = A[i]
    for j in range(i+1, length):
      if minVal > A[j]:
        minIdx = j
        minVal = A[j]
    A[minIdx] = A[i]    
    A[i] = minVal
  return A

if m > n:
  print("Invalid input")
else:
  result = selectionSort(elements, n)

outFile = open('output2.txt', 'w')
for i in result[:m]:
  outFile.write(str(i)+' ')
outFile.close()