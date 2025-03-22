# my sol
def solution(id_pw, db):
    for i in db:
        print(i)
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
        else:
            if i == db[len(db)-1]:
                return "fail"

              
              
# other sol
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
