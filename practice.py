# https://atcoder.jp/contests/abc136/tasks/abc136_c

N = int(input()) #目的
H =[int(i) for i in input().split()]

flug = 0
for index in range(1,N):
  if int(H[index]- H[index - 1]) < -1 :
    print("No")
    flug = 1
    break
  else:
    if int(H[index] < H[index - 1]):
      H[index] = H[index-1]
   # print(H[index])
    continue
if flug == 0:
  print("Yes")


# https://atcoder.jp/contests/abc136/tasks/abc136_b
N = int(input()) #目的

ans = 0
#print(len(str(10)) % 2)
for num in range(1,N+1):
  #print(len(nem))
  if int(len(str(num))) % 2 == 1:
     ans += 1
      
print(int(ans))


# https://atcoder.jp/contests/abc136/tasks/abc136_a

list1=[int(i) for i in input().split()]
A = list1[0]
B = list1[1]
C = list1[2]
#print(A)

tobe = int(A)- int(B)
if tobe < 0:
  tobe = int(0)

#print(tobe)

answer = int(C) - int(tobe)
if answer < 0:
  answer = int(0)
print(int(answer))




#　https://atcoder.jp/contests/abc088/tasks/abc088_a

N = int(input()) #目的
A = int(input()) #1円の枚数

#500円で払える箇所まで割る
amari = N % 500
#print(int(amari))


if amari <= A:
  print("Yes")
else:
  print("No")



#https://atcoder.jp/contests/abc086/tasks/abc086_a

list1=[int(i) for i in input().split()]
a = list1[0]
b = list1[1]
math = a * b
if math % 2 ==0:
  print("Even")
else:
  print("Odd")


# https://atcoder.jp/contests/abc086/tasks/abc086_b

import math

list1=[i for i in input().split()]
a = list1[0]
b = list1[1]

ab = int(a + b)
#print(ab)
ans = int(math.sqrt(ab))
#print(ans)

if ans * ans == ab:
  print("Yes")
else:
  print("No")

# https://atcoder.jp/contests/abc081/tasks/abc081_b


N = int(input())
list1=[int(i) for i
       in input().split()]

count = 0
flug = bool(False)
#print(len(list1))
while flug == False:
  for i in range(len(list1)):
    if list1[i] % 2 != 0:
      #print("here")
      flug = bool(True)
      count = count - 1
      break
    list1[i] = int(list1[i]) / 2
  count = count + 1
print(count)
      
