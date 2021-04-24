"""
회장뽑기 

문제
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.

4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

입력
입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

출력
첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.

"""

import sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
	graph[i][i]=0

a,b=0,0

while a!=-1 and b!=-1:
	a,b=map(int,input().split())
	graph[a][b]=1
	graph[b][a]=1

for i in range(1,n+1):
	for a in range(1,n+1):
		for b in range(1,n+1):
			graph[a][b]= min(graph[a][b],graph[a][i]+graph[i][b])
			#a,b가 서로 친구가 아니면 INF일 것이고 a와i가 친구이고 i와b가 친구이면 더한값
			#이미 친구거나 친구의친구....등 일때 갱신X
			#만약 2+1이라면 친구의친구의친구라는 뜻

min_score=INF
candidate=[]
for i in range(1,n+1):
	min_score=min(min_score,max(graph[i][1:]))

for i in range(1,n+1):
	if max(graph[i][1:])==min_score:
		candidate.append(i)

print(min_score, len(candidate))
for c in candidate:
	print(c, end=' ')
