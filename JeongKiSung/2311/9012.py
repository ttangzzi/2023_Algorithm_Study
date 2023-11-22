N = int(input())

for _ in range(N):
  par = input()
  stack_count = 0
  for i in range(len(par)):
    if stack_count < 0:
      break
    else:
      if par[i] == "(":
        stack_count += 1
      elif par[i] == ")":
        stack_count -= 1
  if stack_count == 0:
    print("YES")
  else:
    print("NO")