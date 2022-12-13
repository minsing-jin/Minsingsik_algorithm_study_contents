import copy
def solution(strings, n):
    
    strings.sort(key= lambda x: (x[n]))
    tmp = []
                
    # print(strings)
    copy_strings = copy.deepcopy(strings)
    
    for i in range(len(strings)-1):
      # print('idx :', i)
      if strings[i][n] == strings[i+1][n]:
        tmp.append(strings[i])
        if strings[i+1][n] != strings[i+2][n]:
          tmp.append(strings[i+1])
    
    # print(tmp)
    if len(tmp) > 1:
      start_idx_search_val = tmp[0]
      end_idx_search_val = tmp[len(tmp)-1]
      
      tmp.sort()
      cnt = 0
      
      for n in tmp:
        
        copy_strings[strings.index(start_idx_search_val)+cnt] = n
        cnt += 1
        print(strings)


    return copy_strings


    # 다양한 종류의 알파벳이 겹친다면?
