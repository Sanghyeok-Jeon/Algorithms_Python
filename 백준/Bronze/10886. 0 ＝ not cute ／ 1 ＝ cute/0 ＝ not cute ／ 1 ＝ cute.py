N = int(input())
cntVote = {0:0, 1:0}
for _ in range(N):
    vote = int(input())
    cntVote[vote] += 1

if cntVote[0] > cntVote[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')