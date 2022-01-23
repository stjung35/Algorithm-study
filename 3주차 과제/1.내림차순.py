n = int(input())
a = list(str(n))
a.sort()
a.reverse()
for n in a:
    print(n,end="")
