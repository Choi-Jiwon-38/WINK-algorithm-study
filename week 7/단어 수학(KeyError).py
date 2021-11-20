n = int(input())
answer = 0
saving = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0}
values = []
num = 9

for _ in range(n):
    word = input()
    for s in range(len(word)):
        saving[word[s]] += 10 ** (len(word) - 1 - s)

# print(saving)

for i in saving.values():
    values.append(i)

values.sort(reverse = True)
# print(values)

for j in values:
    if j == 0:
        break
    else:
        answer += num * j
        num -= 1

print(answer)