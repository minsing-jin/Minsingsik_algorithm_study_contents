def solution(number, limit, power):
    tmp = [1]
    cnt = 0
    if number > 1:
      for n in range(2,number+1):
          print("n: ", n)

          for i in range(1, (n//2)+1):
              
              if n%i == 0:
                  cnt += 1
          print("before cnt: ", cnt)
          



          if cnt % 2 == 0:
            
            cnt = (cnt*2)-1

          else:
            cnt = cnt *2
          print("cnt: ", cnt)
          




          if cnt > limit:
            tmp.append(power)
          else:
            tmp.append(cnt)  
          cnt = 0
          
          print("tmp: ", tmp)

          
    return sum(tmp)



#  n의 반절이 약수의 중앙값이 되지 않는다 -> 착각!
