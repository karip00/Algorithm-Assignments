i2 = open('input2.txt')
nZone = int(i2.readline())
matchSeq = (i2.readline())[:-1]
magnetSeq = i2.readline()
zoneDict = {'Y':'Yasnaya', 'P':'Pochinki', 'S':'School', 'R':'Rozhok', 
            'F':'Farm', 'M':'Mylta', 'H':'Shelter', 'I':'Prison'}

def LCS(str1, str2):
  x = len(str1)+1
  y = len(str2)+1

  lcsArray = [[0]*x for i in range(y)]
  btArray = [[None]*x for i in range(y)]

  for i in range(1, x):
    for j in range(1, y):
      if str1[i-1] == str2[j-1]:
        lcsArray[i][j] = lcsArray[i-1][j-1]+1
        btArray[i][j] = 'diagonal'
      elif lcsArray[i-1][j] >= lcsArray[i][j-1]:
        lcsArray[i][j] = lcsArray[i-1][j]
        btArray[i][j] = 'up'
      else:
        lcsArray[i][j] = lcsArray[i][j-1]
        btArray[i][j] = 'left'
      
  return lcsArray, btArray

def backTrack(table, str1, str2):
  result = ''
  i = len(str1)
  j = len(str2)

  while i != 0 and j != 0:
    if table[i][j] == 'diagonal':
      result += str1[i-1]
      i -= 1
      j -= 1
    elif table[i][j] == 'up':
      i -= 1
    elif table[i][j] == 'left':
      j -= 1
  result = result[::-1]
  return result


o2 = open('output2.txt','w')
T = LCS(matchSeq, magnetSeq)[1]
LCS_bt = backTrack(T, matchSeq, magnetSeq)
for s in LCS_bt:
  o2.write(f'{zoneDict[s]} ')
correctness = ((len(LCS_bt))/nZone)*100
o2.write('\n')
o2.write(f'Correctness of prediction: {int(correctness)}%')
o2.close()
