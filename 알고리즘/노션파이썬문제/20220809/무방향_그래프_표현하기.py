'''그래프 입력이 주어질 때 `무방향` 그래프를 인접 행렬과 인접 리스트로 표현하세요.
첫째 줄에 `정점의 개수 N`과 `간선의 개수 M`이 주어진다.
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
인접 행렬을 출력하고, 인접 리스트를 출력하세요.'''

from pprint import pprint
import sys
sys.stdin = open('무방향_그래프_표현하기.txt')

n, m = map(int, input().split())

graph = []
for i in range(n+1):
    graph.append([0]* (n+1))
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
print(graph)

list_ = [[] * (n+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1:
            list_[i].append(j)
pprint(list_)