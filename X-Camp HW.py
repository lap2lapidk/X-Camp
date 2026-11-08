# lights=[]
# for i in range(3):
#     d=list(map(int,input().split()))
#     lights.append(d)
# dir=[(0,1),(0,-1),(1,0),(-1,0)]
# count=0
# def dfs(lights):
#     global count
#     if 0 not in lights[0] and 0 not in lights[1] and 0 not in lights[2]:
#         return count
#     for i in range(3):
#         for j in range(3):
#             if lights[i][j]==0:
#                 lights[i][j]=1
#                 count+=1
#                 for d in dir:
#                     x=i+d[0]
#                     y=j+d[1]
#                     if 0<=x<3 and 0<=y<3:
#                         lights[x][y]=1
#             print(lights)
#             dfs(lights)
#             lights[i][j]=0
#             for d in dir:
#                 x=i+d[0]
#                 y=j+d[1]
#                 if 0<=x<3 and 0<=y<3:
#                     lights[x][y]=0
#     return False 

# print(dfs(lights))
# import sys
# sys.setrecursionlimit(10**6)
# rooms=0
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# n, m = map(int, input().split())
# grid = [list(input().strip()) for _ in range(n)]
# def dfs(x,y):
#     if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != '.':
#         return
#     grid[x][y]='#'
#     for d in dir:
#         dfs(x + d[0], y + d[1])
# for i in range(n):
#     for j in range(m):
#         if grid[i][j]=='.':
#             rooms+=1
#             dfs(i,j)
# print(rooms)

# n=int(input())
# pref=[input() for _ in range(n)]
# visited=[False]*n
# ans=0
# def dfs(person):
#     global ans
#     if person==n:
#         ans+=1
#         return
#     for book in range(n):
#         if pref[person][book]=='1' and not visited[book]:
#             visited[book]=True
#             dfs(person+1)
#             visited[book]=False
# dfs(0)
# print(ans)

# n,k=map(int,input().split(),reverse=True)
# tasks=sorted(map(int,input().split()),reverse=True)
# machines=[0]*k
# ans=float('inf')
# def dfs(idx):
#     global ans
#     if idx==n:
#         ans=min(ans,max(machines))
#         return
#     for i in range(k):
#         if machines[i]+tasks[idx] <= ans: continue
#         machines[i]+=tasks[idx]
#         dfs(idx+1)
#         machines[i]-=tasks[idx]
# dfs(0)
# print(ans)

# cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
# milk = {cow: 0 for cow in cows}
# n=int(input())
# for _ in range(n):
#     line=input().split()
#     cow=line[0]
#     amount=int(line[1])
#     milk[cow]+=amount
# sort=sorted(set(milk.values()))
# if len(sort)<2:
#     print("Tie")
# else:
#     second_lowest=sort[1]
#     winners=[cow for cow, amount in milk.items() if amount==second_lowest]
#     if len(winners)==1:
#         print(winners[0])
#     else:
#         print("Tie")

# n=int(input())
# mailboxes=input()
# for k in range(1,n+1):
#     seen=set()
#     unique=True
#     for i in range(n-k+1):
#         substring=mailboxes[i:i+k]
#         if substring in seen:
#             unique=False
#             break
#         seen.add(substring)
#     if unique:
#         print(k)
#         break

# set=set()
# n=int(input())
# line=input().split()
# for word in line:
#     set.add(word)
# print(len(set))

# n,x=map(int,input().split())
# arr=list(map(int,input().split()))
# seen=dict()
# if len(arr)<2:
#     print("IMPOSSIBLE")
# for i in range(n):
#     num=arr[i]
#     if num not in seen:
#         seen[num]=i
#     complement=x-num
#     if complement in seen:
#         print(seen[complement]+1, i+1)
#         break
# else:
#     print("IMPOSSIBLE")

while True:
    first = input().split()
    if first[0]=='0':
        break
    n,a,b=int(first[0]),int(first[1]),int(first[2])
    k=[0]+list(map(int,input().split()))
    dist = [-1] * (n + 1)
    dist[a] = 0
    q = [a]
    head = 0
    while head<len(q):
        cur = q[head]
        head += 1
        if cur == b:
            break
        for nx in (cur + k[cur], cur - k[cur]):
            if 1 <= nx <= n and dist[nx] == -1:
                dist[nx]=dist[cur]+1
                q.append(nx)
    print(dist[b])