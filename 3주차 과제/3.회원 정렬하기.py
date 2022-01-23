num = int(input())
list = []

for _ in range(num):
    age,name = map(str, input().split())
    age = int(age)
    list.append((age, name))

list.sort(key = lambda a: (a[0]))

for a in list:
    print(a[0],a[1])
