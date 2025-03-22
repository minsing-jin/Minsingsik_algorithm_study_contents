# my sol
def solution(s):


    tmp = [i for i in s]
    tmp2 = s.split()
    adjust = 0
    for i in range(len(tmp)):
        if tmp[i].isalpha() == False:
            adjust = 0
        else:
            if adjust%2 == 0:
                tmp[i] = tmp[i].upper()
                adjust += 1

            else:
                tmp[i] = tmp[i].lower()
                adjust += 1




    return "".join(tmp)
  
  
  
# other sol
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
