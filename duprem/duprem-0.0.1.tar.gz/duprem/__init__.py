def duprem(l):
  l1=[]
  for i in l:
    if(i not in l1):
      l1.append(i)
  return l1