T = int(input())
for _ in range(T):
    hp1, mp1, str1, def1, hp2, mp2, str2, def2 = map(int, input().split())

    hp12 = 1 if (hp1 + hp2) < 1 else (hp1 + hp2)
    mp12 = 1 if (mp1 + mp2) < 1 else (mp1 + mp2)
    str12 = 0 if (str1 + str2) < 0 else (str1 + str2)

    print(1 * hp12 + 5 * mp12 + 2 * str12 + 2 * (def1 + def2))