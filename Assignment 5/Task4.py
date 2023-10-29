#COMPLETE
i4 = open('input4.txt','r')
fileInfo = i4.readlines()
allInfo = []
for info in fileInfo:
  x = info.split()
  for i in range(len(x)):
    x[i] = int(x[i])
  allInfo.append(x)

o4 = open('output4.txt','w')
for limits in allInfo:
  c = 0
  a = int(limits[0])
  b = int(limits[1])
  if a == 0 and b == 0:
    pass
  else:
    for i in range(a,b):
      if (i**2) <= b:
        c += 1
    o4.write(f'{c}')    
    o4.write('\n')
o4.close()