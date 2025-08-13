def solution():
    def get_palindrome(start, end):
        while 0 <= start <= end < len(board_numbers):
            if board_numbers[start] == board_numbers[end]:
                answers.add((start, end))
                start -= 1
                end += 1
            else:
                break

    N = int(input())
    board_numbers = list(map(int, input().split()))
    M = int(input())
    questions = [tuple(map(lambda num: int(num) - 1, input().split())) for _ in range(M)]

    answers = set()

    # 길이가 1인 경우 저장
    for i in range(N):
        answers.add((i, i))

    # 자 이제부터 모든 펠린드롬을 구해보자
    for idx in range(len(board_numbers)):
        get_palindrome(idx, idx + 1)
        get_palindrome(idx, idx + 2)
    for q in questions:
        if q in answers:
            print(1)
        else:
            print(0)

def solution2():
    N = int(input())
    board_numbers = list(map(int, input().split()))
    M = int(input())
    questions = [tuple(map(lambda num: int(num) - 1, input().split())) for _ in range(M)]

    dp = [[0] * N for _ in range(N)]

    # 길이가 1인 경우 초기화를 해줘야 하고
    for i in range(N):
        dp[i][i] = 1
    # 길이가 2인 경우도 초기화해줘야한다.
    for i in range(N - 1):
        if board_numbers[i] == board_numbers[i + 1]:
            dp[i][i + 1] = 1

    # 이제부터 다른 녀석들의 맞나 틀리냐를 찾아보자
    # 어 이게 디피 탑다운인가...?
    # 와... 여기 길이에 플1과 I에 플 1과 j에 -1 순간 엄청 헷갈렸네...
    for length in range(3, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if board_numbers[i] == board_numbers[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1

    for s, e in questions:
        if dp[s][e]:
            print(1)
        else:
            print(0)

solution2()