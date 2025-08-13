def solution():
    N = int(input())
    logs = [tuple(input().split()) for _ in range(N)]
    dancing_people = {"ChongChong":1}
    for p1, p2 in logs:
        if p1 in dancing_people:
            dancing_people[p2] = 1
        elif p2 in dancing_people:
            dancing_people[p1] = 1
    print(len(dancing_people))


solution()