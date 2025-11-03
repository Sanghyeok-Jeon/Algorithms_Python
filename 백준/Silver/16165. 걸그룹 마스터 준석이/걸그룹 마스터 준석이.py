N, M = map(int, input().split())
group_to_members = {}
member_to_group = {}

for _ in range(N):
    team_name = input()
    team_member_count = int(input())
    team_member = [input() for _ in range(team_member_count)]

    group_to_members[team_name] = sorted(team_member)
    for member in team_member:
        member_to_group[member] = team_name

for _ in range(M):
    question = input()
    question_type = int(input())

    if question_type == 0:
        for member in group_to_members[question]:
            print(member)
    else:
        print(member_to_group[question])