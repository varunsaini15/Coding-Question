n=int(input())
arr=list(map(int,input().split()))
a=[i for i in range(n)]
ans=[]
for i in a:
ans.append(arr.index(i))
print(*ans)
