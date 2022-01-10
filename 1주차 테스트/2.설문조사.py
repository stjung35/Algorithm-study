a = int(input("설문 참여 인원수를 입력하시오."))
b = []
for i in range(a) : 
    b.append(int(input()))
zero_count = b.count(0)
one_count = b.count(1)
if zero_count > one_count :
    print("준희는 귀엽지 않다.")
else :
    print("준희는 귀엽")
            
