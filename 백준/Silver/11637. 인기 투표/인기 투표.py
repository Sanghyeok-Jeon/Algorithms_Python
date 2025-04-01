T = int(input())
for _ in range(T):
    n = int(input())

    # 총 투표수
    total_vote = 0
    list_candidate = []
    for i in range(1, n + 1):
        tmp_vote = int(input())
        total_vote += tmp_vote
        list_candidate.append((tmp_vote, i))

    list_candidate.sort(key=lambda x:-x[0])

    # 최다 득표자가 1명 초과일 경우
    if list_candidate[0][0] == list_candidate[1][0]:
        print('no winner')
    else:
        # 최다 득표자가 과반수 득표를 했을 경우
        if list_candidate[0][0] > total_vote // 2:
            print('majority winner {}'.format(list_candidate[0][1]))
        # 최다 득표자가 절반 이하의 득표를 하였을 경우
        else:
            print('minority winner {}'.format(list_candidate[0][1]))