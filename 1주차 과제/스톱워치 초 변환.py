sec = int(input("초를 입력하시오."))
hr = sec // 3600
sec = sec - hr*3600
mu = sec // 60
ss = sec - mu*60
print(hr, "시간", mu, "분", ss, "초 입니다.")
