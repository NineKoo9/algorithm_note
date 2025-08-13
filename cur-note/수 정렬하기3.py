import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())

    check_list[input_num] = check_list[input_num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)


def solution():
    n = int(input())
    number_count = [0] * 10001
    for _ in range(n):
        number = int(input())
        number_count[number] += 1
    for i in range(10001):
        if number_count[i] == 0:
            continue
        for _ in range(number_count[i]):
            print(i)

solution()