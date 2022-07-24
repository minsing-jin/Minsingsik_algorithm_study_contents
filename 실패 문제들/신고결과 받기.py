def solution(id_list, report, k):

    report = set(report)  # 중복조건 빼주기!!!

    report_list = []

    answer = {id : 0 for id in id_list}
    id_dic_report_cnt = {id : 0 for id in id_list}

    for i in report:
        id_dic_report_cnt[i.split()[1]] += 1 # id당 리폿당한 횟수 카운팅

    for n in report:
        if id_dic_report_cnt[n.split()[1]] >= k:
            answer[n.split()[0]] += 1



    return list(answer.values())
