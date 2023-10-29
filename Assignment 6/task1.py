def fastestZero(num):
  arr = [1000]*(num+1)
  for i in range(num+1):
    if i == 0:
      arr[i] = 0
    else:
      for j in str(i):
        dig = int(j)
        arr[i] = min(arr[i],arr[i-dig]+1)
  return arr[num]

i1 = open('input1.txt','r')
n = int(i1.readline())
i1.close()

o1 = open('output1.txt','w')
o1.write(f'Minimum Steps: {fastestZero(n)}')
o1.close()
