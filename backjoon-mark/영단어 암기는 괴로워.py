def solution():
    from collections import defaultdict
    import sys
    
    i = sys.stdin.readline
    N, M = map(int, i().split())
    words = [i().strip() for _ in range(N)]
    word_count_dic = defaultdict(int)
    for word in words:
        if len(word) < M:
            continue
        word_count_dic[word] += 1
    word_count = [(word, count) for word, count in word_count_dic.items()]
    word_count.sort(key=lambda word: (-word[1], -len(word[0]), word[0]))
    for word, count in word_count:
        print(word)

solution()