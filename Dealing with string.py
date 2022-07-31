# my sol
 def solution(s):
    if len(s) in (4,6) and s.isdigit() == True:
        return True
    return False

# other sol
# def solution(s)-> bool:
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False

# other sol
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
