n = int(input())
def factor(n):
  if n > 0:
    return n * factor(n-1)
  else:
    return 1
print(factor(n))