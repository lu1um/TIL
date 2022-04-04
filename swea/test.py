import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(E)]

