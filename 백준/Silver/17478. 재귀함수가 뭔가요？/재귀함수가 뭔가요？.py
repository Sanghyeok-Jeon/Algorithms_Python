def what_is_recursion(n):
    if n == N:
        print('____' * n + '"재귀함수가 뭔가요?"')
        print('____' * n + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * n + '라고 답변하였지.')
        return

    print('____' * n + '"재귀함수가 뭔가요?"')
    print('____' * n + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('____' * n + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('____' * n + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

    what_is_recursion(n + 1)
    print('____' * n + '라고 답변하였지.')

N = int(input())

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
what_is_recursion(0)