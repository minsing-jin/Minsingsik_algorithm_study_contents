# my sol
def solution(s):
    s_dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in s_dic:
         if i in s:
            s = s.replace(i, str(s_dic[i]))
    return int(s)
  
# other sol
#1
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)


  
  
#2


def solution(s):
    if 'one' in s:
        s= s.replace('one', '1')
    if 'zero' in s:
        s= s.replace('zero', '0')
    if 'two' in s:
        s= s.replace('two', '2')
    if 'three' in s:
        s= s.replace('three', '3')
    if 'four' in s:
        s= s.replace('four', '4')
    if 'five' in s:
        s= s.replace('five', '5')
    if 'six' in s:
        s= s.replace('six', '6')
    if 'seven' in s:
        s= s.replace('seven', '7')
    if 'eight' in s:
        s= s.replace('eight', '8')
    if 'nine' in s:
        s= s.replace('nine', '9')

    return int(s)
