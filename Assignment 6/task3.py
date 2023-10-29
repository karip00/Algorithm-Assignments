def lcs_table(x, y, z):
  m = len(x)+1
  n = len(y)+1
  o = len(z)+1

  c = [[[0]*o for i in range(n)]for j in range(m)]
  for i in range(m):
    for j in range(n):
      for k in range(o):
        if i == 0 or j == 0 or k == 0:
          c[i][j][k] = 0
        else:
          if x[i-1] == y[j-1] and x[i-1] == z[k-1]:
            c[i][j][k] = 1 + c[i-1][j-1][k-1]
          else:
            if c[i-1][j][k] >= c[i][j-1][k]:
              max = c[i-1][j][k]
              if max >= c[i][j][k-1]:
                c[i][j][k] = max
              else:
                max = c[i][j][k-1]
                c[i][j][k] = max
            else:
              max = c[i][j-1][k]
              if max >= c[i][j][k-1]:
                c[i][j][k] = max
              else:
                max = c[i][j][k-1]
                c[i][j][k] = max
  return c[m-1][n-1][o-1]

i3 = open('input3.txt', 'r')
f3 = i3.readlines()
f3Info = []
for i in range(len(f3)):
  if f3[i] == f3[-1]:
    f3Info.append(f3[i])
  else:
    f3Info.append(f3[i][:-1])
x1 = f3Info[0]
x2 = f3Info[1]
x3 = f3Info[2]
o3 = open('output3.txt', 'w')
o3.write(str(lcs_table(x1, x2, x3)))
o3.close()