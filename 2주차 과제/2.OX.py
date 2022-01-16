N=int(input())

for i in range(N) :
    OX=input()
    ans = 0
    cnt = 0
    for j in OX :
        if j == "O" :
            cnt = cnt + 1
            ans = ans + cnt
        else :
            cnt = 0
    print(ans)
