#Task 5a
inputFile = open('input5.txt','r')
elements = inputFile.readline().split()
for s in range(len(elements)):
  elements[s] = int(elements[s])
def quickSort(A,p,r):
  if p < r:
    q = partition(A,p,r)
    quickSort(A,p,q)
    quickSort(A,q+1,r)

def partition(A,p,q):
  x = A[p]
  i = p
  for j in range(p+1, q+1):
    if A[j] <= x:
      i += 1
      A[i],A[j] = A[j],A[i]
  A[p],A[i] = A[i],A[p]
  return i

outFile = open('output5.txt','w')
outFile.write('Unsorted: ')
for num in elements:
  outFile.write(str(num)+' ')
outFile.write('\n')
quickSort(elements,0,len(elements)-1)
outFile.write('Sorted: ')
for num in elements:
  outFile.write(str(num)+' ')
outFile.write('\n')
outFile.write('Time complexity: nlogn')
outFile.close()

#Task 5b