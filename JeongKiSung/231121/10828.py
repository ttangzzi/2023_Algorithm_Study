import sys
N = int(sys.stdin.readline()) # 횟수
X = [] # stack array

for _ in range(N):
  write = sys.stdin.readline().split() # 공백에 따라 write[0], write[1]
  if write[0] == "push":
    X.append(write[1]) # push 1 을 했다면 write[1]는 1

  elif write[0] == "pop":
    if len(X) > 0:
      print(X.pop())
    else:
      print(-1)

  elif write[0] == "size":
    print(len(X))

  elif write[0] == "empty":
    if len(X) == 0:
      print(1)
    else:
      print(0)

  elif write[0] == "top":
    if len(X) > 0:
      print(X[(len(X)-1)]) # stack은 후입선출이므로 top 값이 맨 끝값
    else:
      print(-1)