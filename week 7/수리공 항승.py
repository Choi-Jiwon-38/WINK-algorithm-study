n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort() # 리스트의 요소를 오름차순으로 정렬

answer = 1
end = hole[0] + l - 1

for i in hole:
    if end >= i:
        continue
    else:
        answer += 1
        end = i + l - 1

print(answer)