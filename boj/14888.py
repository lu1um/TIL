import sys
sys.stdin = open('input.txt')

from itertools import permutations

def add(left, right):
    return left + right

def sub(left, right):
    return left - right

def mul(left, right):
    return left * right

def div(left, right):
    negative = 1
    if left<0 and right>0:
        negative = -1
        left *= -1
    res = left // right * negative
    return res

OPERATOR = {
    0: add,
    1: sub,
    2: mul,
    3: div
}

N = int(input())
numbers = list(map(int, input().split()))
operators = map(int, input().split())

ops = list()
for idx, op in enumerate(operators):
    ops.extend([idx]*op)

cases = set(permutations(ops, len(ops)))

min_num = 1e9
max_num = -1e9
for case in cases:
    left = numbers[0]
    for i in range(N-1):
        right = numbers[i+1]
        left = OPERATOR[case[i]](left, right)
    min_num = min(min_num, left)
    max_num = max(max_num, left)

print(max_num)
print(min_num)