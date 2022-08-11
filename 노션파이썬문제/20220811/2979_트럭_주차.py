import sys
sys.stdin = open('2979_트럭_주차.txt')

# A: 트럭 1대
# B: 트럭 2대
# C: 트럭 3대
# x: 주차장 도착 시간
# y: 주차장 떠난 시간

A, B, C = map(int, input().split())

park = []

for _ in range(3):
    car = list(map(int, input().split()))
    park.append(car)

F_car_time = park[0][0]

