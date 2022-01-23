while True :
  data = list(map(int, input().split()))
  if data[0] == 0 and data[1] == 0 and data[2] == 0 :
    break
  
  data.sort
  if data[0] >= data[1] + data[2] :
    print("Invalid")
  else :
    if data[0] == data[1] == data[2] :
      print("Equilateral")
    elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2] :
      print("Isosceles")
    else :
      print("Scalene")
