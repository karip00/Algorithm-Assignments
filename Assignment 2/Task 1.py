#Task 1

#input
inputFile = open('input1.txt','r')
n = int(inputFile.readline())

arr1 = inputFile.readline().split()
i = 0
for s in arr1:
  arr1[i] = int(arr1[i])
  i += 1
inputFile.close()


#checker function for array
def isSorted(arr, length):
  result = False
  if arr[0] > arr[1]:
    for i in range(length-1):
      if arr[i]>arr[i+1]:
        result = True
      else:
        return False
  else:
    for i in range(length-1):
      if arr[i]<arr[i+1]:
        result = True
      else:
        return False
  return result

def bubbleSort(arr, length):
  if isSorted(arr, length) == True: #For best case i.e. if the array is sorted
    pass
  else:
    for i in range(length-1):
        for j in range(length-i-1): 
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]


bubbleSort(arr1,n)
#output
outputFile = open('output1.txt','w')
for i in arr1:
  outputFile.write(str(i)+' ')
outputFile.close()