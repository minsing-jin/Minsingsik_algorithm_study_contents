# my sol
def solution(survey, choices):

    jipyu = ["R", "T", "C", "F", "J", "M", "A", "N"]
    cvt_choices = [3,2,1,0,1,2,3]

    mbti = dict()
    mbti = dict.fromkeys(jipyu,0)


    # Give personal characteristic score
    for i in range(len(choices)):
        if (1<= choices[i] <=3):
            mbti[survey[i][0]] += cvt_choices[choices[i]-1] 
        elif(5<=choices[i]<=7):
            mbti[survey[i][1]] += cvt_choices[choices[i]-1]


    ans = ''

    # Comparing personer characteristic score indicators
    if mbti['R'] < mbti['T']:
        ans += 'T'
    elif mbti['R'] > mbti['T']:
        ans += 'R'
    else:
        ans += 'R'


    if mbti['C'] < mbti['F']:
        ans += 'F'
    elif mbti['C'] > mbti['F']:
        ans += 'C'
    else:
        ans += 'C'



    if mbti['J'] < mbti['M']:
        ans += 'M'
    elif mbti['J'] > mbti['M']:
        ans += 'J'
    else:
        ans += 'J'


    if mbti['A'] < mbti['N']:
        ans += 'N'
    elif mbti['A'] > mbti['N']:
        ans += 'A'
    else:
        ans += 'A'


    return ans



# other sol
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
