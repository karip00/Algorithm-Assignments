# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eltOoL0vmdrWJpSuFIfEoJlubDEbY9Uo
"""

def Multiply_Matrix(A, B, n):
  C = [[0]*n for i in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C


f1 = open('matrix_input.txt','r')
list1 = f1.readline().split()
list2 = f1.readline().split()
n = int(f1.readline())
f1.close()

A =[[0]*n for i in range(n)]
B = [[0]*n for j in range(n)]
  
i1 = 0 #iterator for rows
idx = 0 #index of list1
while i1 < n:
  i2 = 0
  while i2 < n:
    list1[idx] = int(list1[idx])
    list2[idx] = int(list2[idx])
    A[i1][i2] += list1[idx]
    B[i1][i2] += list2[idx]
    idx += 1
    i2 += 1
  i1 += 1

output = Multiply_Matrix(A,B,n)
f2 = open('matrix_output.txt', 'w')
f2.write(str(output))
f2.close()