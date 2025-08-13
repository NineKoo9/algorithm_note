def solution():
    n = int(input())
    members = [(input().split(), i) for i in range(n)]
    members.sort(key=lambda member:(int(member[0][0]), member[1]))
    for member in members:
        print(" ".join(member[0]))

def solution2():
    N = int(input())
    members = [[i] + list(input().split()) for i in range(N)]
    members.sort(key=lambda member: (int(member[1]), member[0]))
    for member in members:
        print(member[1], member[2])
solution2()