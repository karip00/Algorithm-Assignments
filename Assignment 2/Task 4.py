#task 4
inFile = open('input4.txt','r')
N = int(inFile.readline())
elements = inFile.readline().split()
inFile.close()
for s in range(len(elements)):
  elements[s] = int(elements[s])

def merge(A, start, mid, end):
  l = (mid-start)+1
  r = end-mid

  left = [0]*l
  right = [0]*r

  for idx in range(l):
    left[idx] = A[start+idx]
  for idx in range(r):
    right[idx] = A[mid+1+idx]
  i = 0
  j = 0
  k = start

  while i < l and j < r:
    if left[i] < right[j]:
      A[k] = left[i]
      i += 1
      k += 1
    else:
      A[k] = right[j]
      j += 1
      k += 1

  while i < l:
    A[k] = left[i]
    i += 1
    k += 1
  
  while j < r:
    A[k] = right[j]
    j += 1
    k += 1

def mergeSort(A, start, end):
  if start < end:
    mid = (start+end)//2
    mergeSort(A,start,mid)
    mergeSort(A,mid+1,end)
    merge(A,start,mid,end)

outFile = open('output4.txt','w')
mergeSort(elements,0,len(elements)-1)
for num in elements:
  outFile.write(str(num)+' ')
outFile.close()