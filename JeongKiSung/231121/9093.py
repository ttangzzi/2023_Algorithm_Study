N = int(input())
for _ in range(N):
  str = list(input().split())
  for i in range(len(str)):
    str_list = list(str[i]) # str[i]를 list로
    str_list.reverse() # list str[i]를 reverse
    print("".join(str_list), end = " ") # 다시 문자열로
  print()