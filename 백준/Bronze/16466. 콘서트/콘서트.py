N = int(input())
tickets = sorted(list(map(int, input().split())))

ticket_no = 0
for i in range(N):
    ticket_no += 1
    if ticket_no != tickets[i]:
        break

    if i == N - 1:
        ticket_no += 1

print(ticket_no)