L = [1,2,3,4,5]

for y,x in [(0,4)]:
    L[x],L[y] = L[y],L[x]

print(L)