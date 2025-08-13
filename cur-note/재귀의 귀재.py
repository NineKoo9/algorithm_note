def solution():
    def recursion(s, start, end, count):
        if start >= end:
            return (1, count)
        elif s[start] != s[end]:
            return (0, count)
        else:
            return recursion(s, start + 1, end - 1, count + 1)
    
    def is_palindrome(s):
        return recursion(s, 0, len(s) - 1, 1)
    
    
    T = int(input())
    s_lst = [input() for _ in range(T)]
    for s in s_lst:
        result, count = is_palindrome(s)
        print(result, count)

solution()