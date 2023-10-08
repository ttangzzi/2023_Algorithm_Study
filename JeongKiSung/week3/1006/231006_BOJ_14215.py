a, b, c = map(int,input().split())
slot = [a,b,c]
slot.sort()
if slot[2] >= slot[0] + slot[1]:
  print(slot[0] + slot[1] + (slot[0]+slot[1]-1))
else:
  print(a+b+c)