def solution():
    from string import ascii_lowercase
    
    S = input()
    q = int(input())
    questions = [tuple(input().split()) for _ in range(q)]
    dp = {i:[0] * len(S) for i in ascii_lowercase}
    for alpha in ascii_lowercase:
        for idx, ch in enumerate(S):
            if alpha == ch:
                dp[alpha][idx] = dp[alpha][idx - 1] + 1
            else:
                dp[alpha][idx] = dp[alpha][idx - 1] if idx - 1 >= 0 else 0
        
    for question in questions:
        alpha = question[0]
        start = int(question[1])
        end = int(question[2])
        
        print(dp[alpha][end] - (dp[alpha][start - 1] if start - 1 >= 0 else 0))
        
solution()