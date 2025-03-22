def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    const_alpha_len = 20
    ans = ''
    skip = ''.join(set(skip))
    # skip 알파벳 alpha에서 빼기
    for i in alpha:
        for n in skip:
            if i == n:

                alpha = alpha.replace(i, "")
    n = 1


    for i in s:
        print(i)
        print(alpha.index(i))
        if alpha.index(i)+index < len(alpha):
            print(i)
            ans += alpha[alpha.index(i)+index]
            print("ans: ", ans)
#       alpha.index(i)+index가 기존 알파벳 길이를 초과하면
        else:
          while True:
            if ((alpha.index(i)+index) - len(alpha)*n) < len(alpha):
                ans += alpha[(alpha.index(i)+index) - (len(alpha)*n)]
                print("ans: ", ans)
                n = 1
                break
            else:
                n += 1

    return ans


# other sol
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result


def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip]
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s])
