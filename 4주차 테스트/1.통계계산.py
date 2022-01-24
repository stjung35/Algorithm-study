from collections import Counter

list = []
n = int(input())
for _ in range(n):
    list.append(int(input()))

list.sort

print(round(sum(list)/n))

print(sorted(list)[n//2])


count = Counter(list).most_common() 
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(max(list) - min(list))


