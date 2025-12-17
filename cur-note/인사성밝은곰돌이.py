def solution():
    from collections import defaultdict
    
    N = int(input())
    chat_log = [input() for _ in range(N)]
    count = 0
    hello_username = defaultdict(int)
    for log in chat_log:
        if log == "ENTER":
            hello_username.clear()
            continue
        if log in hello_username:
            continue
        hello_username[log] = 1
        count += 1
    print(count)

solution()