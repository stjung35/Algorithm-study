x= int(input("X축을 입력하시오."))
y= int(input("Y축을 입력하시오."))

if x>0 :
    if y>0 :
        print("1사분면입니다.")
    else :
        print("4사분면입니다.")
elif x<0 :
    if y>0 :
        print("2사분면입니다.")
    else :
        print("3사분면입니다.")
else :
    0
