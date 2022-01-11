# 백준 알고리즘 저지 2110번

import sys
from itertools import combinations

input = sys.stdin.readline

N, C = map(int, input().split())

num_list = []

for _ in range(N):
    num_list.append(int(input()))

comb_list = list(combinations(num_list, C))

print(comb_list)

min_list = []

for i in range(len(comb_list)):
    temp = []
    for j in range(C-1):
        temp.append(comb_list[i][j+1] - comb_list[i][j])
    min_list.append(min(temp))

print(max(min_list))