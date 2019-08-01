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
      
