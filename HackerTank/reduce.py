N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) )
for j in n:
    print(type(j))
    print(type(j[::-1]))
    j == j[::-1]