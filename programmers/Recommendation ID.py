# my sol
def solution(new_id):


    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    tmp = []
    for i in new_id:    
        tmp.append(i.lower())
    # tmp = ''.join(tmp)

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    tmp2=[] # 위에 해당하는 녀석만 append

    for alph in tmp:   # 알파벳 or 숫자인지 append
        if alph.isalnum() == True:
            tmp2.append(alph)

        if '-' in alph:
            tmp2.append(alph)

        if '_' in alph:
            tmp2.append(alph)

        if '.' in alph:
            tmp2.append(alph)
    # tmp2 = ''.join(tmp2)
    # print(tmp2)
    # print(len(tmp2))

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    idx_jum = []
    for jum in range(1,len(tmp2)):

        try:
            if tmp2[jum-1] == '.':
                if tmp2[jum-1] == tmp2[jum]: 
                    tmp2[jum-1] = ' '

        except:
            break

    tmp2 = ''.join(tmp2).replace(" ","")
    print(tmp2)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    tmp2 = tmp2.strip('.')
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(tmp2) == 0:
        tmp2 = 'a'
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(tmp2) >= 16:
        tmp2 = tmp2[:15]
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if tmp2[14] == '.':
            tmp2 = tmp2[:14]
    print(tmp2)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(tmp2) < 3:
        tmp2 = tmp2 + tmp2[len(tmp2)-1]

    return tmp2


  
  -------------------------------------------

# other sol1
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

-----------------------------------------------------  
  
  
# other sol 2
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
