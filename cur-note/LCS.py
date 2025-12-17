def solution():
    A = input()
    B = input()
    dp = [[0] * len(A) for _ in range(len(B))]  # y축이 B에 관한 것이고 x 축이 A에 관한 것이다.
    max_value = -int(1e9)
    for y in range(len(B)):
        for x in range(len(A)):
            if B[y] == A[x] and (y == 0 or x == 0):
                dp[y][x] = 1
            elif B[y] == A[x]:
                dp[y][x] = dp[y - 1][x - 1] + 1
            else:
                dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])    
            max_value = max(max_value, dp[y][x])
    print(max_value)


def solution2():
    A = input()
    B = input()
    max_value = -1
    dp = [[0] * len(B) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j] and i == 0 and j == 0:
                dp[i][j] = 1
            elif A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            max_value = max(max_value, dp[i][j])
    print(max_value)

def solution3():
    A = input()
    B = input()

    dp = [[0] * len(B) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i][j] = max(dp[i][j],  1 + (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0))
            else:
                dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0, dp[i][j - 1] if j - 1 >= 0 else 0)
    print(dp[len(A) - 1][len(B) - 1])

def solution4():
    A = input()
    B = input()
    
    len_A = len(A)
    len_B = len(B)
    
    dp = [[0] * len_B for _ in range(len_A)]
    for i in range(len_A):
        for j in range(len_B):
            if A[i] == B[j]:
                if i - 1 < 0 or j - 1 < 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0, dp[i][j - 1] if j - 1 >= 0 else 0)
    print(dp[len_A - 1][len_B - 1])
                
            
    
    

solution3()