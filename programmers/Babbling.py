# my sol

def solution(babbling):
    ans = 0

    for i in babbling:
        if 'aya' in i:
            i = i.replace("aya",'1')
            #print(i)
        if 'ye' in i:
            i = i.replace('ye','2')
            #print(i)
        if 'woo' in i:
            i = i.replace('woo','3')
            #print(i)
        if 'ma' in i:
            i = i.replace('ma','4')
        if i.isdigit() == True:
            for n in range(len(i)-1):

                if i[n] == i[n+1]:
                    i = 'overlap'
                    break

        if i.isdigit() == True:
            ans += 1


    return ans
  
  
  
  
  -----------------------------------------------------------------------------------------------------------
  
  
  
  
  # other sol
  
  def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
