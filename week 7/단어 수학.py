n = int(input())
answer = 0
saving = {}
values = []
num = 9

for _ in range(n):
    word = input()
    for s in range(len(word)):
        if word[s] in saving:
            saving[word[s]] += 10 ** (len(word) - 1 - s)
        else:
            saving[word[s]] = 10 ** (len(word) - 1 - s)

# print(saving)

for i in saving.values():
    values.append(i)

values.sort(reverse = True)

#print(values)

for j in values:
    answer += num * j
    num -= 1

print(answer)