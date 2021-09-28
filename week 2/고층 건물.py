n = int(input())
building = list(map(int, input().split()))

check_buildings = 0
sum_buildings = []

for i in range(n):
    check_buildings = 0 # check_building 초기화
    #left side
    inc = 9999999999
    for j in range(i-1, -1, -1):
        d = (building[i] - building[j]) / ((i+1) - (j+1))
        if d < inc:
            check_buildings += 1
            inc = d

    #left side
    inc = -9999999999
    for j in range(i+1, n):
        d = (building[i] - building[j]) / (i - j)
        if d > inc:
            check_buildings += 1
            inc = d
    sum_buildings.append(check_buildings)

print(sum_buildings)
print(max(sum_buildings))