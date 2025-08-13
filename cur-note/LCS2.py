# A = [""] + list(input())
# B = [""] + list(input())
# LCS = [[""]*len(B) for _ in range(len(A))]
# # LCS[i][j]는 A의 i번째까지의 문자열과
# # B의 j번째까지의 문자열의 LCS 길이 값을 의미함
# # LCS[i][j]에서, 만약 A[i] == B[j]라면
# # 그 두 문자를 제외한 i-1개, j-1개의 LCS
# # 만약 다르다면, i-1개, j개와 i개, j-1개
# # 일 때의 LCS 중 큰 값 취하기. i-1개, j-1개
# # 는 어차피 저 두 케이스보다 반드시 작거나 같으므로
# # 두 케이스만 고려.
# # 그런데 LCS 리스트 원소 값이 LCS 길이 값을 의미하므로,
# # 원소를 LCS 문자열 자체로 둬도 됨. 그럼 길이 값도 갖고
# # 최단 경로도 갖고 있게 됨.
# for i in range(1, len(A)):
#     for j in range(1, len(B)):
#         if A[i] == B[j]:
#             LCS[i][j] = LCS[i-1][j-1] + A[i]
#         else:
#             if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
#                 LCS[i][j] = LCS[i-1][j]
#             else:
#                 LCS[i][j] = LCS[i][j-1]
#
# result = LCS[-1][-1]
# print(len(result), result, sep="\n")

def solution2():
    A = input()
    B = input()
    dp = [[""] * len(B) for _ in range(len(A))]
    answer = ""
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j] and (i == 0 or j == 0): # 이 부분에서 or 대신 and로 해서... 틀렷네
                dp[i][j] = A[i]
            elif A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + A[i]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=lambda s: len(s))
            answer = max(answer, dp[i][j], key=lambda s: len(s))
    if len(answer) == 0:
        print(0)
    else:
        print(len(answer), answer, sep="\n")

def solution3():
    def get_text(u, v):
        if u == 0 or v == 0:
            return
        
        if A[u - 1] == B[v - 1]:
            path.append(A[u - 1])
            get_text(u - 1, v - 1)
        elif dp[u - 1][v] > dp[u][v - 1]:
            get_text(u - 1, v)
        else:
            get_text(u, v - 1)
            
    A = input()
    B = input()
    path = []
    
    len_a = len(A)
    len_b = len(B)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print(dp[i][j])
    get_text(len_a, len_b)
    print(*path[::-1], sep="")

solution3()